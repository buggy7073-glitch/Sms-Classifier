import streamlit as st
import pandas as pd

st.title("This is a Title")


col1,col2,col3 = st.columns(3)
with col1:
    name = st.text_input(" Name")
with col2:
    age = st.number_input("Enter a age ")
with col3:
    slide = st.slider("Wicket",0,10)

if st.button("Click me"):
    pass
gender_list = ["male","Female","other"]
st.selectbox("select gender",sorted(gender_list))

nre = st.text("new langauage")
if st.checkbox("multiple check you can do "):
    st.write("good moring")

age = st.slider("slide and give number",0,100)

st.sidebar.title("good moringh")
st.radio("i am radio",["you","we","us"])

optin = st.sidebar.radio("radio tune ",[23,45,56,"name"])

col5,co7,col9 = st.sidebar.columns(3)

with col5:
    st.slider("slide you want",0,80,30)
with co7:
    st.sidebar.text_input("name you want")
with col9:
    inp = st.number_input("entr a number")