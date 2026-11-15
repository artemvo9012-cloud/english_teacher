import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import random
translator = Translator()

wins = 5


words_by_level = {
    1 : ["кот", "собака", "яблоко", "молоко", "солнце"],
    2 : ["банан", "школа", "друг", "окно", "жёлтый"],
    3 : ["технология", "университет", "информация", "произношение", "воображение"]
}

print("игра словарь для запоминания английских слов")
print("у тебя будет 10 баллов при правильном произношении + 1 балл")
print("при неправильном - 1 балл")
print("еще есть и уровни сложности ")

while wins >= 1:
        print("у тебя жизней: ")
        print(wins)
        complexity = int(input("а вот и выбор сложности 1 изи 2 медиум и 3 сложно"))
        word = random.choice(words_by_level[complexity])
        translated = translator.translate(word, dest="en")
        answer = translated.text.strip().lower() 
        print("тебе попалось слово ")
        print(word)




        
        duration = 5
        sample_rate = 44100
        print("Говори...")
        recording = sd.rec(
        int(duration * sample_rate), # длительность записи в сэмплах
        samplerate=sample_rate,      # частота дискретизации
        channels=1,                  # 1 — это моно
        dtype="int16")               # формат аудиоданных
        sd.wait()  # ждём завершения записи
        wav.write("output.wav", sample_rate, recording)
        print("Запись завершена, теперь распознаём...")
        recognizer = sr.Recognizer()
        with sr.AudioFile("output.wav") as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio, language="en")
        print("Ты сказал:", text)
        word = translated.text.strip().lower() 
        if text == word:
            wins += 1
        else:
            wins -= 1
if wins == 0:
    print("ты проиграл")
    print("если хочешь продолжить введи 5")
    wins = int (input(_))
