import streamlit as st
import pandas as pd
import pycountry
import plotly.express as px

# Load data
df = pd.read_csv("animals.csv")

st.title("🐾 Animal History Map")

# Select year
year = st.slider("Pick a year", min_value=1500, max_value=2025, value=2020)

# Select country
country = st.selectbox("Pick a country", sorted(df["country"].unique()))

# Show animals
filtered = df[(df["country"] == country) & (df["year"] == year)]

st.subheader(f"Animals in {country} in {year}")
if filtered.empty:
    st.write("No data found.")
else:
    for animal in filtered["animal"]:
        st.write("•", animal)

# Optional: Show map
country_obj = pycountry.countries.get(name=country)
if country_obj:
    iso_code = country_obj.alpha_3
    fig = px.choropleth(locations=[iso_code], locationmode="ISO-3", color=[1])
    st.plotly_chart(fig)
