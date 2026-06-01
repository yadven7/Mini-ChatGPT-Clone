import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv

# Page setup should be near top
st.set_page_config(page_title="Mini ChatGPT", page_icon="🤖")
st.title("Mini ChatGPT Clone 🤖")

# API key: Streamlit Cloud secrets OR local .env
try:
    api_key = st.secrets["GEMINI_API_KEY"]  # Streamlit Cloud
except Exception:
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")   # Local

# Stop app if API key not found
if not api_key:
    st.error("API key not found. Add GEMINI_API_KEY in .env or Streamlit Secrets.")
    st.stop()

# Sidebar
with st.sidebar:
    st.title("Settings")

    if st.button("Clear Chat"):
        st.session_state.messages = []

        # Gemini internal chat history bhi clear hogi
        if "chat" in st.session_state:
            del st.session_state.chat

        st.rerun()

# Configure API key for google-generativeai
genai.configure(api_key=api_key)

# Create chat only once
if "chat" not in st.session_state:
    generation_config = {
        "temperature": 0.7,
    }
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        generation_config=generation_config
    )
    st.session_state.chat = model.start_chat(history=[])

# Initialize visible chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Type message")

if user_input:
    # Save and display user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # Get Gemini response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.chat.send_message(user_input)
                assistant_reply = response.text

                st.write(assistant_reply)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": assistant_reply
                })

            except Exception as e:
                st.error(f"Error: {e}")