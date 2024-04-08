import speech_recognition as sr
#import pyaudio

print("Run")
num = 0

while True:
    num +=1
    rec = sr.Recognizer()
    rec.energy_threshold = 500
    text = ""
    with sr.Microphone() as source:
        try:
            audio_data = rec.listen(source, timeout=0.3, phrase_time_limit=5)
            text = rec.recognize_google(audio_data, language = "ko")
        except:
            text = ""
        print(text)
    print(num)
