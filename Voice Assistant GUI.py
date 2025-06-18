import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    response_label.config(text=f"Assistant: {text}")

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        response_label.config(text="Listening...")
        window.update()
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio, language='en-in')
            command = command.lower()
            input_label.config(text=f"You said: {command}")
            handle_command(command)
        except sr.WaitTimeoutError:
            speak("You were silent.")
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that...")
        except sr.RequestError:
            speak("Check your internet connection....")

def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def get_date():
    return datetime.datetime.now().strftime("%A, %d %B %Y")

def handle_command(command):
    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")
    elif "how are you" in command:
        speak("I'm fine, thank you! what about you?")
    elif "good" or "fine" in command:
        speak(f"happy to hear that , how can i assist you")
    elif "time" in command:
        speak(f"The time is {get_time()}")
    elif "date" in command:
        speak(f"Today is {get_date()}")
    elif "search for" in command:
        query = command.replace("search for", "").strip()
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif "Created you" or "creator" in command:
        speak(f" I was created by Rohan for voice assistant project purpose on the day 18 june ")
        
    elif "stop" in command or "exit" in command:
        speak("Goodbye!")
        window.destroy()
    else:
        speak("Sorry, I can't do that yet.")

# GUI setup
window = tk.Tk()
window.title("Voice Assistant")
window.geometry("400x280")
window.configure(bg="#222222")

title_label = tk.Label(window, text="Voice Assistant", font=("Helvetica", 18), bg="#222222", fg="white")
title_label.pack(pady=10)

input_label = tk.Label(window, text="Press the button and speak...", font=("Helvetica", 12), bg="#222222", fg="lightgreen")
input_label.pack(pady=10)

response_label = tk.Label(window, text="", font=("Helvetica", 12), bg="#222222", fg="cyan")
response_label.pack(pady=10)

listen_button = tk.Button(window, text="🎤 Start Listening", font=("Helvetica", 14), bg="blue", fg="white", command=listen_command)
listen_button.pack(pady=20)

exit_button = tk.Button(window, text="❌ Exit", font=("Helvetica", 12), bg="red", fg="white", command=window.destroy)
exit_button.pack()

window.mainloop()
