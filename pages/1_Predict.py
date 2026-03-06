import streamlit as st
import requests
import pandas as pd
import pydeck as pdk

st.title("🚕 TaxiFare Prediction")
st.markdown("""
<style>

.predict-card {
    background-color:#ffffff;
    padding:25px;
    border-radius:12px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    text-align:center;
}

.price {
    font-size:42px;
    font-weight:700;
    color:#00a67e;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
"""
Estimate the price of a New York taxi ride using our deployed ML model.
"""
)

# API
url = "https://taxifare-57400065525.europe-west1.run.app/predict"

# SIDEBAR
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

# MAP
map_data = pd.DataFrame({
    "lat": [pickup_latitude, dropoff_latitude],
    "lon": [pickup_longitude, dropoff_longitude]
})

st.subheader("Ride map")
#st.map(map_data)
path_data = [
    {
        "path": [
            [pickup_longitude, pickup_latitude],
            [dropoff_longitude, dropoff_latitude],
        ]
    }
]

layer = pdk.Layer(
    "PathLayer",
    data=path_data,
    get_path="path",
    get_width=5,
    get_color=[0, 160, 120],
)

view_state = pdk.ViewState(
    latitude=(pickup_latitude + dropoff_latitude) / 2,
    longitude=(pickup_longitude + dropoff_longitude) / 2,
    zoom=11,
)

st.pydeck_chart(
    pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
    )
)

# PARAMETERS
params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

# PREDICT
if st.button("Predict fare"):

    with st.spinner("Running model inference..."):

        response = requests.get(url, params=params)

    if response.status_code == 200:

        prediction = response.json()["fare"]

        st.markdown(
        f"""
        <div class="predict-card">

        ### Estimated Fare

        <div class="price">
        ${prediction:.2f}
        </div>

        </div>
        """,
        unsafe_allow_html=True
        )

    else:

        st.error("API error")