from Speak.smd1 import speak
import pywhatkit as pw
import pyautogui as ag

def ytmain(query):
    if "pause" in query or "play" in query:
        ag.press("k")