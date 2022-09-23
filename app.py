import streamlit as st
import joblib
import sklearn


model = joblib.load('Weight.lr')
labelize = joblib.load('labelized.le')

# Title for app
st.title('Human Weight Predictor')
sex = st.radio(label="Select Gender", options=("Male", "Female"))
height = st.text_input(label='Enter Height', placeholder=" e.g (5.3)")

if not st.button('Predict'):
    pass
else:
    # 1. Labelized
    sex = labelize.transform([sex])

    # 2. Scale and Predict
    result = model.predict([[sex, height]])[0]

    # 3. Display
    st.subheader(f"Predicted Weight is {round(result,2)} kg")
