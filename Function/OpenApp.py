from AppOpener import open, close
from Speak.smd1 import speak
from Function.OpenWeb import openWeb


def openapp(query):
    query = query.replace("open","") # replace unwonted word.
    query = query.replace(" ","") # Remove white space
    query = query.lower()

    if "github" in query:
        openWeb(query)   
    
    else:
         # open application by app name using open function.
        try:
            # open closest app which match with query.
            open(query,match_closest=True,output=True, throw_error=True)
            speak(f"Opening {query}")       

        except:
            openWeb(query)

def closeapp(query):
    query = query.replace("close","") # replace unwonted word.
    query = query.replace(" ","") # Remove white space

    # close application by app name using open function.
    close(query,match_closest=True, output=False) # open closest app which match with query.
    speak(f"Closing {query}")
