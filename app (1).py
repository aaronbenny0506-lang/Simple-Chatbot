"""
app.py
Streamlit web interface for the rule-based chatbot.

Run locally with:
    streamlit run app.py
"""

import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="Simple Chatbot", page_icon="🤖")

st.title("🤖 Simple Rule-Based Chatbot")
st.caption("A beginner-friendly chatbot built with Python + Streamlit — no API key needed!")

# Keep chat history in Streamlit's session state so it persists
# across reruns (Streamlit reruns the whole script on every interaction).
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm a simple chatbot. Ask me something, or say 'help'."}
    ]

# Display the full conversation so far
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Text input field for the user's message
user_input = st.chat_input("Type your message here...")

if user_input:
    # Show the user's message immediately
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Generate and show the bot's reply
    reply = get_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)

with st.sidebar:
    st.header("About")
    st.write(
        "This chatbot uses simple keyword/pattern matching (regex) "
        "to decide how to respond — no AI model or internet connection required."
    )
    st.write("Try typing: **hi**, **joke**, **time**, **help**, or **bye**.")
    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.rerun()
