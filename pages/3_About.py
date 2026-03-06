import streamlit as st

st.title("ℹ️ About this project")

st.markdown(
"""
### TaxiFare Prediction

This application predicts the price of a taxi ride in New York using a machine learning model.

The model is deployed as an API on **Google Cloud Run**, and this interface is built with **Streamlit**.
"""
)

st.subheader("Architecture")

st.markdown(
"""
User  
⬇  
Streamlit frontend  
⬇  
API request  
⬇  
Google Cloud Run  
⬇  
Machine learning model  
⬇  
Prediction returned
"""
)

st.subheader("Tech stack")

st.write(
"""
- **Python**
- **Streamlit**
- **FastAPI**
- **Docker**
- **Google Cloud Run**
"""
)

st.subheader("Goal")

st.write(
"""
This project demonstrates how to deploy a machine learning model as an API and build a simple web interface to interact with it.
"""
)