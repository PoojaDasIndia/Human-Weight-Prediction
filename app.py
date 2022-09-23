import streamlit as st
import joblib

model = joblib.load('Weight.lr')
labelize = joblib.load('labelized.le')

# Title for app
st.title('Human Weight Predictor')
sex = st.radio(label="Sex", options=("Male","Female"))
height = st.text_area(label='Height', placeholder="Enter Height in feet e.g (5.3)")

if not st.button('Predict'):
    pass
else:
    # 1. Labelized
    text = labelize(sex)

    # 2. Scale and Predict
    result = model.predict([[sex,height]])[0]

    # 3. Display
    if result == 0:
        st.header('Not Spam')
    else:
        st.header('Spam')

