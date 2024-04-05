import speech_recognition as sr

class STT:
    def __init__(self):
        self.rec_static_instance = sr.Recognizer()
        print("음성 인식을 시작합니다")
        
    def get_audio(self):
        rec = self.rec_static_instance
        with sr.Microphone() as source:
            try:
                #source = rec.adjust_for_ambient_noise(source)
                audio_data = rec.listen(source, timeout=1.3)
                text = rec.recognize_google(audio_data, language="ko")
            except Exception as e:
                text = "..."
        return text
    
    def run(self):
        while True:
            text = self.get_audio()
            if text =="음성 인식 종료":
                print("\n음성 인식을 종료합니다")
                break
            else:
                print(text)

temp = STT()
temp.run()
