import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("churn_model.pkl")

st.set_page_config(page_title="USSD Customer Churn Prediction", layout="wide")

st.title("📱 USSD Customer Churn Prediction App")
st.write("This app predicts whether a USSD customer is likely to **stop using the service (churn)**.")

# Sidebar inputs
st.sidebar.header("Enter Customer Details")

age = st.sidebar.slider("Age", 18, 70, 30)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
location = st.sidebar.selectbox("Location", ["Urban", "Rural"])
account_type = st.sidebar.selectbox("Account Type", ["Savings", "Current", "Mobile Wallet"])
transactions_last_30d = st.sidebar.slider("Transactions (Last 30 Days)", 0, 100, 15)
avg_transaction_value = st.sidebar.number_input("Average Transaction Value (₦)", min_value=50.0, max_value=10000.0, value=2000.0)
failed_transactions = st.sidebar.slider("Failed Transactions", 0, 20, 2)
sms_alerts = st.sidebar.selectbox("SMS Alerts", ["Yes", "No"])
complaints_logged = st.sidebar.slider("Complaints Logged", 0, 10, 1)
customer_tenure_months = st.sidebar.slider("Customer Tenure (Months)", 1, 60, 12)

# Create dataframe for model input
input_data = pd.DataFrame({
    "age": [age],
    "gender": [1 if gender == "Male" else 0],
    "location": [1 if location == "Urban" else 0],
    "account_type": [0 if account_type == "Current" else (1 if account_type == "Mobile Wallet" else 2)],
    "transactions_last_30d": [transactions_last_30d],
    "avg_transaction_value": [avg_transaction_value],
    "failed_transactions": [failed_transactions],
    "sms_alerts": [1 if sms_alerts == "Yes" else 0],
    "complaints_logged": [complaints_logged],
    "customer_tenure_months": [customer_tenure_months]
})

st.subheader("Customer Input Data")
st.write(input_data)

# Prediction
if st.button("🔮 Predict Churn"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Customer is likely to **CHURN** (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Customer is likely to **STAY** (Probability: {1 - probability:.2f})")
