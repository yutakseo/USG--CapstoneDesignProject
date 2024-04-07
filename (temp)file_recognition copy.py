import speech_recognition as sr
import os
import playsound
# AUDIO_DIR이 실제 오디오 파일이 위치한 디렉토리의 이름이라고 가정
AUDIO_DIR = os.getcwd()
# os.path.join을 사용하여 파일의 전체 경로를 구성
audio = os.path.join(AUDIO_DIR, "AUDIO_DIR/harvard.wav")
# 이제 audio_file_path를 사용하여 파일을 여는 등의 작업을 할 수 있습니다.
noised_audio = os.path.join(AUDIO_DIR, "AUDIO_DIR/jackhammer.wav")


file = noised_audio

#playsound.playsound(file, block=False)


input_sound = sr.AudioFile(file)
r = sr.Recognizer()
with input_sound as source:
    r.adjust_for_ambient_noise(source=source, duration=0.1)
    playsound.playsound(source)
    #audio = r.record(source=source)
    
print("\n\nresult : ",r.recognize_google(audio),"\n\n")


