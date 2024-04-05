import speech_recognition as sr

class STT:
    def __init__(self):
        self.rec_static_instance = sr.Recognizer()
        print("Run!")
        
    def get_audio(self):
        rec = self.rec_static_instance
        with sr.Microphone() as source:
            #audio_data = rec.record(source, duration=5)
            try:
                audio_data = rec.listen(source=source, timeout=1)
                text = rec.recognize_google(audio_data, language="ko")
            except Exception as e:
                text = "...listening"
        return text
    
    def run(self):
        while True:
            text = self.get_audio()
            if text:
                print(text)


temp = STT()
temp.run()
