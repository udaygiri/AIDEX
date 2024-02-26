import webbrowser
from Resources.webside import websitesList
from Speak.smd1 import speak

def openWeb(website_name):
    
    # Convert the website name to lowercase for case-insensitive matching
    website_name = website_name.lower()
    
    # Check if the website name exists in the dictionary
    if website_name in websitesList:
        # Open the website in the default web browser
        webbrowser.open(websitesList[website_name])
        speak(f"opening {website_name}")
    else:
        print("Website not found.")

