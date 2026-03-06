import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.metric_cards import style_metric_cards

st.title("📊 Model Monitoring")

st.markdown(
"""
Overview of the deployed TaxiFare prediction model.
"""
)

# METRICS
col1, col2, col3 = st.columns(3)

col1.metric("Model version", "v1.0")
col2.metric("API status", "Online")
col3.metric("Avg latency", "120 ms")
style_metric_cards()

st.divider()

# FAKE MONITORING DATA
np.random.seed(42)

data = pd.DataFrame({
    "predictions": np.random.normal(12, 3, 100)
})

st.subheader("Prediction distribution")

st.bar_chart(data)

st.subheader("Recent prediction activity")

events = pd.DataFrame({
    "event": [
        "API request received",
        "Features processed",
        "Model inference executed",
        "Prediction returned"
    ]
})

st.table(events)