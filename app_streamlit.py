# app_streamlit.py
import streamlit as st
import requests
import json

st.set_page_config(page_title="Bank Churn Prediction API", layout="centered")

st.title("🏦 Bank Churn Prediction API Interface")
st.write("This interface allows you to test the Bank Churn Prediction API deployed on Azure.")

# Input fields
credit_score = st.number_input("Credit Score", min_value=0, max_value=1000, value=650)
age = st.number_input("Age", min_value=18, max_value=100, value=40)
tenure = st.number_input("Tenure (years)", min_value=0, max_value=50, value=5)
balance = st.number_input("Balance", min_value=0, value=60000)
num_products = st.number_input("Number of Products", min_value=1, max_value=10, value=2)
has_cr_card = st.selectbox("Has Credit Card?", ["Yes", "No"])
is_active_member = st.selectbox("Is Active Member?", ["Yes", "No"])
estimated_salary = st.number_input("Estimated Salary", min_value=0, value=50000)
geography_germany = st.selectbox("Geography Germany?", ["Yes", "No"])
geography_spain = st.selectbox("Geography Spain?", ["Yes", "No"])

# Convert Yes/No to 1/0
has_cr_card = 1 if has_cr_card == "Yes" else 0
is_active_member = 1 if is_active_member == "Yes" else 0
geography_germany = 1 if geography_germany == "Yes" else 0
geography_spain = 1 if geography_spain == "Yes" else 0


# Prediction button
if st.button("Predict Churn"):
    payload = {
        "CreditScore": credit_score,
        "Age": age,
        "Tenure": tenure,
        "Balance": balance,
        "NumOfProducts": num_products,
        "HasCrCard": has_cr_card,
        "IsActiveMember": is_active_member,
        "EstimatedSalary": estimated_salary,
        "Geography_Germany": geography_germany,
        "Geography_Spain": geography_spain
    }

    url = "https://bank-churn-api.victoriousmoss-65485a03.francecentral.azurecontainerapps.io/predict"

    try:
        response = requests.post(url, json=payload)
        result = response.json()
        st.subheader("Prediction Result")
        st.json(result)
    except Exception as e:
        st.error(f"Error calling API: {e}")
