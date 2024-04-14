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

    if "open" in query:
        openapp(query)
    
    elif "close" in query:
        closeapp(query)

    elif "ss" in query or "screenshot" in query:
        screenshot()

    elif "play music" in query or "play song" in query :
        playMusic()

    elif "next music" in query or "next song" in query:
        nextMusic()

    elif "exit" in query or "by" in query or "bye" in query or "by" in query or "tata" in query or "see you" in query:
        speak("Call me any time when you need help, Have nice day Boss!!!")
        exit()

    elif "shutdown" in query or "system off" in query:
        shutDown()

    elif "volume up" in query:
        speak("Volume increased")
        ag.press("volumeup")

    elif "volume down" in query:
        speak("Volume decreased")
        ag.press("volumedown")

    elif "mute" in query:
        speak("Volume muted")
        ag.press("volumemute")

    elif "unmute" in query:
        speak("Volume unmuted")
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




