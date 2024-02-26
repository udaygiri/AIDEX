"""
------------------- Speak Model - 2 -----------------
for install gtts:
--> pip install gtts

Gtts Module docs: https://gtts.readthedocs.io/en/latest/

issue: it's take so much time rather than pyttsx3.
"""

from gtts import gTTS 
import os

def speak(text):
    # Create a gTTS object
    # Give text than gtts model generate mp3 file 
    tts = gTTS(text=text, lang='en')

    # Save the audio file to your location
    tts.save('DataBase\\speak_audio\\audio.mp3')

    # Play the audio file
    os.system('DataBase\\speak_audio\\audio.mp3')

if __name__ == "__main__":
    speak(text="")


    


