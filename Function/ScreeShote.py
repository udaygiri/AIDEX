import pyscreenshot
from datetime import datetime
import os
from Speak.smd1 import speak

def screenshot():
    """
    Function to take a screenshot and save it to the specified directory.
    
    
    Returns:
    - str: The filename of the saved screenshot.
    """
    try:
        # Get the current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")

        # Take a screenshot of the entire screen
        screenshot = pyscreenshot.grab()

        # Save the screenshot to a file
        screenshot.save(f"DataBase\\ScreenShot\\ss_{timestamp}.png")
        print("Screenshot saved successfully:", f"DataBase\\ScreenShot\\ss_{timestamp}.png")
        speak("Screenshot saved successfully. open screenshot.")
        os.open(f"DataBase\\ScreenShot\\ss_{timestamp}.png")
        return f"DataBase\\ScreenShot\\ss_{timestamp}.png"
    except Exception as e:
        print("Error occurred while taking or saving screenshot:", e)
        return None


