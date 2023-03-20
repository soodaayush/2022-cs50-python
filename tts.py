import pyttsx3

engine = pyttsx3.init()
name = input("Say something: ")
engine.say(f"{name}")
engine.runAndWait()