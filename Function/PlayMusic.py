import pywhatkit
import pyautogui
import os
import random
from Speak.smd1 import speak
from Listen.listen import listen

def playMusic():
    speak("Boss which song you want to play.")
    song_name = listen().lower()

    if song_name != "":
        name = song_name.replace("play","")
        name = song_name.replace(" ","")
        try:
            pywhatkit.playonyt(name)
            speak(f"Playing {name} music boss.")
        except :
            speak("Something wrong boss. can't play music.")
            speak("Play offline Music.")
            offlineMusic() 
    else:
        speak("Boss You don't give music name.")
        speak("Play offline Music.")
        offlineMusic() 

def nextMusic():
    try:
        # Press and hold Shift, then press N, then release both keys
        pyautogui.keyDown('shift')
        pyautogui.press('n')
        pyautogui.keyUp('shift')
        speak("Play next Music boss.")
    except:
        print("Something Wrong...")


def offlineMusic():
    file_path = "D:\\music"
    try:
        # Get the list of files and directories in the folder
        files = os.listdir(file_path)
        # Filter out only files from the list
        files = [file for file in files if os.path.isfile(os.path.join(file_path, file))]
        # Select a random file from the list
        if files:
            musicName = random.choice(files)
            try:
                os.startfile(os.path.join(file_path, musicName))
                speak("Play offline Music boss.")
            except Exception:
                offlineMusic()
        else:
            print("No music files found in the folder:", file_path)
            return None
    except:
        print("An error occurred")
        return None

