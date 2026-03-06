import streamlit as st

st.set_page_config(
    page_title="TaxiFare ML App",
    page_icon="🚕",
    layout="wide"
)

st.title("🚕 TaxiFare Prediction")

col1, col2 = st.columns([1,1])

with col1:

    st.markdown("""
### Welcome 👋

This application predicts the **taxi fare price in New York** using a machine learning model.

You can:

• Estimate a taxi ride price  
• Visualize the route on a map  
• Interact with a deployed ML API  

👉 Go to **Predict** in the sidebar to try it.
""")

with col2:

    st.image(
        "https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif",
        use_container_width=True
    )

st.divider()

st.caption("Machine Learning API • FastAPI • Docker • Cloud Run • Streamlit")