import streamlit as st
import speech_recognition as sr
import pyttsx3
from main import get_bot_response

st.set_page_config(page_title="Voice Bot", page_icon="🎤")
st.title("Voice Bot with Voice Input & Output")


def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


col1, col2 = st.columns([8,1])
with col1:
    user_input = st.text_input("Type your message or use the mic:", key="text_input")
with col2:
    voice_clicked = st.button("🎤", help="Click to speak")


if voice_clicked:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Please speak now.")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        try:
            MyText = r.recognize_google(audio)
            st.session_state["text_input"] = MyText
            st.success(f"You said: {MyText}")
        except sr.RequestError as e:
            st.error(f"Could not request results; {e}")
        except sr.UnknownValueError:
            st.error("Sorry, I could not understand your voice.")
    st.experimental_rerun()


bot_response = None
if st.button("Send"):
    if user_input.strip():
        st.write(f"**You:** {user_input}")
        bot_response = get_bot_response(user_input)
        st.write(f"**Bot:** {bot_response}")
        SpeakText(bot_response)