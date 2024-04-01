import pywhatkit
from Speak.smd1 import speak

def musicYt(song_name):
    try:
        pywhatkit.playonyt(song_name)
        speak(f"Playing {song_name} music")
    except Exception as e:
        print("An error occurred:", str(e))


