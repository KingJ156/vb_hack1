import streamlit as st 
import pandas as pd 
import numpy as np 
st.title('Uber pickups in NYC')

st.title('Hello World')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')

number1 = st.number_input(
    "Enter the first number", value=None, placeholder="Type a number..."
)

number2 = st.number_input(
    "Enter the second number", value=None, placeholder="Type a number..."
)

if number1 is not None and number2 is not None:
    total = number1 + number2
    st.write("The answer is", total)