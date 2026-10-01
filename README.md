# SecurePay - Credit Card Fraud Detection

SecurePay is a machine learning application that detects potential credit card fraud using a trained LightGBM model. A Streamlit interface allows users to enter transaction details and receive a fraud probability and risk assessment.

## Features

- Credit card fraud detection
- LightGBM classification model
- Fraud probability prediction
- Configurable decision threshold
- Streamlit web interface
- Saved model using Joblib

## Features Used

- `distance_from_home`
- `distance_from_last_transaction`
- `ratio_to_median_purchase_price`
- `repeat_retailer`
- `used_chip`
- `used_pin_number`
- `online_order`

## Project Structure

```text
Credit Card Fraud Detection/
├── app.py
├── card_transdata.csv
├── requirements.txt
├── README.md
└── model/
    ├── fraud_model.pkl
    └── model_config.pkl

Installation
python -m venv .venv

Windows:
.venv\Scripts\Activate.ps1

Install dependencies:
python -m pip install -r requirements.txt

Run
python -m streamlit run app.py

The application will open at:
http://localhost:8501

Technology Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- LightGBM
- Joblib
- Streamlit
Model
The trained model is stored in model/fraud_model.pkl, while the prediction threshold and feature order are stored in model/model_config.pkl.
The application loads these files and predicts the probability of fraud for each transaction.
Note
This project is intended for educational and demonstration purposes. A model prediction represents a risk assessment and should not be treated as definitive proof of fraud.
```