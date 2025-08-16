import streamlit as st
import pandas as pd

st.title("My First Dashboard Test")

# Load your wrangled CSV
df = pd.read_csv("data/wrangled_data_env.csv")

st.subheader("Preview of dataset")
st.write(df.head())

