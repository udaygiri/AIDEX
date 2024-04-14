import pygetwindow as gw
from Function.Youtube.youtubeMain import ytmain
def active_app(query):
    """
    Finds the active window and passes the voice command to the 
    appropriate function based on the active application

    Args:
        query (str): The voice command to execute
    """
    # Get the active window
    active_window = gw.getActiveWindow()

    if not active_window:
        return

    app_name = active_window.title.lower()

    # YouTube
    if "youtube" in app_name:
        ytmain(query)


