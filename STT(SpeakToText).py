import speech_recognition as sr
import pyaudio

class STT:
    def __init__(self):
        pass

    rec_static_instance = None
    @staticmethod
    def rec_instance(self):
        self.rec_static_instance = sr.Recognizer()
    
    def get_audio(self):
        rec = self.rec_static_instance
        with sr.Microphone() as source:
            audio_data = sr.listen(source)
            try:
                text = rec.recognize_google(audio_data, language = "ko")
            except Exception as e:
                pass
        
        return text
    
    def run(self):
        while True:
            text =  self.get_audio()
            print(text)
            
STT.run()