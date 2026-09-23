import streamlit as st
import pandas as pd

names_link = "https://raw.githubusercontent.com/D0n0Van-NETIZEN/Plantas/refs/heads/main/titanic%20(3).csv"
names_data = pd.read_csv(names_link)

st.title("streamlit and pandas")
st.dataframe(name_data)
