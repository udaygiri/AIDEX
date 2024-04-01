import pygetwindow as gw
from Function.Youtube.youtubeMain import ytmain
def activeApps(query):
    # Get the active window
    active_window = gw.getActiveWindow()

    if active_window:
        activeApp  = active_window.title.lower()

        if "youtube" in activeApp:
            ytmain(query)
    else:
        return "No active application found."


