import streamlit as st
import pandas as pandas

names_link = "https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv"
names_data = pd.read_csv(names_link)

st.title("streamlit and pandas")
st.dataframe(name_data)
