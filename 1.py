from google import genai
from google.genai import types
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

api_key = st.secrets.get("AQ.Ab8RN6LLFXeSWMwDG9XuMvFaMARsTpgXKTO2oea2PCKT94yOaQ") or os.getenv("AQ.Ab8RN6LLFXeSWMwDG9XuMvFaMARsTpgXKTO2oea2PCKT94yOaQ")
client = genai.Client(api_key=api_key)

# Page setup
st.set_page_config(page_title="Mini ChatGPT", page_icon="🤖")
st.title("Mini ChatGPT Clone 🤖")
# API key yahan

# Sidebar
# Sidebar clear button
with st.sidebar:
    st.title("Settings")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Session state initialize
if "client" not in st.session_state:
    st.session_state.client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

if "chat" not in st.session_state:

    config = types.GenerateContentConfig(
        temperature=0.7
    )

    st.session_state.chat = st.session_state.client.chats.create(
        model="gemini-2.5-flash",
        config=config
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

# Old messages display
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Type message")

if user_input:

    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # Gemini response
    response = st.session_state.chat.send_message(user_input)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response.text
    })

    with st.chat_message("assistant"):
        st.write(response.text)