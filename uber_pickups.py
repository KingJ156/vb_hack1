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

operation = st.selectbox(
    "Choose an operation",
    ["Add", "Subtract", "Multiply", "Divide"]
)

if number1 is not None and number2 is not None:

    if st.button("Add"):
        st.write("Answer:", number1 + number2)

    if st.button("Subtract"):
        st.write("Answer:", number1 - number2)

    if st.button("Multiply"):
        st.write("Answer:", number1 * number2)

    if st.button("Divide"):
        if number2 != 0:
            st.write("Answer:", number1 / number2)
        else:
            st.write("Cannot divide by zero.")