import speech_recognition as sr
import pyttsx3
import datetime


 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[1 ].id)
def speak(audio):
    pass
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
       speak("Good morning")  
       speak("I am jarvis sir. please tell me how can i help you") 
    elif hour>=12 and hour<18:
          speak("Good Afternon")

    else:
        speak("Good evening")



        speak("I am jarvis sir. please tell me how can i help you")
def takecommand():
    
     r = sr.Recognizer()
     with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

     try:
            print("Recongnizing...")
            query = r.recognize_google(audio, audio, language='en-in')
            print(f"User said: {query}\n")

     except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None" 
     return query  
if __name__ == "__main__":
    wishme()
    takecommand()