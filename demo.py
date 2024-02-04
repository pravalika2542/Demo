import streamlit as st
st.set_page_config(page_title='bmi')        
st.title("Welcome to BMI Calculator")     

weight=st.number_input("Enter your weight(in kgs):")

x=st.radio("Select your height format:",('Cms','meters','feet'))
if(x=='Cms'):
  height=st.number_input("Centimeters:")
elif(x=='meters'):
  height=st.number_input("Meters:")
else:
  height=st.number_input("Feet:")
