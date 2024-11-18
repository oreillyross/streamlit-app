import streamlit as st

st.title("Simple streamlit app")

name = st.text_input("Enter your name?")

age = st.slider("Enter your age?", 0, 100)

if st.button("Submit"):
  st.write(f"Hello, {name}, you are {age} years old!")