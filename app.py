import streamlit as st

# Title of the app
st.title("Square Calculator")

# Input field for the user
number = st.number_input("Enter a number", value=1)

# Display the square of the number
st.write(f"The square of {number} is {number**2}")
