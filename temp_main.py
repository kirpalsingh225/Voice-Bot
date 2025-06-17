import streamlit as st

st.set_page_config(page_title="Kirpal Singh Voice Bot", page_icon="🤖")
st.title("Kirpal Singh Voice Bot")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# User input (should be above chat history for better UX)
user_input = st.text_input("Type your message and press Enter:", key="user_input")

send_clicked = st.button("Send")

# On send, clear all previous messages and show only the latest exchange
if send_clicked and user_input.strip():
    st.session_state["messages"] = []  # Clear previous messages
    st.session_state["messages"].append({"role": "user", "content": user_input})
    # Here you would call your RAG/LLM backend to get the answer
    bot_response = "[Bot's answer will appear here. Integrate your RAG/LLM logic.]"
    st.session_state["messages"].append({"role": "bot", "content": bot_response})
    st.rerun()  # Do not try to set st.session_state["user_input"] directly

# Display chat history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")
