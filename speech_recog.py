import speech_recognition as speech
import pyttsx3
engine=pyttsx3.init()
sp=speech.Recognizer()  #creating a class for speech recognition module
mic_list=speech.Microphone.list_microphone_names()  #list of microphones connected
mic=speech.Microphone(device_index=0)  #selecting a microphone for input
with mic as source:
    print("listening...")
    sp.adjust_for_ambient_noise(source)  #removing ambient noise
    audio=sp.listen(source)  #listening to the input

input=sp.recognize_google(audio)  #converting speech to text
print(input)

engine.setProperty('rate',250)
engine.say(input)
engine.runAndWait()





