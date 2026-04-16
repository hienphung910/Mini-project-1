import streamlit as st

w = 10052.79
b = 22655.57
st.title("Salary Predictor")

years = st.slider("Years of Experience", 0.0, 10.0, step = 0.1)
salary = w * years + b

st.write(f"Predicted Salary: {salary}")