import streamlit as st
import pandas as pd
from pathlib import Path
from bot import Bot

def initialize_session_state():
    """Initialize session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "bot" not in st.session_state:
        st.session_state.bot = Bot()

def display_chat_messages():
    """Display chat messages from history"""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_user_input():
    """Handle user input and generate bot response."""
    # walrus operatro :=
    # if promt:
    # prompt=st.chat_input("What is up?")
    if prompt := st.chat_input("Vad vill du ena veta?"):

        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})

        bot_response = st.session_state.bot.chat(prompt)
        response = f"Ro Båt: {bot_response}"

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})

def layout():
    """Define the layout of the Streamlit app."""
    st.title("Tjatta med RO BÅT")
    st.write("RO BÅT är en robot som hjälper dig att analysera saker och han gillar att driva med Stockholmare")
    display_chat_messages()
    handle_user_input()

if __name__ == "__main__":
    initialize_session_state()
    layout()