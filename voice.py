import pyttsx3

def speak_text(text):
    """Convert the given text to speech using pyttsx3."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Example usage:
if __name__ == "__main__":
    speak_text("Hello, this is a test of the text to speech system.")