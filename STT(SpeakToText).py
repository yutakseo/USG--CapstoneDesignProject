import speech_recognition as sr

class STT:
    def __init__(self, energy, speak_time_out, analyize_ambient_duration):
        self.rec_static_instance = sr.Recognizer()
        self.rec_static_instance.energy_threshold = energy
        self.timeout = speak_time_out
        self.ambient_duration = analyize_ambient_duration
        print("음성 인식을 시작합니다")
        
    def get_audio(self):
        rec = self.rec_static_instance
        text = ""
        with sr.Microphone() as source:
            try:
                rec.listen(source, timeout = self.timeout)
                #noise_cancelled_audio = rec.adjust_for_ambient_noise(source=audio_data, duration=0.5)
                rec.adjust_for_ambient_noise(source=source, duration=self.ambient_duration)
                text = rec.recognize_google(source, language="ko")
            except Exception as e:
                pass
        return text
    
    def run(self):
        while True:
            text = self.get_audio()
            if text =="음성 인식 종료":
                print("\n음성 인식을 종료합니다")
                break
            else:
                print(text)

temp = STT(1000, 1.0, 0.5)
temp.run()
