import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
        
    elif hour>=12 and hour<18:
        speak("good afternoon")
            
    else:
        speak("good evening")    
    speak("i am mahendra  .please tell me how may i help you")    
    
def takecommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("listning...")
        r.pause_threshold = 1
        audio=r.listen(source)
        
    try:
        print("recagnizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
        
    except Exception as e:
        #print(e)    
        
        print("say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mahendramane243@gmail.com','Shree@1920') 
    server.sendmail('mahendramane243@gmail.com', to,content) 
    server.close()  
        
            
if __name__ =='__main__':
    WishMe()
    if 1: 
        query=takecommand().lower()
        
        # logic for exicuting tasks based on quary
        
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
         
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")    
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
    
        elif 'play music' in query:
            music_dir="D:\\Quick Share"
            songs=os.listdir(music_dir) 
            os.startfile(os.path.join(music_dir, songs[0])) 
            
            
        elif 'the time' in query:
            strtime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime}")
            
        elif 'open code'in query:
            codepath="C:\\Users\\Prime\\AppData\\Local\\Programs\\Microsoft VS Code"
            os.startfile(codepath)
            
        elif 'email to mahendra' in query:
            
            try:
                speak("what should i say ")    
                content=takecommand()
                to="mahendramane243@gmail.com"
                sendEmail(to, content)
                speak("Email has been send")
            except Exception as e:
                print(e)
                speak("sorry i am not able to send this email")    
                
        elif 'open LinkedIn' in query:
            webbrowser.open("https://www.linkedin.com/")       
            
               
         
    
