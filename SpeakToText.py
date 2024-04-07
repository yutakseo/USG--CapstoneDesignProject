import speech_recognition as sr
#import pyaudio

rec = sr.Recognizer()
rec.energy_threshold = 2000
print("Run")
while True:
    with sr.Microphone() as source:
        try:
            audio_data = rec.listen(source, timeout=0.5)
            text = rec.recognize_google(audio_data, language = "ko")
        except:
            print("..")
            text = ""
        print(text)
