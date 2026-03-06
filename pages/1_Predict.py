import streamlit as st
import requests
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="TaxiFare Prediction", page_icon="🚕", layout="wide")

st.title("🚕 TaxiFare Prediction")

st.markdown(
"""
Estimate the price of a **New York taxi ride** using our deployed **Machine Learning model**.
"""
)

# ---------------------------
# STYLE
# ---------------------------

st.markdown("""
<style>

.predict-card {
    background-color:#ffffff;
    padding:30px;
    border-radius:14px;
    box-shadow:0 6px 18px rgba(0,0,0,0.08);
    text-align:center;
    margin-top:20px;
}

.price {
    font-size:46px;
    font-weight:700;
    color:#00a67e;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------
# API
# ---------------------------

url = "https://taxifare-57400065525.europe-west1.run.app/predict"


# ---------------------------
# SIDEBAR INPUTS
# ---------------------------

st.sidebar.header("Ride parameters")

pickup_datetime = st.sidebar.text_input(
    "Pickup datetime",
    "2014-07-06 19:18:00"
)

pickup_latitude = st.sidebar.number_input(
    "Pickup latitude",
    value=40.783282
)

pickup_longitude = st.sidebar.number_input(
    "Pickup longitude",
    value=-73.950655
)

dropoff_latitude = st.sidebar.number_input(
    "Dropoff latitude",
    value=40.769802
)

dropoff_longitude = st.sidebar.number_input(
    "Dropoff longitude",
    value=-73.984365
)

passenger_count = st.sidebar.slider(
    "Passengers",
    1, 8, 2
)


# ---------------------------
# MAIN LAYOUT
# ---------------------------

col1, col2 = st.columns([1,1])


# ---------------------------
# MAP
# ---------------------------

with col2:

    st.subheader("Ride Map")

    path_data = [{
        "path": [
            [pickup_longitude, pickup_latitude],
            [dropoff_longitude, dropoff_latitude]
        ]
    }]

    path_layer = pdk.Layer(
        "PathLayer",
        data=path_data,
        get_path="path",
        get_width=5,
        get_color=[0,160,120],
    )

    points = pd.DataFrame({
        "lat":[pickup_latitude, dropoff_latitude],
        "lon":[pickup_longitude, dropoff_longitude]
    })

    point_layer = pdk.Layer(
        "ScatterplotLayer",
        data=points,
        get_position='[lon, lat]',
        get_radius=120,
        get_color=[255,0,0],
    )

    view_state = pdk.ViewState(
        latitude=(pickup_latitude + dropoff_latitude)/2,
        longitude=(pickup_longitude + dropoff_longitude)/2,
        zoom=11,
    )

    st.pydeck_chart(
        pdk.Deck(
            layers=[path_layer, point_layer],
            initial_view_state=view_state,
        )
    )


# ---------------------------
# PARAMETERS + PREDICTION
# ---------------------------

with col1:

    st.subheader("Ride Information")

    st.write("Pickup:", pickup_latitude, pickup_longitude)
    st.write("Dropoff:", dropoff_latitude, dropoff_longitude)
    st.write("Passengers:", passenger_count)

    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    predict = st.button("🚕 Predict Fare", use_container_width=True)

    if predict:

        with st.spinner("Running model inference..."):

            try:

                response = requests.get(url, params=params)

                if response.status_code == 200:

                    prediction = response.json()["fare"]

                    st.markdown(
                    f"""
                    <div class="predict-card">

                    <h3>Estimated Fare</h3>

                    <div class="price">
                    ${prediction:.2f}
                    </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                    )

                else:

                    st.error("API returned an error.")

            except:

                st.error("Cannot reach prediction API.")