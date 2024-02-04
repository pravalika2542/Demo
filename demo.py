import streamlit as st
st.set_page_config(page_title='bmi')        
st.title("Welcome to BMI Calculator")     

weight=st.number_input("Enter your weight(in kgs):")

height=st.radio("Select your height format:",('Cms','meters','feet'))
if(height==Cms):
  st.number_input("Centimeters:")
elif(height==meters):
  st.number_input("Meters:")
else:
  st.number_input("Feet:")
