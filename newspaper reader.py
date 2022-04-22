
from pip import main
import requests
import json
import pyttsx3

# Akhbaar padhke sunaao
# def speak(str):
#     from win32com.client import Dispatch
#     speak = Dispatch("SAPI.SpVoice")
#     speak.Speak(str)
"""Function 'speak' can also be used to listen the news"""

def listen(str):
    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    converter.setProperty('volume', 1.2)
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    converter.setProperty('voice', voice_id)
    converter.say(str)
    converter.runAndWait()

if __name__=='__main__':

    listen("Starting Latest News")
    response = requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=54ad484f6aa7489a96182a950f2ab6d4")
    a = response.json()
    list1 = a["articles"]
    for i in list1:
        listen(i["title"])
        # print(i["title"])   
        # Above commented line can be used to read the news.
    listen("Thanks for patient listening")
        
