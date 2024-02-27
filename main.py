# Neccesser module...
from Listen.listen import listen
from Speak.smd1 import speak
from Function.OpenApp import openapp, closeapp


# Main function section...
def main():
    query = listen().lower()

    if "open" in query:
        openapp(query)
    
    elif "close" in query:
        closeapp(query)
    
    elif "exit" in query:
        exit()
        speak("Call me any time when you need help, Have nice Boss!!!")

# Main function call.
if __name__ == "__main__":
    speak("Hello, i'm AIDEX: Artificial Intelligence Desktop Executor.")
    speak("How can i help you Boss!!!")

    while True:
        main()
