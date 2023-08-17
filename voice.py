from playsound import playsound
import pyttsx3

query = ""
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
engine.setProperty('rate',160)
query = ""



def Speak(audio):
    print("     ")
    print(f"  : {audio}")
    print("     ")
    engine.say(audio)
    engine.runAndWait()
    
