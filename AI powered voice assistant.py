import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import wikipedia

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Greet user
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your assistant. How can I help you today?")

# Listen and recognize voice
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print(f"You said: {command}")
    except sr.UnknownValueError:
        speak("Sorry, I did not catch that. Please repeat.")
        return ""
    except sr.RequestError:
        speak("Could not request results. Please check your internet connection.")
        return ""
    return command.lower()

# Handle recognized command
def handle_command(command):
    if 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")
    
    elif 'date' in command:
        date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {date}")
    
    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    
    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'wikipedia' in command:
        speak("Searching Wikipedia...")
        topic = command.replace("wikipedia", "").strip()
        if topic:
            result = wikipedia.summary(topic, sentences=2)
            speak("According to Wikipedia")
            speak(result)
        else:
            speak("Please tell me what to search on Wikipedia.")

    elif 'play music' in command:
        music_dir = "C:\\Users\\Public\\Music"  # Change this path
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))
        else:
            speak("No music files found.")
    
    elif 'exit' in command or 'bye' in command:
        speak("Goodbye!")
        exit()
    
    else:
        speak("Sorry, I don't know that command yet.")

# Main loop
if __name__ == "__main__":
    greet()
    while True:
        command = listen()
        if command:
            handle_command(command)
