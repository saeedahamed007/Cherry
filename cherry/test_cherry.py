# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 20:50:38 2021

@author: Shrinidhi
"""


# Code for virtual assistant with GUI 
import speech_recognition as sr
import pyttsx3
import time
import pyautogui
import datetime
from time import ctime
import webbrowser
import playsound
import os
import random
from gtts import gTTS
from tkinter import *
from PIL import ImageTk,Image

def wishme():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        lee_voice("Good Morning Friend. I am Cherry. How can I assist you?")
    elif 12 <= hour < 18:
        lee_voice("Good Afternoon Friend. I am Cherry. How can I assist you?")
    else:
        lee_voice("Good Evening Friend. I am Cherry. How can I assist you?")

print('Say something...')
r = sr.Recognizer()
speaker = pyttsx3.init()

# def takecommand():
#     global loading
#     global flag
#     global flag2
#     #global canvas2
#     global query
#     global img4
#     # if flag2 == False:
#     #     canvas2.delete("all")
#     #     canvas2.create_image(0,0, image=img4, anchor="nw")

#     speak("I am listening.")
#     flag= True
#     r = sr.Recognizer()
#     r.dynamic_energy_threshold = False
#     r.energy_threshold = 4000
#     with sr.Microphone() as source:
#         print("Listening...")
#         #r.pause_threshold = 3
#         audio = r.listen(source)

def record_audio(ask = False):
 #user voice record
    with sr.Microphone() as source:
        if ask:
            lee_voice(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print('Recognizer voice :'+ voice_data)
        except Exception:
            print('Oops something went Wrong')
 #lee_voice('Oops something went Wrong')
        return voice_data
def lee_voice(audio_string):
 #Play audio text to voice
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
def notepad():
    #global flag2
    #global loading
    pyautogui.press('win',interval=0.2)
    pyautogui.typewrite('notepad',interval=0.6)
    pyautogui.press('enter',interval=0.6) 
    text1='type on notepad'
class Widget: #GUI OF VIRTUAL ASSISTAND AND COMMANDS 
    def __init__(self):
        root = Tk()
        root.title('Cherry-The Voice Bot')
        root.geometry('1520x720') 
        img = ImageTk.PhotoImage(Image.open('chatbot-image.png'))
        panel = Label(root, image=img)
        panel.pack(side='right', fill='both', expand='no')
        compText = StringVar()
        userText = StringVar()
        userText.set('Your Virtual Assistant')
        frames = [PhotoImage(file='chatgif.gif',format = 'gif -index %i' %(i)) for i in range(20)]
        canvas = Canvas(root, width = 800, height = 596)
        canvas.place(x=10,y=10)
        canvas.create_image(0, 0, image=img1, anchor=NW)
        question_button = Button(root,image=img2, bd=0, command=takecommand)
        question_button.place(x=200,y=625)
        #userFrame = LabelFrame(root, text='Lena', font=('Railways', 24,  'bold'))
        #userFrame.pack(fill='both', expand='yes')
        #top = Message(userFrame, textvariable=userText, bg='white', fg='black')
        #top.config(font=("Century Gothic", 15, 'bold'))
        #top.pack(side='top', fill='both', expand='yes')
 # compFrame = LabelFrame(root, text="Lena", font=('Railways', 
#10, 'bold'))
 # compFrame.pack(fill="both", expand='yes')
        btn = Button(root, text='Speak', font=('railways', 10, 'bold'),bg='red', fg='white', command=self.clicked).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close', font=('railways', 10, 'bold'), bg='grey', fg='white', command=root.destroy).pack(fill='x', expand='no')
        wishme()
        root.mainloop()
    def clicked(self):
 #BUTTON CALLING
        # print("working...")
        # voice_data = record_audio()
        # voice_data = voice_data.lower()
        try:
            print("Recognizing..")
            query = r.recognize_google(audio, language='en-in')
            print(f"user Said :{query}\n")
            query = query.lower()
            # canvas2.create_text(490, 120, anchor=NE, justify = RIGHT ,text=query, font=('fixedsys', -30),fill="white", width=350)
            global img3
            loading = Label(root, image=img3, bd=0)
            loading.place(x=900, y=622)

        except Exception as e:
            print(e)
            speak("Say that again please")
            return "None"
        if 'who are you' in voice_data:
            lee_voice('My name is Lena ')
        if 'search' in voice_data:
            search = record_audio('What do you want to search for ?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            lee_voice('Here is what i found' + search)
        if 'type on notepad' in voice_data  :
                notepad()
                voice_data1=record_audio()
                pyautogui.typewrite(voice_data1)
                voice_data = None
        if 'find location' in voice_data:
            location = record_audio('What is your location?')
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            lee_voice('Here is location' + location)
        if 'what is the time' in voice_data or "time" in voice_data:
            lee_voice("Sir the time is :" + ctime())
        if 'exit' in voice_data:
            lee_voice('Thanks have a good day ')
            exit()
if __name__== '__main__':
    widget = Widget()
    time.sleep(1)
while 1:
    voice_data = record_audio()
    r.respond(voice_data)
speaker.runAndWait()