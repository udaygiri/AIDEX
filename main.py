# Neccesser module...
from Listen.listen import listen
from Speak.smd1 import speak
from Function.OpenApp import openapp, closeapp


# Main function section...
def main():
    query = listen()

    if "open" in query:
        openapp(query)
    
    elif "close" in query:
        closeapp(query)

# Main function call.
if __name__ == "__main__":
    speak("Hello, i'm AIDEX: Artificial Intelligence Desktop Executor.")
    while True:
        main()
