#Import module...
from Listen.listen import listen
from Speak.smd1 import speak
from Function.ActiveApp import activeApps
from Function.OpenApp import openapp, closeapp
from Function.PlayMusic import playMusic, nextMusic
from Function.ScreeShote import screenshot
from Function.ShutDown import shutDown
import pyautogui as ag



# Main function section...
def main(query):
    """
    Main function to execute all the commands.

    Args:
        query (str): The voice command to execute.
    """
    query = query.lower()

    if "open" in query:
        openapp(query)
    elif "close" in query:
        closeapp(query)
    elif "screenshot" in query:
        screenshot()
    elif "play music" in query or "play song" in query:
        playMusic()
    elif "next song" in query or "next music" in query:
        nextMusic()
    elif any(word in query for word in ("exit","bye","tata","see you")):
        speak("Call me any time when you need help, Have nice day Boss!!!")
        exit()
    elif "shutdown" in query or "system off" in query:
        shutDown()
    elif "volume up" in query:
        ag.press("volumeup")
    elif "volume down" in query:
        ag.press("volumedown")
    elif "mute" in query:
        ag.press("volumemute")
    elif "unmute" in query:
        ag.press("volumeunmute")


# Main function call.
if __name__ == "__main__":
    speak("Hello Boss, i'm AIDEX: Artificial Intelligence Desktop Executor.")
    speak("How can i help you Boss!!!")

    while True:
        query = listen().lower()
        if "jarvis" in query:
            query = query.replace("jarvis","")
            activeApps(query)
            main(query)




