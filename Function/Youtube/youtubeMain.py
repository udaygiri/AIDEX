from Speak.smd1 import speak  # Importing the speak function from Speak.smd1 module
import pywhatkit as pw  # Importing pywhatkit module as pw
import pyautogui as ag  # Importing pyautogui module as ag
import time  # Importing time module

def ytmain(query):
    """
    Function to control YouTube playback using voice commands.

    Args:
    query (str): The voice command to execute.
    """

    if "search" in query:
        ag.press("/")  # Pressing '/' to activate the search bar
        query = query.replace("search","")  # Removing the word "search" from the query
        ag.write(query)  # Typing the query into the search bar
        time.sleep(1)  # Giving some time for the search results to load
        ag.press("enter")  # Pressing Enter to execute the search
        speak(f"Searching for {query}")  # Speaking the search query

    elif "next" in query:
        ag.press("n")  # Pressing 'n' to go to the next video

    elif "previous" in query:
        ag.press("p")  # Pressing 'p' to go to the previous video

    elif "mute" in query:
        ag.press("m")  # Pressing 'm' to mute the video

    elif "unmute" in query:
        ag.press("m")  # Pressing 'm' to unmute the video

    elif "full screen" in query or "fullscreen" in query:
        ag.press("f")  # Pressing 'f' to toggle fullscreen mode

    elif "normal screen" in query or "normalscreen" in query:
        ag.press("f")  # Pressing 'f' to exit fullscreen mode

    elif "stop" in query:
        pw.stop()  # Stopping the current video playback

    elif "pause" in query or "pause video" in query or "play" in query or "play video" in query:
        ag.press("space")  # Pressing 'space' to pause the video

    elif "volume" in query:
        query = query.replace("volume","")  # Extracting the volume level from the query
        query = int(query)  # Converting the volume level to an integer
        pw.volume(query)  # Setting the volume to the specified level

    # Scroll down and up the page
    elif "scroll down" in query:
        ag.press("pagedown")  # Pressing Page Down to scroll down

    elif "scroll up" in query:
        ag.press("pageup")  # Pressing Page Up to scroll up

