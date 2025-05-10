# AI-Powered-Voice-Assistant
## 🧠 AI Voice Assistant using Python
A simple AI-powered voice assistant built with Python that can recognize voice commands, speak responses, search the web, open applications, and perform useful tasks like checking the time or date.

## 📌 Features
🎤 Voice recognition using Google Speech Recognition API

🔊 Text-to-speech using pyttsx3

🕒 Tells current time and date

🌐 Opens Google and YouTube

📖 Answers questions using Wikipedia

🎵 Plays local music

✅ Modular and extensible command handler

🧠 Works offline for TTS (text-to-speech)

## 🚀 Getting Started
✅ Prerequisites
Ensure you have Python installed (preferably Python 3.8+). Install the following packages:

pip install SpeechRecognition pyttsx3 wikipedia pyaudio
If pyaudio throws errors on Windows:

pip install pipwin
pipwin install pyaudio
## 📂 Project Structure

voice_assistant/
│
├── voice_assistant.py     # Main Python script
├── README.md              # Documentation
🔧 How to Run
Clone the repository or copy the code.

Open terminal or command prompt.

Run:

python voice_assistant.py
Start speaking when prompted!

## 🧠 Available Commands
Command	Action
"What is the time"	Speaks current time
"What is the date"	Speaks today's date
"Open Google"	Opens Google in your default browser
"Open YouTube"	Opens YouTube
"Wikipedia [topic]"	Reads summary from Wikipedia
"Play music"	Plays a music file from local directory
"Exit" or "Bye"	Closes the assistant

## 🧱 Built With
Python 3

SpeechRecognition

pyttsx3

Wikipedia API

PyAudio

## ⚙️ Customization
To change the music directory, edit this line in the Python file:

Edit
music_dir = "C:\\Users\\Public\\Music"
Add new commands by extending the handle_command() function.
