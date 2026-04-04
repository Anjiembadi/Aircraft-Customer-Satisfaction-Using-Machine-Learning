import streamlit as st
import pandas as pd
import joblib

# Load saved pipeline
model = joblib.load("rf_pipeline.pkl")

st.title("Aircraft Customer Satisfaction Prediction")

# Input fields
online_boarding = st.selectbox("Online boarding", [0, 1, 2, 3, 4, 5])
wifi_service = st.selectbox("Inflight wifi service", [0, 1, 2, 3, 4, 5])
travel_class = st.selectbox("Class", ["Business", "Eco", "Eco Plus"])
travel_type = st.selectbox("Type of Travel", ["Business travel", "Personal Travel"])
entertainment = st.selectbox("Inflight entertainment", [0, 1, 2, 3, 4, 5])
seat_comfort = st.selectbox("Seat comfort", [0, 1, 2, 3, 4, 5])

if st.button("Predict Satisfaction"):
    input_df = pd.DataFrame([{
        "Online boarding": online_boarding,
        "Inflight wifi service": wifi_service,
        "Class": travel_class,
        "Type of Travel": travel_type,
        "Inflight entertainment": entertainment,
        "Seat comfort": seat_comfort
    }])

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.success("Passenger is Satisfied")
    else:
        st.error("Passenger is Not Satisfied")