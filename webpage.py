import streamlit as st

st.title("🎓 Placement Management System")

# Student Details
st.header("Student Details")

name = st.text_input("Enter Student Name")
branch = st.selectbox("Select Branch", ["CSE", "ECE", "EEE", "MECH", "CIVIL"])
percentage = st.slider("Enter Percentage", 0, 100)
internship = st.radio("Internship Completed?", ["Yes", "No"])
skills = st.multiselect("Select Skills", ["Python", "Java", "C++", "SQL", "Web Development"])

# Eligibility Logic
st.header("Placement Eligibility")

eligible = False

if percentage >= 60 and internship == "Yes":
    eligible = True

# Display Results
if st.button("Check Eligibility"):

    st.subheader("📋 Student Summary")
    st.write("Name:", name)
    st.write("Branch:", branch)
    st.write("Percentage:", percentage)
    st.write("Internship:", internship)
    st.write("Skills:", skills)

    st.subheader("🎯 Result")

    if eligible:
        st.success("✅ Eligible for Placement")
    else:
        st.error("❌ Not Eligible for Placement")

    # Extra Insight
    st.subheader("📊 Suggestions")

    if percentage < 60:
        st.warning("Improve your percentage to at least 60%")

    if internship == "No":
        st.warning("Complete an internship to increase chances")

    if len(skills) < 2:
        st.info("Try to learn more technical skills")