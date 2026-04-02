import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Title
st.title("📊 Sales Performance Dashboard")

# Data
data = {
    "Region": ["North", "South", "East", "West", "North", "South", "East", "West"],
    "Sales": [200, 150, None, 300, 250, None, 220, 280],
    "Profit": [50, 40, 30, None, 60, 35, None, 70],
    "Category": ["Electronics", "Furniture", "Clothing", "Electronics",
                 "Furniture", "Clothing", "Electronics", "Furniture"]
}

df = pd.DataFrame(data)

# Raw Data
st.subheader("📄 Raw Data")
st.dataframe(df)

# Cleaning
df["Sales"].fillna(df["Sales"].mean(), inplace=True)
df["Profit"].fillna(df["Profit"].mean(), inplace=True)

# Cleaned Data
st.subheader("✅ Data After Cleaning")
st.dataframe(df)

# Sidebar filter
st.sidebar.header("🔍 Filter Data")
region = st.sidebar.selectbox("Select Region", df["Region"].unique())

filtered = df[df["Region"] == region]

# Metrics
total_sales = filtered["Sales"].sum()
total_profit = filtered["Profit"].sum()

col1, col2 = st.columns(2)
col1.metric("💰 Total Sales", f"{total_sales:.2f}")
col2.metric("📈 Total Profit", f"{total_profit:.2f}")

# --- Sales by Category (Bar Chart) ---
st.subheader("📊 Sales by Category")

cat_data = filtered.groupby("Category")["Sales"].sum()

fig1, ax1 = plt.subplots()
ax1.bar(cat_data.index, cat_data.values)
ax1.set_title(f"Sales by Category in {region}")
ax1.set_xlabel("Category")
ax1.set_ylabel("Sales")
plt.xticks(rotation=30)

st.pyplot(fig1)

# --- Scatter Plot (Sales vs Profit) ---
st.subheader("🔵 Scatter Plot: Sales vs Profit")

fig2, ax2 = plt.subplots()
ax2.scatter(filtered["Sales"], filtered["Profit"])

ax2.set_xlabel("Sales")
ax2.set_ylabel("Profit")
ax2.set_title(f"Sales vs Profit in {region}")

st.pyplot(fig2)

# --- Pie Chart (Category Distribution) ---
st.subheader("🥧 Sales Distribution by Category")

fig3, ax3 = plt.subplots()
ax3.pie(cat_data.values, labels=cat_data.index, autopct='%1.1f%%')

ax3.set_title(f"Category Share in {region}")

st.pyplot(fig3)