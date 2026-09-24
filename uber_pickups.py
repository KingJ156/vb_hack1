import streamlit as st 
import pandas as pd 
import numpy as np 
import requests
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

    if operation == "Add":
        answer = number1 + number2

    elif operation == "Subtract":
        answer = number1 - number2

    elif operation == "Multiply":
        answer = number1 * number2

    elif operation == "Divide":
        if number2 != 0:
            answer = number1 / number2
        else:
            answer = "Cannot divide by zero."

    st.write("Answer:", answer)

BASE_URL = "https://pokeapi.co/api/v2/pokemon"


def fetch_pokemon(name_or_id: str, timeout: float = 6) -> dict:
    """Raise requests.HTTPError if the name/id doesn't exist (404) or on network errors."""
    r = requests.get(f"{BASE_URL}/{str(name_or_id).strip().lower()}", timeout=timeout)
    r.raise_for_status()
    return r.json()