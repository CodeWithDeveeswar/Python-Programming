# Streamlit is a Python library to create web apps for data projects — without needing HTML, CSS, or JavaScript.
# It turns your Python scripts into interactive web apps just by running a script.

# Terminal command: python -m streamlit run Streamlit/webapp.py

# webapp.py
import streamlit as st

st.title("📊 My First Streamlit App")
st.header("Welcome to the Demo App")
st.write("This is a simple app built with Streamlit!")

# Interactive element
name = st.text_input("What's your name?")
if name:
    st.success(f"Hello, {name}! 👋")

# Slider example
age = st.slider("Select your age", 1, 100, 25)
st.write("You selected:", age)