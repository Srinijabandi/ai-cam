import streamlit as st
import requests

st.set_page_config(page_title="Weather UI 🌦️")

# 🔑 Your API Key
API_KEY = "YOUR_API_KEY_HERE"

# 🌄 Background
st.markdown("""
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1501973801540-537f08ccae7b");
    background-size: cover;
    background-position: center;
    color: white;
}

.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
}

.box {
    background: rgba(0,0,0,0.5);
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    width: 50%;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">🌦️ Weather App</p>', unsafe_allow_html=True)

st.markdown('<div class="box">', unsafe_allow_html=True)

# 🌆 City Dropdown
cities = ["Hyderabad", "Delhi", "Bangalore", "Chennai", "Kerala"]

selected_city = st.selectbox("Select City 📍", ["--Select--"] + cities)

# 🔍 Optional manual input
manual_city = st.text_input("Or Enter City 🌍")

# Function
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    return requests.get(url).json()

# Button
if st.button("Check Weather 🌡️"):
    
    # Priority: manual input > dropdown
    if manual_city:
        city = manual_city.strip().title()
    elif selected_city != "--Select--":
        city = selected_city
    else:
        st.warning("⚠️ Please select or enter a city")
        st.stop()

    data = get_weather(city)

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        st.success(f"Weather found for {city} ✅")
        st.markdown(f"### 🌤️ {condition.title()}")
        st.markdown(f"🌡️ Temperature: {temp}°C")
        st.markdown(f"💧 Humidity: {humidity}%")
        st.markdown(f"🌬️ Wind Speed: {wind} m/s")
    else:
        st.error("❌ Weather not found for this city")

st.markdown('</div>', unsafe_allow_html=True)