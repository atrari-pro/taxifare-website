import streamlit as st
import requests
from datetime import datetime

st.title("TaxiFare Prediction")

st.markdown("Enter ride parameters to estimate the taxi fare.")

pickup_datetime = st.text_input("Pickup datetime", "2014-07-06 19:18:00")
pickup_longitude = st.number_input("Pickup longitude", value=-73.950655)
pickup_latitude = st.number_input("Pickup latitude", value=40.783282)
dropoff_longitude = st.number_input("Dropoff longitude", value=-73.984365)
dropoff_latitude = st.number_input("Dropoff latitude", value=40.769802)
passenger_count = st.number_input("Passenger count", value=2)

url = "https://taxifare-57400065525.europe-west1.run.app/predict"

params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

if st.button("Predict fare"):
    response = requests.get(url, params=params)
    prediction = response.json().get("fare")

    st.success(f"Estimated fare: ${prediction:.2f}")