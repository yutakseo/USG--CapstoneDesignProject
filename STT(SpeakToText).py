import speech_recognition as sr, time

class STT:
    def __init__(self):
        self.rec_static_instance = sr.Recognizer()
        print("음성 인식을 시작합니다")
        
    def get_audio(self):
        rec = self.rec_static_instance
        with sr.Microphone() as source:
            try:
                audio_data = rec.listen(source, timeout=0.4)
                text = rec.recognize_google(audio_data, language="en-US") #ko
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
                print(f"\n{time.strftime('%I:%M:%S')} - ", text)

temp = STT()
temp.run()