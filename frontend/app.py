import streamlit as st
import requests

st.title(
    "LLM Chatbot"
)

prompt = st.text_input(
    "Enter message"
)

if st.button("Send"):

    response = requests.post(
        "http://127.0.0.1:8000/chat",

        json={
            "prompt":prompt
        }
    )

    st.write(
        response.json()["response"]
    )