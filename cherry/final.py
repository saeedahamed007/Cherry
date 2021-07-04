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
    p2 = Thread(target=transition2)
    p2.start()
    time.sleep(7)
    root.destroy()

def transition2():
    global img1
    global flag
    global flag2
    global frames
    global canvas
    local_flag = False
    for k in range(0,5000):
        for frame in frames:
            if flag == False:
                canvas.create_image(0, 0, image=img1, anchor=NW)
                canvas.update()
                flag = True
                return
            else:
                canvas.create_image(0, 0, image=frame, anchor=NW)
                canvas.update()
                time.sleep(0.1)
        
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
        answer = "Sorry. I could not find the desired results"


    canvas2.create_text(10, 225, anchor=NW, text=answer, font=('Candara Light', -25,'bold italic'),fill="white", width=350)
    flag2 = False
    loading.destroy()

    p1=Thread(target=speak,args=(answer,))
    p1.start()
    p2 = Thread(target=transition2)
    p2.start()

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

    canvas2.create_text(10,10,anchor =NW , text=text,font=('Candara Light', -25,'bold italic'), fill="white",width=350)
    p1=Thread(target=speak,args=(text,))
    p1.start()
    p2 = Thread(target=transition2)
    p2.start()

def takecommand():
    global loading
    global flag
    global flag2
    global canvas2
    global query
    global img4
    if flag2 == False:
        canvas2.delete("all")
        canvas2.create_image(0,0, image=img4, anchor="nw")

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
        canvas2.create_text(490, 120, anchor=NE, justify = RIGHT ,text=query, font=('fixedsys', -30),fill="white", width=350)
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
    canvas2.create_text(10, 225, anchor=NW, text='', font=('Candara Light', -25,'bold italic'),fill="white", width=350)
    text1='type on notepad'
    p1=Thread(target=speak,args=(text1,))
    p1.start()
    p2 = Thread(target=transition2)
    p2.start()
    flag2=False

def office_write():
    global flag2
    global loading
    pyautogui.press('win',interval=0.2)
    pyautogui.typewrite('Microsoft Office Word 2007',interval=0.4)
    pyautogui.press('enter',interval=0.8)  
    canvas2.create_text(10, 225, anchor=NW, text='', font=('Candara Light', -25,'bold italic'),fill="white", width=350)
    text1='type on microsoft word 2007'
    p1=Thread(target=speak,args=(text1,))
    p1.start()
    p2 = Thread(target=transition2)
    p2.start()
    flag2=False 

def calculator():
    speak('Say expression')
    try:
        voice_data3=record_audio()
        s=eval_binary_expr(*(voice_data3.split()))
        canvas2.create_text(10, 225, anchor=NW, text=f'The answer for the expression is:{s}', font=('Candara Light', -25,'bold italic'),fill="white", width=350)
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
    canvas2.create_text(10, 225, anchor=NW, text='', font=('Candara Light', -25,'bold italic'),fill="white", width=350)
    text2='open docuements'
    p1=Thread(target=speak,args=(text2,))
    p1.start()
    p2 = Thread(target=transition2)
    p2.start()
    flag2=False

def opendownloads():
    global flag2
    global loading
    pyautogui.press('win',interval=0.2)
    pyautogui.typewrite('This PC',interval=0.6)
    pyautogui.press('enter',interval=0.6)
    canvas2.create_text(10, 225, anchor=NW, text='', font=('Candara Light', -25,'bold italic'),fill="white", width=350)
    text2='open downloads'
    p1=Thread(target=speak,args=(text2,))
    p1.start()
    p2 = Thread(target=transition2)
    p2.start()  
    flag2=False    

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

            elif 'calculator' in query:
                calculator()
                query=None    
            
            elif 'open downloads' in query:
                opendownloads()
                pyautogui.doubleClick(x=150,y=375,interval=0.6)
                query=None 

            
            elif 'documents' or 'document' in query:
                opendocuements() 
                pyautogui.doubleClick(x=150,y=345,interval=0.6)
                query=None    
                 

            else: 
                web_scraping(query)
                query=None     


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

    img1= PhotoImage(file='chatbot.png')
    img2= PhotoImage(file='button-green.png')
    img3= PhotoImage(file='icon.png')
    img4= PhotoImage(file='terminal.png')
    background_image=PhotoImage(file="last.png")
    
    f = Frame(root,width = 1360, height = 690)
    f.place(x=0,y=0)
    f.tkraise()
    front_image = PhotoImage(file="voice-bot.png")
    okVar = IntVar()
    btnOK = Button(f, image=front_image,command=lambda: okVar.set(1))
    btnOK.place(x=0,y=0)
    f.wait_variable(okVar)
    f.destroy() 
    

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
    canvas2=Canvas(frame,bg='#FFFFFF',width=500,height=596,scrollregion=(0,0,500,900))
    vbar=Scrollbar(frame,orient=VERTICAL)
    vbar.pack(side=RIGHT,fill=Y)
    vbar.config(command=canvas2.yview)
    canvas2.config(width=500,height=596, background="black")
    canvas2.config(yscrollcommand=vbar.set)
    canvas2.pack(side=LEFT,expand=True,fill=BOTH)
    canvas2.create_image(0,0, image=img4, anchor="nw")

    task = Thread(target=main_window)
    task.start()
    root.mainloop()

'''

     elif 'documents' or 'document' in query:
                opendocuements() 
                pyautogui.doubleClick(x=150,y=345,interval=0.6)
                query=None
'''                