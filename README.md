# Invoice Intelligence System

## Overview

Invoice Intelligence System is a Machine Learning powered application that helps businesses analyze vendor invoices through two predictive modules:

1. **Freight Cost Prediction**
2. **Invoice Risk Assessment**

The system enables organizations to estimate freight expenses and identify potentially risky invoices before processing.

---

## Features

### Freight Cost Prediction

Predicts the expected freight cost based on:

* Quantity
* Total Invoice Value (Dollars)
* Average Purchase Price
* Number of Products
* Number of Brands

**Best Model:** Linear Regression

Performance:

* R² Score: 0.9704
* MAE: 25.11
* RMSE: 123.60

---

### Invoice Risk Prediction

Classifies invoices as:

* Low Risk
* High Risk

Features used:

* PO Number
* Quantity
* Invoice Value
* Freight Amount
* Average Purchase Price
* Number of Products
* Number of Brands
* Invoice Month
* PO Month
* Payment Month

**Best Model:** XGBoost Classifier

Performance:

* Accuracy: 77%
* Risk Class F1 Score: 0.33

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Streamlit
* Pickle

---

## Project Structure

├── app.py

├── freight_model.pkl

├── freight_model_preprocessing.pkl

├── risk_model.pkl

├── risk_model_preprocessing.pkl

├── requirements.txt

└── README.md

---

## Installation

Clone the repository:

```bash
git clone <repository-link>
cd invoice-intelligence-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Business Value

This solution helps organizations:

* Estimate freight expenses accurately
* Monitor invoice payment patterns
* Detect potentially risky invoices
* Improve operational decision making
* Reduce manual verification efforts

---

## Future Enhancements

* Real-time dashboard analytics
* Automated invoice upload
* Vendor risk profiling
* Advanced anomaly detection
* Interactive reporting and visualization

---

## Author

Aaditya Hole

B.Tech Computer Engineering

Data Science & Machine Learning Enthusiast
