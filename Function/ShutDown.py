import os
import time
from Speak.smd1 import speak

def shutDown():
    """
    Shuts down the computer after 3 seconds with a spoken notification.
    
    Uses a custom 'speak' function to notify the user about the shutdown.
    If an error occurs during the shutdown process, an error message is spoken.
    """
    try:  
        speak("Shutdown the system in 3 seconds.")
        time.sleep(3)
        os.system('shutdown /s /t 1')

    except:
        speak("Something went wrong. Unable to shutdown the system.")


