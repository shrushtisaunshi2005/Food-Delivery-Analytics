[Uploading README (2).md…]()
# AI-Based Food Delivery Time Prediction and Operational Analytics

## Project Overview

This project is an academic **Data Analytics with AI** project that analyzes food-delivery data and predicts delivery duration using machine learning.

The project follows an end-to-end workflow:

**Data Loading → Data Cleaning → Exploratory Data Analysis → Feature Engineering → Machine Learning → Model Evaluation → Business Analytics → Streamlit Prediction UI**

The objective is to identify important operational factors affecting delivery time and provide a simple AI-based system for estimating delivery duration.

---

## Problem Statement

Food-delivery platforms need to manage delivery distance, traffic conditions, driver availability, vehicle type and ordering time. These factors can influence how long an order takes to reach the customer.

This project uses historical food-delivery data to:

- Clean and validate the data.
- Discover important delivery patterns.
- Analyze operational factors affecting delivery duration.
- Build regression models for delivery-time prediction.
- Provide business-oriented insights.
- Demonstrate prediction through a Streamlit web interface.

---

## Objectives

1. Inspect and understand the food-delivery dataset.
2. Perform systematic data cleaning and validation.
3. Conduct exploratory data analysis using meaningful visualizations.
4. Create time-based features from order timestamps.
5. Predict `Delivery_Duration_Minutes`.
6. Compare multiple machine-learning regression models.
7. Evaluate models using MAE, RMSE and R².
8. Generate KPIs, trends, drivers and risk indicators.
9. Provide an interactive Streamlit prediction interface.

---

## Dataset

**Dataset:** `Order_delivery.csv`

The dataset contains food-delivery order records with information related to orders, restaurants, drivers, traffic, delivery distance, vehicle type, geographical information and timestamps.

Important fields used for analysis include:

- `Delivery_Duration_Minutes`
- `Delivery_Distance_km`
- `Traffic_Level`
- `City`
- `Driver_Vehicle`
- `Driver_Availability`
- `Order_Time`
- `Delivery_Time`
- `Total_Price`
- `Quantity`

The original CSV is not modified. Data cleaning is performed on a separate copy inside the notebook.

---

## Data Cleaning

The project performs the following data-quality checks:

- Missing-value analysis
- Duplicate-record detection and removal
- Data-type correction
- Datetime conversion
- Text/categorical standardization
- Invalid quantity validation
- Invalid price validation
- Invalid delivery-duration validation
- Invalid delivery-distance validation
- Latitude and longitude validation

The notebook displays the cleaning results so the process is reproducible.

---

## Exploratory Data Analysis

The project analyzes:

- Delivery-duration distribution
- Orders by city
- Orders by food item
- Orders by traffic level
- Driver vehicle distribution
- Driver availability
- Delivery distance vs delivery duration
- Traffic level vs delivery duration
- City vs average delivery duration
- Vehicle type vs average delivery duration
- Peak ordering hours

The analysis follows a decision-oriented structure:

**KPIs → Trends → Drivers → Risk → Action**

---

## Feature Engineering

The following features are created from `Order_Time`:

- Order Hour
- Day of Week
- Month
- Weekend Indicator
- Peak-Hour Indicator

These features help the model understand time-related delivery patterns.

---

## Machine Learning

### Target Variable

```text
Delivery_Duration_Minutes
```

### Prediction Features

The final prediction model uses only the most relevant operational parameters:

```text
Delivery_Distance_km
Traffic_Level
City
Driver_Vehicle
Driver_Availability
Order_Hour
Is_Weekend
```

These parameters are selected because they represent information that can reasonably be available before delivery completion.

### Models

The project compares:

1. Linear Regression
2. Random Forest Regressor
3. Gradient Boosting Regressor

### Evaluation Metrics

Models are evaluated using:

- **MAE** – Mean Absolute Error
- **RMSE** – Root Mean Squared Error
- **R²** – Coefficient of Determination

The notebook calculates the actual results from the supplied dataset. No model performance values are manually assumed.

---

## Data Leakage Prevention

The following information is not used as a prediction input:

- `Delivery_Time` because it is available after delivery and can cause target leakage.
- Order, user, restaurant and driver IDs because they are identifiers rather than meaningful operational measurements.

The prediction interface also does not request unnecessary identifiers, coordinates or post-delivery information.

---

## Business Analytics

The project calculates meaningful KPIs including:

- Total Orders
- Average Delivery Time
- Average Delivery Distance
- Average Order Value
- Long Delivery Orders
- Peak Ordering Hour

The project follows:

**Data → Information → Insight → Decision → Action**

Example operational areas include:

- Monitoring high-traffic periods.
- Identifying longer-distance deliveries.
- Reviewing city-level delivery performance.
- Monitoring peak ordering periods.
- Supporting operational planning using predicted delivery duration.

---

## Streamlit User Interface

The project includes a professional Streamlit application with four sections.

### 1. Overview

Displays:

- Total orders
- Average delivery time
- Average delivery distance
- Average order value
- Traffic-related delivery analysis

### 2. Data Analysis

Provides interactive analysis using filters such as:

- City
- Traffic Level

It displays:

- Traffic vs delivery duration
- Vehicle vs delivery duration
- Orders by hour

### 3. Delivery Time Prediction

The user enters only the important prediction parameters:

- Delivery Distance
- Traffic Level
- City
- Driver Vehicle
- Driver Availability
- Order Hour
- Weekend status

After clicking **Predict Delivery Time**, the application displays the estimated delivery duration in minutes.

### 4. Business Insights

Displays data-driven findings related to:

- Traffic
- City
- Long-delivery risk
- Peak ordering periods

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Jupyter Notebook
- VS Code

---

## Project Structure

```text
Food Delivery/
│
├── Food_Delivery_Analytics_Complete.ipynb
├── Order_delivery.csv
├── requirements.txt
├── README.md
├── app.py
└── Food_Delivery_Analytics_Professional_Report.docx
```

`app.py` is generated from the Streamlit section of the notebook.

---

## Installation

Open the project folder in VS Code and open the terminal.

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## Run the Jupyter Notebook

Open:

```text
Food_Delivery_Analytics_Complete.ipynb
```

Select a Python kernel and run the notebook cells.

Make sure:

```text
Order_delivery.csv
```

is in the same folder as the notebook.

---

## Run the Streamlit Application

After the notebook has generated `app.py`, run:

```bash
streamlit run app.py
```

The Streamlit application will open in the browser.

---

## Reproducibility

The project does not hard-code analytical results or model performance values.

All:

- Cleaning statistics
- EDA results
- KPIs
- Model metrics
- Prediction results
- Business insights

are generated from the actual `Order_delivery.csv` dataset when the project is executed.

---

## Internship Deliverables

The main submission files are:

1. `Food_Delivery_Analytics_Complete.ipynb`
2. `requirements.txt`
3. `README.md`
4. Project Report `.docx`

The Streamlit `app.py` can be included as an additional project demonstration file.

---

## Conclusion

This project demonstrates how data analytics and artificial intelligence can be combined to analyze food-delivery operations and predict delivery duration.

The complete workflow connects **data cleaning, analytics, machine learning and business decision-making** in a single project, making it suitable for an academic Data Analytics with AI internship.

---

## Author

**Academic Internship Project – Data Analytics with AI**

