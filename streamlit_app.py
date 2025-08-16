import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Dashboard Demo")

# Load both datasets
df_group = pd.read_csv("data/wrangled_data_group.csv")
df_individual = pd.read_csv("data/wrangled_data_individual.csv")

st.subheader("Group Dataset (first 5 rows)")
st.dataframe(df_group.head(), use_container_width=True)

st.subheader("Individual Dataset (first 5 rows)")
st.dataframe(df_individual.head(), use_container_width=True)

