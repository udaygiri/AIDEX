'''
For install Speech recognition:
--> pip install SpeechRecognition

Speech Recognition Docs: https://pypi.org/project/SpeechRecognition/
'''

import speech_recognition as sr 

def listen():
    """Listens for speech and returns the recognized text."""

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print()
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing....")
        text = recognizer.recognize_google(audio,language="en-in")  # Use Google Speech Recognition
        print()
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""

