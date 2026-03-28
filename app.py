import streamlit as st
import time

name = st.text_input("Enter your name:")
st.write("Hello", name)

age = st.number_input("Enter your age:", min_value=0, max_value=120)
st.write("Your age is:", age)

branch = st.selectbox("Select your branch:", ["Computer Science", "Mechanical", "Electrical", "Civil"])
st.write("Your branch is:", branch)

skills = st.multiselect("Select your skills:", ["Python", "Java", "C++", "JavaScript"])
st.write("Your skills are:", skills)

gender = st.radio("Gender", ["Male", "Female", "Other"])
st.write("Your gender is:", gender)

marks = st.slider("Enter your marks:", 0, 100)
st.write("Your marks are:", marks)

resume = st.file_uploader("Upload your resume:")

with st.spinner("Loading..."):
    time.sleep(2)
    st.success("Done!")

date = st.date_input("Select your date of birth:")
st.write("Date of birth:", date)

color = st.color_picker("Pick a color")
st.write("Selected color:", color)

dark_mode = st.toggle("Enable dark mode")
if dark_mode:
    st.write("Dark mode is enabled!")
else:
    st.write("Dark mode is disabled!")