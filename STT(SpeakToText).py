import speech_recognition as sr

class STT:
    def __init__(self, energy, speak_time_out, analyize_ambient_duration):
        self.energy_threshold = energy
        self.timeout = speak_time_out
        self.ambient_duration = analyize_ambient_duration
        print("음성 인식을 시작합니다")
        
    def get_audio(self):
        rec = sr.Recognizer()
        rec.energy_threshold = self.energy_threshold
        text = ""
        with sr.Microphone() as source:
            try:
                rec.listen(source, timeout = self.timeout)
                print("음성획득")
                #rec.adjust_for_ambient_noise(source=source, duration=self.ambient_duration)
                text = rec.recognize_google(source, language="ko")
                print("텍스트 변환성공")
            except Exception as e:
                text=".."
        return text
    
    def run(self):
        while True:
            text = self.get_audio()
            if text =="음성 인식 종료":
                print("\n음성 인식을 종료합니다")
                break
            else:
                print(text)

temp = STT(500, 1.0, 0.5)
temp.run()
