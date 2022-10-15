# pip install gtts playsound
# Anaconda prompt > conda activate aip
# 파일을 저장해줘야 문장 읽기 가능

from gtts import gTTS
import playsound

news = input("읽고자 하는 문장을 입력하세요. : ")
file_name = input("저장하고자 하는 파일 이름을 입력하세요. : ")

tts = gTTS(text = news, lang='ko')
"""
tts_k = gTTS(text = news, lang ='ko')
tts_e= gTTS(text = news, lang ='en')
tts_f= gTTS(text = news, lang ='fr')
"""

# 같은 이름의 파일이 이미 있으면 오류 발생
# import os
# os.remove(file_name+".mp3")를 추가하면 여러 번 반복 가능

tts.save(file_name+".mp3")
playsound.playsound(file_name+".mp3",True)
