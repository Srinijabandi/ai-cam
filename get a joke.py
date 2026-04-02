import streamlit as st
import requests
st.title("JOKE APP")
if st.button("Get a joke"):
    url="https://official-joke-api.appspot.com/random_joke"
    response=requests.get(url)
    data=response.json()
    st.write(data["setup"])
    st.write(data["punchline"])