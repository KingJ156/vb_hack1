import streamlit as st 
import pandas as pd 
import numpy as np 
st.title('Uber pickups in NYC')

st.title('Hello World')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')

number = st.number_input("Insert a number")
st.write("The current number is ", number)