import streamlit as st
import requests
import pandas as pd

st.title(
    "Analytics Dashboard"
)

data=requests.get(
    "http://127.0.0.1:8000/history"
).json()

df=pd.DataFrame(data)

st.dataframe(df)