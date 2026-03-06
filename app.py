import streamlit as st

st.set_page_config(
    page_title="TaxiFare AI",
    page_icon="🚕",
    layout="wide"
)

st.title("🚕 TaxiFare AI")

st.markdown(
"""
Welcome to the **TaxiFare prediction app**.

This application predicts the price of a New York taxi ride using a machine learning model deployed on **Google Cloud Run**.

Use the navigation menu on the left to explore the app.
"""
)