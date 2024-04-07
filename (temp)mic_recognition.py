import speech_recognition as sr


r = sr.Recognizer()
r.energy_threshold = 300
mic = sr.Microphone()


with mic as source:
    audio = r.listen(source, timeout=0.5)
    r.adjust_for_ambient_noise(source=audio, duration=0.5)
    text = r.recognize_google(audio, language="ko")
    
print(text)