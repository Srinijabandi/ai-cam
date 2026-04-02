import streamlit as st
import pandas as pd

st.title("Risk Analysis in User Testing")

st.write("Enter risk details and evaluate their priority")

# Input fields
risk_name = st.text_input("Risk Name")
category = st.selectbox("Category", ["User", "Technical", "Data", "Ethical", "Resource"])
likelihood = st.slider("Likelihood (1-5)", 1, 5)
impact = st.slider("Impact (1-5)", 1, 5)

# Calculate Risk Score
risk_score = likelihood * impact

# Determine Priority
if risk_score >= 15:
    priority = "High"
elif risk_score >= 8:
    priority = "Medium"
else:
    priority = "Low"

# Store data
if "data" not in st.session_state:
    st.session_state.data = []

# Add Risk
if st.button("Add Risk"):
    if risk_name:
        st.session_state.data.append({
            "Risk Name": risk_name,
            "Category": category,
            "Likelihood": likelihood,
            "Impact": impact,
            "Risk Score": risk_score,
            "Priority": priority
        })
        st.success("Risk Added Successfully!")
    else:
        st.warning("Please enter a risk name")

# Display Table
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.subheader("Risk Analysis Table")
    st.dataframe(df)

    # Summary
    st.subheader("Summary")
    st.write("Total Risks:", len(df))
    st.write("High Priority:", len(df[df["Priority"] == "High"]))
    st.write("Medium Priority:", len(df[df["Priority"] == "Medium"]))
    st.write("Low Priority:", len(df[df["Priority"] == "Low"]))