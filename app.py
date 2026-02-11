import streamlit as st
import pickle
import numpy as np

# Load model and encoders
model = pickle.load(open("model.pkl", "rb"))
le_brand = pickle.load(open("le_brand.pkl", "rb"))
le_series = pickle.load(open("le_series.pkl", "rb"))
le_processor = pickle.load(open("le_processor.pkl", "rb"))

st.title("📱 Smart Phone Price Prediction")

brand = st.selectbox("Brand", le_brand.classes_)
series = st.selectbox("Series", le_series.classes_)
ram = st.number_input("RAM (GB)", min_value=1)
storage = st.number_input("Storage (GB)", min_value=8)
camera = st.number_input("Camera (MP)", min_value=1)
battery = st.number_input("Battery (mAh)", min_value=1000)
display = st.number_input("Screen Size (inches)", min_value=4.0)
processor = st.selectbox("Processor", le_processor.classes_)
is_5g = st.selectbox("5G Support", ["Yes", "No"])

if st.button("Predict Price"):

    brand_encoded = le_brand.transform([brand])[0]
    series_encoded = le_series.transform([series])[0]
    processor_encoded = le_processor.transform([processor])[0]
    is_5g_encoded = 1 if is_5g.lower() == "yes" else 0


    import pandas as pd

    input_data = pd.DataFrame([[ 
        brand_encoded,
        series_encoded,
        ram,
        storage,
        camera,
        battery,
        display,
        processor_encoded,
        is_5g_encoded
    ]], columns=[
        'Brand','Series','RAM_GB','Storage_GB',
        'Camera_MP','Battery_mAh',
        'Screen_Size','Processor','5G'
    ])

    prediction = model.predict(input_data)

    st.success(f"Estimated Price: ₹ {int(prediction[0])}")

