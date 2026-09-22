

import numpy as np
import pandas as pd
import streamlit as st

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(page_title="Food Delivery Analytics", page_icon="🍔", layout="wide")

DATA_FILE = "Order_delivery.csv"
TARGET = "Delivery_Duration_Minutes"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_FILE)
    df.columns = df.columns.str.strip().str.replace(" ", "_", regex=False)

    for col in [
        "Quantity", "Total_Price", "Delivery_Duration_Minutes",
        "Delivery_Distance_km"
    ]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df["Order_Time"] = pd.to_datetime(df["Order_Time"], errors="coerce")
    df = df.drop_duplicates().copy()
    df = df[df[TARGET].notna() & (df[TARGET] > 0)].copy()
    df = df[df["Delivery_Distance_km"].notna() & (df["Delivery_Distance_km"] >= 0)].copy()

    df["Order_Hour"] = df["Order_Time"].dt.hour
    df["Order_DayOfWeek"] = df["Order_Time"].dt.dayofweek
    df["Order_Month"] = df["Order_Time"].dt.month
    df["Is_Weekend"] = (df["Order_DayOfWeek"] >= 5).astype(int)

    return df

df = load_data()

# Only the most useful and practical pre-delivery parameters are exposed in the UI.
PREDICTION_FEATURES = [
    "Delivery_Distance_km",
    "Traffic_Level",
    "City",
    "Driver_Vehicle",
    "Driver_Availability",
    "Order_Hour",
    "Is_Weekend"
]

@st.cache_resource
def train_prediction_model(data):
    X = data[PREDICTION_FEATURES].copy()
    y = data[TARGET].copy()

    numeric_features = ["Delivery_Distance_km", "Order_Hour", "Is_Weekend"]
    categorical_features = [
        "Traffic_Level", "City", "Driver_Vehicle", "Driver_Availability"
    ]

    preprocessor = ColumnTransformer([
        ("num", Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ]), numeric_features),
        ("cat", Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore"))
        ]), categorical_features)
    ])

    model = Pipeline([
        ("preprocessor", preprocessor),
        ("model", RandomForestRegressor(
            n_estimators=200,
            random_state=42,
            n_jobs=-1
        ))
    ])

    model.fit(X, y)
    return model

model = train_prediction_model(df)

st.title("🍔 AI-Based Food Delivery Time Prediction and Operational Analytics")
st.caption("Data Analytics with AI | Academic Internship Project")

page = st.sidebar.radio(
    "Select Page",
    ["Overview", "Data Analysis", "Delivery Time Prediction", "Business Insights"]
)

if page == "Overview":
    st.header("Overview")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Orders", f"{len(df):,}")
    c2.metric("Avg Delivery Time", f"{df[TARGET].mean():.2f} min")
    c3.metric("Avg Distance", f"{df['Delivery_Distance_km'].mean():.2f} km")
    c4.metric("Avg Order Value", f"{df['Total_Price'].mean():.2f}")

    st.subheader("Average Delivery Time by Traffic")
    st.bar_chart(df.groupby("Traffic_Level")[TARGET].mean())

elif page == "Data Analysis":
    st.header("Interactive Data Analysis")

    city = st.selectbox("City", ["All"] + sorted(df["City"].dropna().astype(str).unique()))
    traffic = st.selectbox(
        "Traffic Level",
        ["All"] + sorted(df["Traffic_Level"].dropna().astype(str).unique())
    )

    filtered = df.copy()
    if city != "All":
        filtered = filtered[filtered["City"] == city]
    if traffic != "All":
        filtered = filtered[filtered["Traffic_Level"] == traffic]

    st.write(f"Records displayed: {len(filtered):,}")
    st.subheader("Traffic vs Delivery Duration")
    st.bar_chart(filtered.groupby("Traffic_Level")[TARGET].mean())

    st.subheader("Vehicle vs Delivery Duration")
    st.bar_chart(filtered.groupby("Driver_Vehicle")[TARGET].mean())

    st.subheader("Orders by Hour")
    st.bar_chart(filtered.groupby("Order_Hour").size().reindex(range(24), fill_value=0))

elif page == "Delivery Time Prediction":
    st.header("🚚 Delivery Time Prediction")

    st.info(
        "Only the key operational parameters needed before delivery are requested. "
        "Customer IDs, restaurant IDs, coordinates, payment method and food item are "
        "not required in the prediction form."
    )

    col1, col2 = st.columns(2)

    with col1:
        distance = st.number_input(
            "Delivery Distance (km)",
            min_value=0.0,
            value=float(df["Delivery_Distance_km"].median()),
            step=0.1
        )
        traffic = st.selectbox(
            "Traffic Level",
            sorted(df["Traffic_Level"].dropna().astype(str).unique())
        )
        city = st.selectbox(
            "City",
            sorted(df["City"].dropna().astype(str).unique())
        )
        vehicle = st.selectbox(
            "Driver Vehicle",
            sorted(df["Driver_Vehicle"].dropna().astype(str).unique())
        )

    with col2:
        availability = st.selectbox(
            "Driver Availability",
            sorted(df["Driver_Availability"].dropna().astype(str).unique())
        )
        order_hour = st.slider("Order Hour", 0, 23, int(df["Order_Hour"].median()))
        weekend = st.selectbox("Weekend?", ["No", "Yes"])

    if st.button("Predict Delivery Time", type="primary"):
        input_df = pd.DataFrame([{
            "Delivery_Distance_km": distance,
            "Traffic_Level": traffic,
            "City": city,
            "Driver_Vehicle": vehicle,
            "Driver_Availability": availability,
            "Order_Hour": order_hour,
            "Is_Weekend": 1 if weekend == "Yes" else 0
        }])

        prediction = float(model.predict(input_df)[0])
        st.success(f"Predicted Delivery Time: {prediction:.2f} minutes")

elif page == "Business Insights":
    st.header("Business Insights")

    traffic = df.groupby("Traffic_Level")[TARGET].mean().sort_values(ascending=False)
    city = df.groupby("City")[TARGET].mean().sort_values(ascending=False)

    threshold = df[TARGET].quantile(0.90)
    long_orders = int((df[TARGET] >= threshold).sum())
    peak_hour = int(df.groupby("Order_Hour").size().idxmax())

    st.subheader("Data → Information → Insight → Decision → Action")
    st.write(
        f"Highest average delivery duration by traffic: "
        f"{traffic.index[0]} ({traffic.iloc[0]:.2f} min)."
    )
    st.write(
        f"Highest average delivery duration by city: "
        f"{city.index[0]} ({city.iloc[0]:.2f} min)."
    )
    st.write(
        f"Long-delivery risk: {long_orders:,} orders are at or above "
        f"the 90th-percentile threshold ({threshold:.2f} min)."
    )
    st.write(f"Peak order hour: {peak_hour}:00.")

