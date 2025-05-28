import streamlit as st
import os
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
st.divider()

st.image(os.path.join(os.getcwd(),"static","lz.jpg"))