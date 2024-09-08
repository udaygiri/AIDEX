#Import module...
from Listen.listen import listen
from Speak.smd1 import speak
from Function.ActiveApp import active_app
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
    # Convert the query to lowercase to ensure case-insensitive matching
    query = query.lower()

    # Check if the query contains the word "open" and call the openapp function
    if "open" in query:
        openapp(query)
    # Check if the query contains the word "close" and call the closeapp function
    elif "close" in query:
        closeapp(query)
    # Check if the query contains the word "screenshot" and call the screenshot function
    elif "screenshot" in query:
        screenshot()
    # Check if the query contains "play music" or "play song" and call the playMusic function
    elif "play music" in query or "play song" in query:
        playMusic()
    # Check if the query contains "next song" or "next music" and call the nextMusic function
    elif "next song" in query or "next music" in query:
        nextMusic()
    # Check if the query contains any exit-related words and respond with a farewell message, then exit
    elif any(word in query for word in ("exit", "bye", "tata", "see you")):
        speak("Call me any time when you need help, Have nice day Boss!!!")
        exit()
    # Check if the query contains "shutdown" or "system off" and call the shutDown function
    elif "shutdown" in query or "system off" in query:
        shutDown()
    # Check if the query contains "volume up" and increase the system volume
    elif "volume up" in query:
        ag.press("volumeup")
    # Check if the query contains "volume down" and decrease the system volume
    elif "volume down" in query:
        ag.press("volumedown")
    # Check if the query contains "mute" and mute the system volume
    elif "mute" in query:
        ag.press("volumemute")
    # Check if the query contains "unmute" and unmute the system volume
    elif "unmute" in query:
        ag.press("volumeunmute")



# Main function call.
if __name__ == "__main__":

    while True:
        query = listen().lower()
        if "jarvis" in query:
            speak("Hello Boss, i'm AIDEX: Artificial Intelligence Desktop Executor. Also known as Jarvis!!!")
            speak("How can i help you Boss!!!")
            while True:
                query = listen().lower()
                # query = query.replace("jarvis","")
                active_app(query)
                main(query)




