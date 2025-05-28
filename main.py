import streamlit as st
import os
import pandas as pd
st.write({"key":"Value"})
st.write("Hello World")
3+4
pressed = st.button("press me")
print(pressed)
st.title("Stream lit workproject")
st.header("Py workbook")
st.subheader("Subheader")
st.markdown("_Markdown_")
st.caption("Small texts")
code_ex = """ 
def greet(name):
    print("Welcome", name)
"""
st.code(code_ex, language="python")
st.image(os.path.join(os.getcwd(),"static","lz.jpg"))
st.divider()
st.title("Streamlit Interface")

text_input = st.text_input("Enter text:")

number_input = st.number_input("Enter a number:", value=0)

checkbox = st.checkbox("Show additional input")

if checkbox:
    conditional_text_input = st.text_input("Enter additional text:")

options = ["Option 1", "Option 2", "Option 3"]
selected_option = st.selectbox("Select an option:", options)

date_input = st.date_input("Select a date:")

st.write("You entered:")
st.write(f"Text: {text_input}")
st.write(f"Number: {number_input}")
if checkbox:
    st.write(f"Additional Text: {conditional_text_input}")
st.write(f"Selected Option: {selected_option}")
st.write(f"Date: {date_input}")
