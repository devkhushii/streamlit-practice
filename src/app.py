import streamlit as st
import pandas as pd 
import numpy as np 
import time as t 

st.title("WELCOME TO MY DEMO APP")
st.write("In this some methods of streamlit is used")
st.header("This is heading")

st.subheader("This is sub heading")

st.info("This is Information")

st.warning("This is a warning")

st.error("This is an error")

st.write("This is write function")

st.success("this is success message")

st.markdown("# This is markdown")

st.text("this is text")

st.markdown(":moon:")

st.caption("it's a caption")

st.latex(r''' a+b x^2+c''')

st.checkbox('login')

st.button("click")

st.radio("pick your hgender",["male","female"])

st.selectbox("select course",["BTECH","BCA","POLY"])

st.multiselect("select multiple choices",["java","python","cpp","javascript"])

st.select_slider("Rating",["bad","good","excellent"])

st.slider("enter ur number",0,100)

st.number_input("choose a number",0,30)

st.text_input("enter some text")

st.date_input("select date")

st.time_input("choose time")

st.text_area("enter some text, this is text area")

st.file_uploader("upload your file/folder")

st.color_picker("color")

st.progress(90)

with st.spinner("just wait"):
    t.sleep(3)
    
st.balloons()

st.sidebar.title("this is side bar")

st.title("bar chart")
data=pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.bar_chart(data)

