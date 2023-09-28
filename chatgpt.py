import pyaudio
import pyttsx3
from pyllamacpp.model import Model as ModelG
import random
import time

TALKING = ""

def choice(a,b):
    number = random.randint(a,b)
    return number

def speak(text):
    global TALKING
    chat = TALKING
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    TALKING = 'Yes'
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Speaking Exception: "+str(e))
        pass
    TALKING = chat


def new_text_callback(text: str):
    print(text,end="")


def GPT(QUESTION):

    prompt = (QUESTION + "?")

    num=choice(1,4)
    if num == 1:
        speak("Processing.One moment sir")
    elif num == 2:
        speak("Processing the request")
    elif num == 3:
        speak("Processing. This may take some time sir")
    elif num == 4:
        speak("Working on it sir. Please be patient.")

    model = ModelG(ggml_model='C:/J.A.R.V.I.S. A.I/gpt4all-model.bin',n_ctx=512)

    generated_text = model.generate(prompt,n_predict=50,new_text_callback=new_text_callback,n_threads=6)
    generated_text = generated_text.replace(prompt,"")

    try:
     if num == 1:
         speak("I have the requested information sir")
     elif num == 2:
         speak("Request completed")
     elif num == 3:
         speak("Processing completed")
     elif num == 4:
         speak("Done sir")
     speak(generated_text)
    except:
        print("Error with GPT processing.")
        pass

def main():
    Task = input("How can I help?")
    GPT(Task)

main()
 
    
