import pyautogui
import pytube
import speech_recognition as sr
from Speak.smd1 import speak

def ytmain(query):
    """
    Function to control YouTube playback using voice commands.

    Args:
        query (str): The voice command to execute.
    """
    # Go to the next video
    if "next" in query:
        pyautogui.hotkey('shift', 'n')

    # Go to the previous video
    elif "previous" in query:
        pyautogui.hotkey('shift', 'p')

    # Mute the current video
    elif "mute" in query:
        pyautogui.press('m')

    # Unmute the current video
    elif "unmute" in query:
        pyautogui.press('m')

    # Toggle fullscreen mode
    elif "full screen" in query or "fullscreen" in query:
        pyautogui.press('f')

    # Exit fullscreen mode
    elif "normal screen" in query or "normalscreen" in query:
        pyautogui.press('f')

    # Stop the current video playback
    elif "stop" in query:
        pyautogui.press('k')

    # Pause or resume the video playback
    elif "pause" in query or "pause video" in query or "play" in query or "play video" in query:
        pyautogui.press('k')

    # Set the volume of the video
    elif "volume" in query:
        query = query.replace("volume", "").strip()
        set_volume(int(query))

    # Scroll down the page
    elif "scroll down" in query:
        pyautogui.scroll(-500)

    # Scroll up the page
    elif "scroll up" in query:
        pyautogui.scroll(500)

def set_volume(level):
    for _ in range(50):  # Reset volume to 0
        pyautogui.press('volumedown')
    for _ in range(level):  # Set to desired level
        pyautogui.press('volumeup')

# Example usage with voice recognition
def listen_and_execute():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print(f"Command: {query}")
            ytmain(query.lower())
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Could not request results; check your network connection.")

# Uncomment to use voice recognition
# listen_and_execute()

