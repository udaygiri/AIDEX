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

    # Search a video on YouTube
    if "search" in query:
        query = query.replace("search","")
        pw.search(query, mode="list")
        speak(f"Searching for {query}")

    # Go to the next video
    elif "next" in query:
        pw.playnext(mode="list")

    # Go to the previous video
    elif "previous" in query:
        pw.playprevious(mode="list")

    # Mute the current video
    elif "mute" in query:
        pw.mute(mode="list")

    # Unmute the current video
    elif "unmute" in query:
        pw.unmute(mode="list")

    # Toggle fullscreen mode
    elif "full screen" in query or "fullscreen" in query:
        pw.fullscreen(mode="list")

    # Exit fullscreen mode
    elif "normal screen" in query or "normalscreen" in query:
        pw.normalscreen(mode="list")

    # Stop the current video playback
    elif "stop" in query:
        pw.stop(mode="list")

    # Pause or resume the video playback
    elif "pause" in query or "pause video" in query or "play" in query or "play video" in query:
        pw.pause(mode="list")

    # Set the volume of the video
    elif "volume" in query:
        query = query.replace("volume","")
        query = int(query)
        pw.volume(query, mode="list")

    # Scroll down the page
    elif "scroll down" in query:
        pw.scroll_down(mode="list")

    # Scroll up the page
    elif "scroll up" in query:
        pw.scroll_up(mode="list")

