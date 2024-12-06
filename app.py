import streamlit as st
import random

# Title of the app
st.title("Random Number Generator")

# Input for the maximum number
max_value = st.number_input("Enter the maximum number (greater than 1):", min_value=2, step=1)

# Button to generate a random number
if st.button("Generate Random Number"):
    # Generate a random number between 1 and the specified maximum value
    random_number = random.randint(1, max_value)
    st.write(f"Your random number is: **{random_number}**")
