import pyttsx3
import time

def speak_phrase(phrases):
	engine = pyttsx3.init()
	rate = engine.getProperty('rate')
	engine.setProperty('rate', 125)
	voices = engine.getProperty('voices')  # getting details of current voice
	engine.setProperty('voice', voices[1].id)
	engine.say(phrases)
	#time.sleep(0.5)
	#engine.say("This is a simple demo of Python Text to Speech Engine and its working.")
	engine.runAndWait()
	engine.stop()