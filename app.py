import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("aqi_model.pkl")
columns = joblib.load("columns.pkl")

st.set_page_config(page_title="AQI Prediction", layout="centered")

st.title("🌍 Air Quality Index Prediction")

st.write("Enter pollutant values below:")

pm25 = st.number_input("PM2.5", min_value=0.0)
pm10 = st.number_input("PM10", min_value=0.0)
no2 = st.number_input("NO2", min_value=0.0)
so2 = st.number_input("SO2", min_value=0.0)
co = st.number_input("CO", min_value=0.0)
o3 = st.number_input("O3", min_value=0.0)

# ADD THIS
city = st.selectbox(
    "Select City",
    ["Bengaluru","Chennai","Delhi","Hyderabad",
     "Jaipur","Kolkata","Lucknow","Mumbai","Pune"]
)

if st.button("Predict AQI"):

    input_df = pd.DataFrame(0, index=[0], columns=columns)

    input_df["pm2.5"] = pm25
    input_df["pm10"] = pm10
    input_df["no2"] = no2
    input_df["so2"] = so2
    input_df["co"] = co
    input_df["o3"] = o3

    city_col = f"city_{city}"
    if city_col in input_df.columns:
        input_df[city_col] = 1

    prediction = model.predict(input_df)[0]

    st.success(f"Predicted AQI: {round(prediction,2)}")