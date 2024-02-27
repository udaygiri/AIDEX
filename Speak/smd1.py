'''
------------------- Speak Model - 1 -----------------

For install pyttsx3
--> pip install pyttsx3

pyttsx3 Docs: https://pypi.org/project/pyttsx3/

'''
import pyttsx3

def speak(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Set the speed of the speech
    engine.setProperty('rate', 175)

    # Set the voice of the speech
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # Say something
    engine.say(text)
    if (text!=""):
        print(f"AIDEx said: {text}")

    # Wait for the speech to finish
    engine.runAndWait()
