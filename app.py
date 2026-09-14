from dotenv import load_dotenv
import os
load_dotenv()
import streamlit as st
import requests
import json

st.title("Customer Churn Predictor")
st.write("Enter customer details to predict churn likelihood.")

url = os.getenv("AZURE_ENDPOINT_URL")
api_key = os.getenv("AZURE_API_KEY")

tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.number_input("Monthly Charges ($)", 0.0, 200.0, 70.0)
total_charges = st.number_input("Total Charges ($)", 0.0, 10000.0, 1000.0)
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
senior = st.selectbox("Senior Citizen", ["No", "Yes"])

if st.button("Predict Churn"):
    contract_one_year = 1 if contract == "One year" else 0
    contract_two_year = 1 if contract == "Two year" else 0
    internet_fiber = 1 if internet == "Fiber optic" else 0
    internet_no = 1 if internet == "No" else 0
    senior_val = 1 if senior == "Yes" else 0

    row = [senior_val, tenure] + [0]*15 + [contract_one_year, contract_two_year] + [0]*2 + [internet_fiber, internet_no] + [0]*4 + [monthly_charges, total_charges] + [0]*4

    data = {"data": [row[:30]]}

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        result = json.loads(response.text)[0]
        if result == 1:
            st.error("⚠️ This customer is likely to churn")
        else:
            st.success("✅ This customer is likely to stay")
    else:
        st.error(f"Error: {response.text}")