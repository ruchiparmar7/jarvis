import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import cv2
from time import ctime
import time
from requests import get
import sys
import pywhatkit as kit
from googletrans import Translator
from pytube import YouTube
import pyjokes
import phonenumbers
from phonenumbers import timezone
from phonenumbers import carrier
from phonenumbers import geocoder
import speedtest
from bs4 import BeautifulSoup
import PyPDF2
import psutil
import pyautogui
from pywikihow import search_wikihow
import instaloader
import requests
#from dictionary import translate
#from news import speak_news, getNewsUrl
from PIL import Image

# importing the module
from englisttohindi.englisttohindi import EngtoHindi
  

#import COVID19Py

print("""
    --------------------------------------------------------------------------       
    |           __    ______    ______   __           __  _      _____       |     
    |          |  |  |  __  |  |  __  \  \ \         / / | |    / ____]      |    
    |          |  |  | |__| |  | |  | |   \ \       / /  | |   / /           |     
    |          |  |  |  __  |  | '--'_/    \ \     / /   | |   \ \____       |         
    |    __    |  |  | |  | |  |  _  \      \ \   / /    | |    \___  \      |     
    |    \ |___|  |  | |  | |  | | \  \      \ \_/ /     | |    ____}  |     |    
    |     \_______/  |_|  |_|  |_|  \__\      \___/      |_|    \_____/      |         
    |                                                                        |      
    --------------------------------------------------------------------------     
""")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id) for boy voice
engine.setProperty('voice', voices[1].id)
def silenceTime(query):
        print(query)
        x=0
        #caliculating the given time to seconds from the speech commnd string
        if ('10' in query) or ('ten' in query):x=600
        elif '1' in query or ('one' in query):x=60
        elif '2' in query or ('two' in query):x=120
        elif '3' in query or ('three' in query):x=180
        elif '4' in query or ('four' in query):x=240
        elif '5' in query or ('five' in query):x=300
        elif '6' in query or ('six' in query):x=360
        elif '7' in query or ('seven' in query):x=420
        elif '8' in query or ('eight' in query):x=480
        elif '9' in query or ('nine' in query):x=540
        silence(x)
        
    #Silence
def silence(k):
        t = k
        s = "Ok okay I will be silent for "+str(t/60)+" minutes"
        speak(s)
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        speak("okay "+str(k/60)+" minutes over")

def condition():
        usage = str(psutil.cpu_percent())
        speak("CPU is at"+usage+" percentage")
        print("CPU is at"+ usage +" percentage")
        battray = psutil.sensors_battery()
        percentage = battray.percent
        print(percentage)
        speak(f"Boss our system have {percentage} percentage Battery")
        
        if percentage >=75:
            speak(f"Boss we could have enough charging to continue our work")
            print(f"Boss we could have enough charging to continue our work")
        elif percentage >=40 and percentage <=75:
            speak(f"Boss we should connect out system to charging point to charge our battery")
            print(f"Boss we should connect out system to charging point to charge our battery")
        elif percentage >=15 and percentage <=30:
            speak(f"Boss we don't have enough power to work, please connect to charging")
            print(f"Boss we don't have enough power to work, please connect to charging")
        else:
            speak(f"Boss we have very low power, please connect to charging otherwise the system will shutdown very soon")
            print(f"Boss we have very low power, please connect to charging otherwise the system will shutdown very soon")

def pdf_reader():
        speak("okay enter the name of the book which you want to read")
        n = input("Enter the book name: ")
        n = n.strip()+".pdf"
        book_n = open(n,'rb')
        pdfReader = PyPDF2.PdfFileReader(book_n)
        pages = pdfReader.numPages
        speak(f"okay there are total of {pages} in this book")
        speak("please enter the page number Which I nead to read")
        num = int(input("Enter the page number: "))
        page = pdfReader.getPage(num)
        text = page.extractText()
        print(text)
        speak(text)
def news():
        MAIN_URL_= "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=YOUR_NEWS_API_KEY"
        MAIN_PAGE_ = get(MAIN_URL_).json()
        articles = MAIN_PAGE_["articles"]
        headings=[]
        seq = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth'] #If you need more than ten you can extend it in the list
        for ar in articles:
            headings.append(ar['title'])
        for i in range(len(seq)):
            print(f"todays {seq[i]} news is: {headings[i]}")
            speak(f"todays {seq[i]} news is: {headings[i]}")
        speak("Boss I am done, I have read most of the latest news")
def scshot():
        #speak("Boss, please tell me the name for this screenshot file")
        name = takeCommand()
        speak("Please boss hold the screen for few seconds, I am taking screenshot")
        time.sleep(3)
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'C:\Users\ruchi\OneDrive\Desktop\screenshot1.png')
        speak("I am done boss, the screenshot is saved in main folder.")
'''       
def Covid(s):
        try:
            from covid_india import states
            details = states.getdata()
            if "check in" in s:
                s = s.replace("check in","").strip()
                print(s)
            elif "check" in s:
                s = s.replace("check","").strip()
                print(s)
            elif "tech" in s:
                s = s.replace("tech","").strip()
            s = state[s]
            ss = details[s]
            Total = ss["Total"]
            Active = ss["Active"]
            Cured = ss["Cured"]
            Death = ss["Death"]
            print(f"Boss the total cases in {s} are {Total}, the number of active cases are {Active}, and {Cured} people cured, and {Death} people are death")
            speak(f"Boss the total cases in {s} are {Total}, the number of active cases are {Active}, and {Cured} people cured, and {Death} people are death")
            time.sleep(5)
            speak("Boss do you want any information of other states")
            I = takeCommand()
            print(I)
            if ("check" in I):
                Covid(I)
            else:
                speak("Okay boss stay home stay safe")
                pass
        except:
            speak("Boss some error occured, please try again")
            speak("Boss which state covid 19 status do you want to check")
            I = takeCommand()
            Covid(I)
        '''
def Instagram_Pro():
        speak("Boss please enter the user name of Instagram: ")
        name = input("Enter username here: ")
        webbrowser.open(f"www.instagram.com/{name}")
        time.sleep(5)
        speak("Boss would you like to download the profile picture of this account.")
        cond = takeCommand()
        if('download' in cond):
            mod = instaloader.Instaloader()
            mod.download_profile(name,profile_pic_only=True)
            speak("I am done boss, profile picture is saved in your main folder. ")
        else:
            pass

def Cal_day():
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',4: 'Thursday', 5: 'Friday', 6: 'Saturday',7: 'Sunday'}
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            print(day_of_the_week)
        
        return day_of_the_week

         


    #Search for a process how to do
def How():
        speak("How to do mode is is activated")
        while True:
            speak("Please tell me what you want to know")
            how = takeCommand()
            try:
                if ("exit" in how) or("close" in how):
                    speak("Ok sir how to mode is closed")
                    break
                else:
                    max_result=1
                    how_to = search_wikihow(how,max_result)
                    assert len(how_to) == 1
                    how_to[0].print()
                    speak(how_to[0].summary)
            except Exception as e:
                speak("Sorry sir, I am not able to find this")

def tran():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=1)
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source , phrase_time_limit=4)

        try:
            print("Recognizing...")    
   # message to be translated
            message = takeCommand()
  
# creating a EngtoHindi() object
            res = EngtoHindi(message)
  
# displaying the translation
            print(res.convert)
            speak(f'the translated line is {res.convert}')
    
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source , phrase_time_limit=4)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("Say that again please...")  
        return "None"
    return query
def InternetSpeed():
        speak("Wait a few seconds okay, checking your internet speed")
        st = speedtest.Speedtest()
        dl = st.download()
        dl = dl/(1000000) #converting bytes to megabytes
        up = st.upload()
        up = up/(1000000)
        print(dl,up)
        speak(f"okay, we have {dl} megabytes per second downloading speed and {up} megabytes per second uploading speed")
def verifyMail():
        try:
            speak("what should I say?")
            content = takeCommand()
            speak("To whom do u want to send the email?")
            to = takeCommand()
            sendEmail(to,content)
            speak("Email has been sent to "+str(to))
        except Exception as e:
            print(e)
            speak("Sorry sir I am not not able to send this email")


def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("ruchiparmar065@gmail.com","ruchi@2001")
    server.sendmail("parmarvivek084@gmail.com",to,content)
    server.close()

def whatsapp():
    speak("tell me the name of the person!")
    name=takeCommand()
    
    if 'bro' in name:
        speak("tell me the message!")
        msg=takeCommand()
        speak("tell me the time!")
        speak("time in hour !")
        hour = int(takeCommand())
        speak("time in minute !")
        minute = int(takeCommand())
        kit.sendwhatmsg("+917984234520",msg,hour,minute,20)
        speak("ok ,sending whatsapp message!")
        
    elif 'papa' in name:
        speak("tell me the message!")
        msg=takeCommand()
        speak("tell me the time!")
        speak("time in hour !")
        hour = int(takeCommand())
        speak("time in minute !")
        minute = int(takeCommand())
        kit.sendwhatmsg("+919825587131",msg,hour,minute,20)
        speak("ok ,sending whatsapp message!")
    else:
        speak("tell me the number !")
        phonenumber=int(takeCommand())
        ph='+91'+phonenumber
        speak("tell me the message!")
        msg=takeCommand()
        speak("tell me the time!")
        speak("time in hour !")
        hour = int(takeCommand())
        speak("time in minute !")
        minute = int(takeCommand())
        kit.sendwhatmsg("+917984234520",msg,hour,minute,20)
        speak("ok ,sending whatsapp message!") 

def track():
     ro_number = phonenumbers.parse("+919328061722", None)
     print(geocoder.description_for_number(ro_number, "en"))
     print(carrier.name_for_number(ro_number, "en"))
     print(timezone.time_zones_for_number(ro_number))
    # covid19 = COVID19Py.COVID19(data_source="in")
     #print(covid19)
     
def temperature():
        IP_Address = get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
        geo_reqeust = get(url)
        geo_data = geo_reqeust.json()
        city = geo_data['city']
        search = f"temperature in {city}"
        url_1 = f"https://www.google.com/search?q={search}"
        r = get(url_1)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        speak(f"current {search} is {temp}")
        
def location():
        speak("Wait boss, let me check")
        try:
            IP_Address = get('https://api.ipify.org').text
            print(IP_Address)
            url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
            print(url)
            geo_reqeust = get(url)
            geo_data = geo_reqeust.json()
            city = geo_data['city']
            state = geo_data['region']
            country = geo_data['country']
            tZ = geo_data['timezone']
            longitude = geo_data['longitude']
            latidute = geo_data['latitude']
            org = geo_data['organization_name']
            print(city+" "+state+" "+country+" "+tZ+" "+longitude+" "+latidute+" "+org)
            speak(f"Boss i am not sure, but i think we are in {city} city of {state} state of {country} country")
            speak(f"and boss, we are in {tZ} timezone the latitude os our location is {latidute}, and the longitude of our location is {longitude}, and we are using {org}\'s network ")
        except Exception as e:
            speak("Sorry boss, due to network issue i am not able to find where we are.")
            pass

if __name__ == "__main__":
    

    wishMe()
    while True:
       # command = takeCommand() #Every time taking command after a task is done
       # print(command)
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if ('wikipedia' in query) or ('open wikipedia'):
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif ('open youtube' in query) or ('youtube' in query):
            speak("opening the youtube !")
            webbrowser.open("youtube.com")

        elif ('open google' in query) or ('google' in query):
            speak("opening the google !")
            speak("sir,what should i search in google")
            cm=takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif ('open stackoverflow' in query) or ('stackoverflow' in query):
            webbrowser.open("stackoverflow.com")   


        elif ('play music' in query) or ('music' in query):
            speak("dude! music is playing.... !")
            music_dir = 'C:\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif ('the time' in query) or ('time' in query):
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        
        
        elif ('open notepad' in query) or ('notepad' in query):
            speak("opening the notepad !")
            npath="C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
            
        elif ('open command prompt' in query) or ('command prompt' in query):
            speak("opening the Command prompt !")
            os.system("start cmd")
        
        elif ('open camera' in query) or ('camera' in query):
            speak('opening the camera')
            speak('press space to capture the picture')
            speak('press esc to close the camera')
            # press esc to close & space to click photo at current location
            cam = cv2.VideoCapture(0)

            cv2.namedWindow("test")
            img_counter = 0

            while True:
                ret, frame = cam.read()
                if not ret:
                    print("failed to grab frame")
                    break
                cv2.imshow("test", frame)
            
                k = cv2.waitKey(1)
                if k%256 == 27:
                    # ESC pressed
                    print("Escape hit, closing...")
                    break
                elif k%256 == 32:
                    # SPACE pressed
                    img_name = "opencv_frame_{}.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    print("{} written!".format(img_name))
                    img_counter += 1
            
            cam.release()
            
            cv2.destroyAllWindows()
    #elif 'where is' or 'mylocation' in query:
           # query = query.split(" ")
            #location = query[2]
            #speak("Hold on Ruchi, I will show you where " + location + " is.")
            #os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
            
        elif ('how are you' in query) or('how you being' in query) :
            speak("I am fine")
        elif ('hi'in query) or('hai'in query) or ('hey'in query) or ('hello' in query) :
            speak("Hello okay what can I help for u")

        elif ('ip address' in query) or ('ip' in query):
                ip = get('https://api.ipify.org').text
                print(f"your IP address is {ip}")
                speak(f"your IP address is {ip}")
          
        elif ('open facebook' in query) or ('facebook' in query):
            speak("opening the Facebook !")
            webbrowser.open("www.facebook.com")
            
            
        elif ('send message' in query) or ('whatsapp' in query) or ('send message to vivek' in query):
            kit.sendwhatmsg("+917984234520", "this is for testing",10,50)
            
        elif ('play songs on youtube' in query) or ('fav song on youtube' in query):
            kit.playonyt("kya mujhe pyar hai")
        
        elif ('translator' in query) or ('in hindi' in query) or('speak in hindi' in query):
            tran()
        elif ('microsoft teams' in query) or ('teams' in query):
            speak("opening the Microsoft teams !")
            teampath="C:\\Users\\ruchi\\AppData\\Local\\Microsoft\\Teams\\Update"
            os.startfile(teampath)
        elif ('word' in query) or ('Microsoft word' in query) or ('open word' in query):
            speak("opening the Microsoft word !")
            wordpath="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD"
            os.startfile(wordpath)
        elif ('powerpoint' in query) or ('microsoft powerpoint' in query ) or ('open powerpoint' in query):
            speak("opening the Microsoft powerpoint !")
            pointpath="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT"
            os.startfile(pointpath)
        elif ('code blocks' in query) or ('open codeblocks' in query) or ('codeblocks' in query):
            speak("opening the codeblocks !")
            blockpath="C:\\Program Files\\CodeBlocks\\codeblocks"
            os.startfile(blockpath)
        elif ('visual studio' in query)or('open studio' in query) or ('open visual studio' in query):
           speak("opening the Visualstudio !")
           studiopath="C:\\Users\\ruchi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code"
           os.startfile(studiopath)
        elif ('anaconda' in query) or ('conda' in query):
            speak("opening the Anaconda !")
            condapath="C:\\OneDriveTemp\\Anaconda\\pythonw"
            os.startfile(condapath)
            
        elif ('calculator' in query) or ('calc' in query) or ('cal' in query):
            speak("opening the calculator !")
            calpath="C:\\Windows\\System32\\calc.exe"
            os.startfile(calpath)
        
        elif 'email to vivek' in query:
            try:
                speak("What should I say?")
                content = takeCommand().lower()
                to = "ruchiparmar065@gmail.com"    
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("Sorry ,my friend . I am not able to send this email") 
        elif ('hotstar' in query) or ('open hotstar' in query):
            speak('opening your disney plus hotstar')
            webbrowser.open('https://www.hotstar.com/in')
        elif ('prime' in query) or ('open prime' in query):
            speak('opening your amazon prime videos')
            webbrowser.open('https://www.primevideo.com/')
        elif ('netflix' in query) or ('open netflix' in query):
            speak('opening Netflix videos')
            webbrowser.open('https://www.netflix.com/')
        elif 'close notepad' in query:
            speak("okay , closeing notepad!")
            os.system("taskkill /f /im notepad.exe")
        elif ('slides' in query) or ('open slides' in query):
            speak('opening your google slides')
            webbrowser.open('https://docs.google.com/presentation/')
        elif ('canva' in query) or ('open canva' in query):
            speak('opening your canva')
            webbrowser.open('https://www.canva.com/')
        elif ('github' in query) or ('open github' in query):
            speak('opening your github')
            webbrowser.open('https://github.com/')
        elif ('gitlab' in query) or ('open gitlab' in query):
            speak('opening your gitlab')
            webbrowser.open('https://gitlab.com/-/profile')
        elif ('play youtube' in query) or ('any song' in query) or ('search in youtube' in query):
            speak("okay can you please say what to search in youtube")
            search =takeCommand()
            if "play" in search:
                search = search.replace("play","")
            speak('playing '+search)
            print(f'playing {search}')
            kit.playonyt(search)
            print('playing')
        elif "download youtube video" in query:
            speak("okay please enter the youtube video link which you want to download")
            link = input("Enter the YOUTUBE video link: ")
            yt=YouTube(link)
            yt.streams.get_highest_resolution().download()
            speak(f"okay downloaded {yt.title} from the link you given into the main folder")
        elif ('edge' in query) or ('open edge' in query):
            speak('opening your Miscrosoft edge')
            os.startfile('..\\..\\MicrosoftEdge.exe')
        elif ('flipkart' in query) or ('open flipkart' in query):
            speak('Opening flipkart online shopping website')
            webbrowser.open("https://www.flipkart.com/")
        elif ('amazon' in query) or ('open amazon' in query):
            speak('Opening amazon online shopping website')
            webbrowser.open("https://www.amazon.in/")
        elif ('temperature' in query) or ('today temperature' in query):
            speak('the temperature is ')
            temperature()
            
        elif ('today schedule' in query) or ('schedule' in query):
            day = Cal_day().lower()
            speak("okay today's shedule is")
            Week = {"monday" : "okay from 9:00 to 9:50 you have python class, from 10:00 to 11:50 you have data structure class, from 12:00 to 2:00 you have brake, and today you have sensors lab from 2:00",
                    "tuesday" : "okay from 9:00 to 9:50 you have system analysis class, from 10:00 to 10:50 you have break,from 11:00 to 12:50 you have networking class, from 1:00 to 2:00 you have brake, and today you have python lab from 2:00",
                    "wednesday" : "okay today you have a full day of classes from 9:00 to 10:50 you have Data structures class, from 11:00 to 11:50 you have advance database class, from 12:00 to 12:50 you have data structure class, from 1:00 to 2:00 you have brake, and today you have Data structures lab from 2:00",
                    "thrusday" : "okay today you have a full day of classes from 9:00 to 10:50 you have Maths class, from 11:00 to 12:50 you have networking class, from 1:00 to 2:00 you have brake, and today you have advance database lab from 2:00",
                    "friday" : "okay today you have a full day of classes from 9:00 to 9:50 you have Biology class, from 10:00 to 10:50 you have data structures class, from 11:00 to 12:50 you have Elements of computing class, from 1:00 to 2:00 you have brake, and today you have Electronics lab from 2:00",
                    "saturday" : "okay today you have a full day of classes from 9:00 to 11:50 you have maths lab, from 12:00 to 12:50 you have english class, from 1:00 to 2:00 you have brake, and today you have elements of computing lab from 2:00",
                    "sunday":"okay today is holiday but we can't say anything when they will bomb with any assisgnments"}
            if day in Week.keys():
                speak(Week[day])
        elif 'your name' in  query:
            speak("My name is jarvis")
        elif 'my name' in query:
            speak("your name is Ruchi")
        elif 'university name' in query:
            speak("you are studing in charusat university, pursuing bachelors in computer application ") 
        elif 'what can you do' in query:
            speak("I speak with you until you want to stop, I can say time, open your social media accounts,your open source accounts, open google browser,and I can also open your college websites, I can search for some thing in google and I can tell jokes")
        elif 'your age' in query:
            speak("I am very young that u")
        elif 'date' in query:
            speak('Sorry not intreseted, I am having headache, we will catch up some other time')
        elif 'are you single' in query:
            speak('No, I am in a relationship with wifi')
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'are you there' in query:
            speak('Yes , I am here')
        elif 'gmail' in query:
            speak('opening your google gmail')
            webbrowser.open('https://mail.google.com/mail/')
        elif ' google maps' in query:
            speak('opening google maps')
            webbrowser.open('https://www.google.co.in/maps/')
        elif 'google news' in query:
            speak('opening google news')
            webbrowser.open('https://news.google.com/')
        elif 'google calender' in query:
            speak('opening google calender')
            webbrowser.open('https://calendar.google.com/calendar/')
        elif 'google photos' in query:
            speak('opening your google photos')
            webbrowser.open('https://photos.google.com/')
        elif 'google documents' in query:
            speak('opening your google documents')
            webbrowser.open('https://docs.google.com/document/')
        elif 'google spreadsheet' in query:
            speak('opening your google spreadsheet')
            webbrowser.open('https://docs.google.com/spreadsheets/')   
        elif 'close calculator' in query:
            speak("okay , closeing calculator!")
            os.system("taskkill /f /im calc.exe")
        elif 'close powerpoint' in query:
           speak("okay , closeing powerpoint!")
           os.system("taskkill /f /im POWERPNT")
        elif 'close word' in query:
            speak("okay , closeing word!")
            os.system("taskkill /f /im WINWORD")
        elif 'close microsoft teams' in query:
            speak("okay , closeing Microsoft teams!")
            os.system("taskkill /f /im Update")
        elif 'close visual studio' in query:
           speak("okay , closeing visual studio!")
           os.system("taskkill /f /im Code")
        elif 'close anaconda' in query:
           speak("okay , closeing anaconda!")
           os.system("taskkill /f /im pythonw")
        elif ('shutdown the system' in query) or ('down the system' in query):
                speak("okay shutting down the system in 10 seconds")
                time.sleep(10)
                os.system("shutdown /s /t 5")
        elif ("you can sleep" in query) or ("sleep now" in query):
                speak("Okay okay, I am going to sleep you can call me anytime.")
                break
            #command for waking the jarvis from sleep
            #jarvis wake up
        elif ("wake up" in query) or ("get up" in query):
                speak("okay, I am not sleeping, I am in online, what can I do for u")
        elif 'send email' in query:
                verifyMail()
            #command for checking the temperature in surroundings
            #jarvis check the surroundings temperature
        elif "temperature" in query:
                temperature()
            #command for checking internet speed
            #Eg: jarvis check my internet speed
        elif "internet speed" in query:
                InternetSpeed()
            #command if you don't want the JARVIS to spack until for a certain time
            #Note: I can be silent for max of 10mins
            # Eg: JARVIS keep quiet for 5 minutes 
        elif ('silence' in query) or ('silent' in query) or ('keep quiet' in query) or ('wait for' in query) :
                silenceTime(query)
           #command for restarting the system
            #Eg: jarvis restart the system
        elif ('restart the system' in query) or ('restart' in query):
                speak("Boss restarting the system in 10 seconds")
                time.sleep(10)
                os.system("shutdown /r /t 5")
            #command for make the system sleep
            #Eg: jarvis sleep the system
        elif ('sleep the system' in query) or ('sleep' in query):
                speak("Boss the system is going to sleep")
                os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")
           #Command for reading PDF
            #EG: Jarvis read pdf
        elif ("read pdf" in query) or ("pdf" in query):
                pdf_reader()
                '''
        elif ("covid" in query) or  ("corona" in query):
                speak("Boss which state covid 19 status do you want to check")
                s = takeCommand()
                Covid(s)
                '''
        elif ('system condition' in query) or ('condition of the system' in query):
                speak("checking the system condition")
                condition()
        elif ('take screenshot' in query)or ('screenshot' in query) or("take a screenshot" in query):
                scshot()
       
        elif ("volume mute" in query) or ("mute the sound" in query) :
                speak('muting the sound')
                pyautogui.press("volumemute")
                speak('volume muted')
        elif ("volume down" in query) or ("decrease volume" in query):
                pyautogui.press("volumedown")
                speak('volume decreased')
          #command for searching for a procedure how to do something
            #Eg:jarvis activate mod
            #   jarvis How to make a cake (or) jarvis how to convert int to string in programming 
        elif "activate mod" in query:
                How()
            #command for increaing the volume in the system
            #Eg: jarvis increase volume
        elif ("volume up" in query) or ("increase volume" in query):
                pyautogui.press("volumeup")
                speak('volume increased')
        elif ('where i am' in query) or ('where we are' in query):
                location()
        elif ('yes' in query) or ('yup' in query) or ('yeah' in query):
            speak("ok friend what should i do")
        elif ('tell me news' in query) or ("the news" in query) or ("todays news" in query):
                speak("Please wait boss, featching the latest news")
                news()
            #Command for opening an instagram profile and downloading the profile pictures of the profile
            #Eg: jarvis open a profile on instagram 
        elif ('instagram profile' in query) or("profile on instagram" in query):
                Instagram_Pro()
        elif ('instagram' in query) or ('open instagram' in query):
            speak('opening your instagram')
            webbrowser.open('https://www.instagram.com/')
        elif ('twitter' in query) or ('open twitter' in query):
            speak('opening your twitter')
            webbrowser.open('https://twitter.com/Suj8_116')
        elif ('discord' in query) or ('open discord' in query):
            speak('opening your discord')
            webbrowser.open('https://discord.com/channels/@me') 
            '''
        elif 'how is the weather' and 'weather' in query:

            url = 'https://api.openweathermap.org/'#Open api link here

            res = requests.get(url)

            data = res.json()

            weather = data['weather'] [0] ['main'] 
            temp = data['main']['temp']
            wind_speed = data['wind']['speed']

            latitude = data['coord']['lat']
            longitude = data['coord']['lon']

            description = data['weather'][0]['description']
            speak('Temperature : {} degree celcius'.format(temp))
            print('Wind Speed : {} m/s'.format(wind_speed))
            print('Latitude : {}'.format(latitude))
            print('Longitude : {}'.format(longitude))
            print('Description : {}'.format(description))
            print('weather is: {} '.format(weather))
            speak('weather is : {} '.format(weather))
            '''
        elif 'it\'s my birthday today' in query:
            print(" Wow! Wish you a very Happy Birthday")
            speak(" Wow! Wish you a very Happy Birthday")
    
        elif ("where is" in query) or ('current location' in query):
            data = query.split(" ")
            location = data[2]
            speak("Hold on, I will show you where " + location + " is.")
            os.system('cmd /k "start chrome https://www.google.nl/maps/place/"'+ location)
        elif 'remember that' in query:
            speak("what should i remember sir")
            rememberMessage = takeCommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif ('do you remember anything' in query) or ('remember anything' in query):
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())
            
            
       # elif 'dictionary' in query:
            #speak('What you want to search in your intelligent dictionary?')
            #translate(takeCommand())
       # elif 'my news' in query:
        #    speak('Ofcourse sir..')
         #   speak_news()
          #  speak('Do you want to read the full news...')
           # test = takeCommand()
            #if 'yes' in test:
             #   speak('Ok Sir, Opening browser...')
              #  webbrowser.open(getNewsUrl())
               # speak('You can now read the full news from this website.')
            #else:
             #   speak('No Problem Sir')
         
        elif ("switch the window" in query) or ("switch window" in query) or ('window' in query):
                speak("Okay sir, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")  
        elif ("track" in query) or ("track a mobile number" in query):
            track()
     
        elif ('no thanks' in query) or ('no' in query):
            speak("thank you! sir goodbyie have a nice day")
            sys.exit()
            
        elif ("goodbye" in query) or ("get lost" in query) or ('by' in query) or ('talk to you later' in query):
                speak("Thanks for using me , have a good day")
                sys.exit()
        speak("sir,do you want any other work")
    
    
         