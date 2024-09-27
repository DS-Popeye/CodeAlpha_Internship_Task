import speech_recognition as sr
import pyttsx3
import webbrowser

# initializing the speech recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Define commands and actions
commands = {
    "open google": lambda: webbrowser.open("https://www.google.com"),
    "open facebook": lambda: webbrowser.open("https://www.facebook.com"),
    "tell me a joke": lambda: engine.say("Why did the bullet end up losing his job? He got fired!"),
    "stop listening": lambda: exit(),
}

# this function is to process voice commands
def process(command):
    action = commands.get(command.lower())
    if action:
        action()
    else:
        engine.say("Sorry, I didn't understand that command.")
    engine.runAndWait()

# waiting for input frm user to start    
input("Press any key to start listening...")

# Main loop to listen for commands
while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"Command: {command}")
        process(command)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        print("There was an error with the speech recognition service.")