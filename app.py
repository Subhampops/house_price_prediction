import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load saved model
with open("housing_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🏠 Housing Price Prediction App")

# User input fields
def user_input():
    area = st.number_input("Area (sqft)", 500, 10000, 2000)
    bedrooms = st.slider("Bedrooms", 1, 10, 3)
    bathrooms = st.slider("Bathrooms", 1, 5, 2)
    stories = st.slider("Stories", 1, 5, 2)
    mainroad = st.selectbox("Mainroad (Yes=1, No=0)", [0,1])
    guestroom = st.selectbox("Guestroom (Yes=1, No=0)", [0,1])
    basement = st.selectbox("Basement (Yes=1, No=0)", [0,1])
    hotwaterheating = st.selectbox("Hot Water Heating (Yes=1, No=0)", [0,1])
    airconditioning = st.selectbox("Air Conditioning (Yes=1, No=0)", [0,1])
    parking = st.slider("Parking Spaces", 0, 5, 1)
    prefarea = st.selectbox("Preferred Area (Yes=1, No=0)", [0,1])
    furnishingstatus = st.selectbox("Furnishing Status (Unfurnished=0, Semi-furnished=1, Furnished=2)", [0,1,2])
    
    data = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "stories": stories,
        "mainroad": mainroad,
        "guestroom": guestroom,
        "basement": basement,
        "hotwaterheating": hotwaterheating,
        "airconditioning": airconditioning,
        "parking": parking,
        "prefarea": prefarea,
        "furnishingstatus": furnishingstatus
    }
    
    return pd.DataFrame([data])

input_df = user_input()

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_df)
    st.success(f"🏡 Estimated Price: ₹ {prediction[0]:,.2f}")
