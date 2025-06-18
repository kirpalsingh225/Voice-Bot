import streamlit as st
from voice import speak_text
from main import get_bot_response

st.set_page_config(page_title="Voice Bot", page_icon="🎤")
st.title("Text to Speech Bot")

# UI: Text input only
user_input = st.text_input("Type your message:", key="text_input")

# When user submits text
if st.button("Send"):
    if user_input.strip():
        st.write(f"**You:** {user_input}")
        bot_response = get_bot_response(user_input)
        st.write(f"**Bot:** {bot_response}")
        speak_text(bot_response)
    else:
        st.warning("Please enter a message.")
