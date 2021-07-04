from tkinter import *
import time
import datetime
import webbrowser
import pyttsx3
import pyautogui
import operator
import speech_recognition as sr
from threading import Thread
import requests
from bs4 import BeautifulSoup
import subprocess 
import wolframalpha 
import pyttsx3 
import tkinter 
import json 
import random 
import operator 
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os 
import winshell 
import pyjokes 
import feedparser 
import smtplib 
import ctypes 
import time 
import requests 
import shutil 
from twilio.rest import Client 
from clint.textui import progress 
from ecapture import ecapture as ec 
from bs4 import BeautifulSoup 
import win32com.client as wincl 
from urllib.request import urlopen 

r=sr.Recognizer() #
def record_audio(ask=False):
    with sr.Microphone() as source: #
        if(ask):
            speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            speak('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down') # error: recognizer is not connected        
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()

def shut_down():
    p1=Thread(target=speak,args=("Shutting down. Thankyou For Using Our Sevice. Take Care, Good Bye.",))
    p1.start()
    # p2 = Thread(target=transition2)
    # p2.start()
    time.sleep(7)
    root.destroy()

# def transition2():
#     global img1
#     global flag
#     global flag2
#     global frames
#     global canvas
#     local_flag = False
#     for k in range(0,5000):
#         for frame in frames:
#             if flag == False:
#                 canvas.create_image(0, 0, image=img1, anchor=NW)
#                 canvas.update()
#                 flag = True
#                 return
#             else:
#                 canvas.create_image(0, 0, image=frame, anchor=NW)
#                 canvas.update()
#                 time.sleep(0.1)
        
def web_scraping(qs):
    global flag2
    global loading

    URL = 'https://www.google.com/search?q=' + qs
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    links = soup.findAll("a")
    all_links = []
    for link in links:
       link_href = link.get('href')
       if "url?q=" in link_href and not "webcache" in link_href:
           all_links.append((link.get('href').split("?q=")[1].split("&sa=U")[0]))
           

    flag= False
    for link in all_links:
       if 'https://en.wikipedia.org/wiki/' in link:
           wiki = link
           flag = True
           break

    div0 = soup.find_all('div',class_="kvKEAb")
    div1 = soup.find_all("div", class_="Ap5OSd")
    div2 = soup.find_all("div", class_="nGphre")
    div3  = soup.find_all("div", class_="BNeawe iBp4i AP7Wnd")

    if len(div0)!=0:
        answer = div0[0].text
    elif len(div1) != 0:
       answer = div1[0].text+"\n"+div1[0].find_next_sibling("div").text
    elif len(div2) != 0:
       answer = div2[0].find_next("span").text+"\n"+div2[0].find_next("div",class_="kCrYT").text
    elif len(div3)!=0:
        answer = div3[1].text
    elif flag==True:
       page2 = requests.get(wiki)
       soup = BeautifulSoup(page2.text, 'html.parser')
       title = soup.select("#firstHeading")[0].text
       
       paragraphs = soup.select("p")
       for para in paragraphs:
           if bool(para.text.strip()):
               answer = title + "\n" + para.text
               break
    else:
        speak("Sorry. I could not find the desired results")


    flag2 = False
    loading.destroy()

    p1=Thread(target=speak,args=(answer,))
    p1.start()

def speak(text):
    global flag
    engine.say(text)
    engine.runAndWait()
    flag=False

def wishme():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        text = "Good Morning Friend. I am Cherry. How can I assist you?"
    elif 12 <= hour < 18:
        text = "Good Afternoon Friend. I am Cherry. How can I assist you?"
    else:
        text = "Good Evening Friend. I am Cherry. How can I assist you?"
    p1=Thread(target=speak,args=(text,))
    p1.start()

def takecommand():
    global loading
    #global flag
    #global flag2
    global query
    global img4


    speak("I am listening.")
    flag= True
    r = sr.Recognizer()
    r.dynamic_energy_threshold = False
    r.energy_threshold = 4000
    with sr.Microphone() as source:
        print("Listening...")
        #r.pause_threshold = 3
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user Said :{query}\n")
        query = query.lower()
        global img3
        loading = Label(root, image=img3, bd=0)
        loading.place(x=900, y=622)

    except Exception as e:
        print(e)
        speak("Say that again please")
        return "None"

def notepad():
    global flag2
    global loading
    pyautogui.press('win',interval=0.2)
    pyautogui.typewrite('notepad',interval=0.6)
    pyautogui.press('enter',interval=0.6) 
    text1='type on notepad'
    p1=Thread(target=speak,args=(text1,))
    p1.start()
    flag2=False

def office_write():
    global flag2
    global loading
    pyautogui.press('win',interval=0.2)
    pyautogui.typewrite('Microsoft Office Word 2007',interval=0.4)
    pyautogui.press('enter',interval=0.8)  
    text1='type on microsoft word 2007'
    p1=Thread(target=speak,args=(text1,))
    p1.start()

    flag2=False 

def calculator():
    speak('Say expression')
    try:
        voice_data3=record_audio()
        s=eval_binary_expr(*(voice_data3.split()))
        speak(f'The answer for the expression is:{s}')
    except sr.UnknownValueError: 
        speak('say once again') 

def get_operator_fn(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        'x' : operator.mul,
        'divided' :operator.__truediv__,
        'Mod' : operator.mod,
        'mod' : operator.mod,
        '^' : operator.xor,
        }[op]
def eval_binary_expr(op1, oper, op2):
    op1,op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)              
    

def opendocuements():
    global flag2
    global loading
    pyautogui.press('win',interval=0.2)
    pyautogui.typewrite('This PC',interval=0.6)
    pyautogui.press('enter',interval=0.6)
    text2='open docuements'
    p1=Thread(target=speak,args=(text2,))
    p1.start()
    flag2=False

def opendownloads():
    global flag2
    global loading
    pyautogui.press('win',interval=0.2)
    pyautogui.typewrite('This PC',interval=0.6)
    pyautogui.press('enter',interval=0.6)
    # s
    text2='open downloads'
    p1=Thread(target=speak,args=(text2,))
    p1.start()
    # p2 = Thread(target=transition2)
    # p2.start()  
    flag2=False
def sendEmail(to, content): 
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo() 
    server.starttls() 
      
    # Enable low security in gmail 
    server.login('your email id', 'your email passowrd') 
    server.sendmail('your email id', to, content) 
    server.close() 
    

def main_window():
    global query
    wishme()
    while True:
        if query != None:
            if 'shutdown' in query or 'quit' in query or 'stop' in query or 'goodbye' in query:
                shut_down()
                break 
             
            elif 'type on notepad' in  query:
                notepad()
                voice_data1=record_audio()
                pyautogui.typewrite(voice_data1)
                query = None

            elif 'Office Word' in query:
                office_write()
                voice_data2=record_audio()
                pyautogui.typewrite(voice_data2)
                query = None

            # elif 'calculator' in query:
            #     calculator()
            #     query=None    
            
            elif 'open downloads' in query:
                opendownloads()
                pyautogui.doubleClick(x=150,y=375,interval=0.6)
                query=None 

            
            elif 'documents' or 'document' in query:
                opendocuements() 
                pyautogui.doubleClick(x=150,y=345,interval=0.6)
                query=None
            elif 'open youtube' in query: 
                speak("Here you go to Youtube\n") 
                webbrowser.open("youtube.com") 
  
            elif 'open google' in query: 
                speak("Here you go to Google\n") 
                webbrowser.open("google.com") 
  
            elif 'open stackoverflow' in query: 
                speak("Here you go to Stack Over flow.Happy coding") 
                webbrowser.open("stackoverflow.com")    
  
            elif 'play music' in query or "play song" in query: 
                speak("Here you go with music") 
                #music_dir = "G:\\Song"
                music_dir = "C:\\Users\\itech\\Music"
                songs = os.listdir(music_dir) 
                print(songs)     
                random = os.startfile(os.path.join(music_dir, songs[1])) 
  
            elif 'the time' in query: 
                strTime = datetime.datetime.now().strftime("% H:% M:% S")     
                speak(f"Sir, the time is {strTime}") 
  
            elif 'open opera' in query: 
                codePath = r"C:\\Users\\GAURAV\\AppData\\Local\\Programs\\Opera\\launcher.exe"
                os.startfile(codePath) 
  
            elif 'email to saeed' in query: 
                try: 
                    speak("What should I say?") 
                    content = takecommand() 
                    to = "Receiver email address"    
                    sendEmail(to, content) 
                    speak("Email has been sent !") 
                except Exception as e: 
                    print(e) 
                    speak("I am not able to send this email") 
  
            elif 'send a mail' in query: 
                try: 
                    speak("What should I say?") 
                    content = takecommand() 
                    speak("whome should i send") 
                    to = input()     
                    sendEmail(to, content) 
                    speak("Email has been sent !") 
                except Exception as e: 
                    print(e) 
                    speak("I am not able to send this email") 
  
            elif 'how are you' in query: 
                speak("I am fine, Thank you") 
                speak("How are you, Sir") 
  
            elif 'fine' in query or "good" in query: 
                speak("It's good to know that your fine") 
  
            elif "change my name to" in query: 
                query = query.replace("change my name to", "") 
                assname = query 
  
            elif "change name" in query: 
                speak("What would you like to call me, Sir ") 
                assname = takecommand() 
                speak("Thanks for naming me") 
  
            elif "what's your name" in query or "What is your name" in query: 
                speak("My friends call me") 
                speak(assname) 
                print("My friends call me", assname) 
  
            elif 'exit' in query: 
                speak("Thanks for giving me your time") 
                exit() 
  
            elif "who made you" in query or "who created you" in query:  
                speak("I have been created by chinnu.") 
              
            elif 'joke' in query: 
                speak(pyjokes.get_joke()) 
              
            elif "calculate" in query:  
              
                app_id = "Wolframalpha api id" 
                client = wolframalpha.Client(app_id) 
                indx = query.lower().split().index('calculate')  
                query = query.split()[indx + 1:]  
                res = client.query(' '.join(query))  
                answer = next(res.results).text 
                print("The answer is " + answer)  
                speak("The answer is " + answer)  
  
            elif 'search' in query or 'play' in query: 
              
                query = query.replace("search", "")  
                query = query.replace("play", "")           
                webbrowser.open(query)  
  
            elif "who i am" in query: 
                speak("If you talk then definately you are human.") 
  
            elif "why you came to world" in query: 
                speak("Thanks to Gaurav. further It's a secret") 
  
            elif 'power point presentation' in query: 
                speak("opening Power Point presentation") 
                power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
                os.startfile(power) 
  
            elif 'is love' in query: 
                speak("It is 7th sense that destroy all other senses") 
  
            elif "who are you" in query: 
                speak("I am your virtual assistant created by Gaurav") 
  
            elif 'reason for you' in query: 
                speak("I was created as a Minor project by Mister Gaurav ") 
  
            elif 'change background' in query: 
                ctypes.windll.user32.SystemParametersInfoW(20,  
                                                       0,  
                                                       "Location of wallpaper", 
                                                       0) 
                speak("Background changed succesfully") 
  
            elif 'open bluestack' in query: 
                appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
                os.startfile(appli) 
  
            elif 'news' in query: 
              
                try:  
                    jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''') 
                    data = json.load(jsonObj) 
                    i = 1
                  
                    speak('here are some top news from the times of india') 
                    print('''=============== TIMES OF INDIA ============'''+ '\n') 
                  
                    for item in data['articles']: 
                      
                        print(str(i) + '. ' + item['title'] + '\n') 
                        print(item['description'] + '\n') 
                        speak(str(i) + '. ' + item['title'] + '\n') 
                        i += 1
                except Exception as e: 
                  
                    print(str(e)) 
  
          
            elif 'lock window' in query: 
                speak("locking the device") 
                ctypes.windll.user32.LockWorkStation() 
  
            elif 'shutdown system' in query: 
                speak("Hold On a Sec ! Your system is on its way to shut down") 
                subprocess.call('shutdown / p /f') 
                  
            elif 'empty recycle bin' in query: 
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
                speak("Recycle Bin Recycled") 
  
            elif "don't listen" in query or "stop listening" in query: 
                speak("for how much time you want to stop jarvis from listening commands") 
                a = int(takecommand()) 
                time.sleep(a) 
                print(a) 
  
            elif "where is" in query: 
                query = query.replace("where is", "") 
                location = query 
                speak("User asked to Locate") 
                speak(location) 
                webbrowser.open("https://www.google.nl / maps / place/" + location + "") 
  
            elif "camera" in query or "take a photo" in query: 
                ec.capture(0, "Jarvis Camera ", "img.jpg") 
  
            elif "restart" in query: 
                subprocess.call(["shutdown", "/r"]) 
              
            elif "hibernate" in query or "sleep" in query: 
                speak("Hibernating") 
                subprocess.call("shutdown / h") 
  
            elif "log off" in query or "sign out" in query: 
                speak("Make sure all the application are closed before sign-out") 
                time.sleep(5) 
                subprocess.call(["shutdown", "/l"])
               
            elif "write a note" in query: 
                speak("What should i write, sir") 
                note = takecommand() 
                file = open('jarvis.txt', 'w') 
                speak("Sir, Should i include date and time") 
                snfm = takecommand() 
                if 'yes' in snfm or 'sure' in snfm: 
                    strTime = datetime.datetime.now().strftime("% H:% M:% S") 
                    file.write(strTime) 
                    file.write(" :- ") 
                    file.write(note) 
                else: 
                    file.write(note) 
          
            elif "show note" in query: 
                speak("Showing Notes") 
                file = open("jarvis.txt", "r")  
                print(file.read()) 
                speak(file.read(6)) 
              

            # else: 
            #     web_scraping(query)
            #     query=None     


if __name__ == "__main__":
    loading = None
    query = None
    flag = True
    flag2 = True

    engine = pyttsx3.init() # Windows
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-10)

    root=Tk()
    root.title("Intelligent Chatbot")
    root.geometry('1360x690+-5+0')
    root.configure(background='white')

    img1= PhotoImage(file='chatbot-image.png')
    img2= PhotoImage(file='button-green.png')
    img3= PhotoImage(file='icon.png')
    img4= PhotoImage(file='terminal.png')
    background_image=PhotoImage(file="last.png")
    
    # f = Frame(root,width = 1360, height = 690)
    # f.place(x=0,y=0)
    # f.tkraise()
    # front_image = PhotoImage(file="front2.png")
    # okVar = IntVar()
    # btnOK = Button(f, image=front_image,command=lambda: okVar.set(1))
    # btnOK.place(x=0,y=0)
    # f.wait_variable(okVar)
    # f.destroy() 
    

    background_label = Label(root, image=background_image)
    background_label.place(x=0, y=0)

    frames = [PhotoImage(file='chatgif.gif',format = 'gif -index %i' %(i)) for i in range(20)]
    canvas = Canvas(root, width = 800, height = 596)
    canvas.place(x=10,y=10)
    canvas.create_image(0, 0, image=img1, anchor=NW)
    question_button = Button(root,image=img2, bd=0, command=takecommand)
    question_button.place(x=200,y=625)

    frame=Frame(root,width=500,height=596)
    frame.place(x=825,y=10)
    vbar=Scrollbar(frame,orient=VERTICAL)
    vbar.pack(side=RIGHT,fill=Y)
    #vbar.config(command=canvas2.yview)
    task = Thread(target=main_window)
    task.start()
    root.mainloop()

'''

     elif 'documents' or 'document' in query:
                opendocuements() 
                pyautogui.doubleClick(x=150,y=345,interval=0.6)
                query=None
'''                