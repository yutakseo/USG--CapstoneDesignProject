import speech_recognition as sr
import pyaudio

rec = sr.Recognizer()
print("Run")
while True:
    with sr.Microphone() as source:
        audio_data = rec.record(source, duration=5)
        try:
            text = rec.recognize_google(audio_data, language = "ko")
        except:
            print("..")
            text = ""
        print(text)
