'''
0)setting up the voice----> pyttsx3---->datetime
1)voice input
2)recognise ----> speech_recognition----->wikipedia
3)translate the command
4)output -----> webbrowser
'''
import smtplib

import pyttsx3  #pyttsx3 is a text-to-speech conversion library in Python
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import requests
import json
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pyjokes import pyjokes
import imdb
from bs4 import BeautifulSoup


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')      #getting details of current voice
engine.setProperty('voice',voices[1].id)   # setting the voice

#voices[0].id means voices at zeroth index i.e David desktop
#voices[1].id means voices at first index i.e Zira desktop

def speak(audio):
    engine.say(audio)
    engine.runAndWait() #Blocks while processing all currently queued commands.
    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("This is Nazi, your voice assistant,how can i help you!")
    


def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5  #optional
        audio = r.listen(source) # to listen the audio

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #this is google search engine
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        takeCommand()
        return "None"
    return query


if __name__ == '__main__':
    assname = 'Nazi'

    wishMe()

    if True:
        query = takeCommand().lower()    #converting to lowercase
        #logic for executing task based on query

        if 'wikipedia' in query:  #if wikipedia is there in query then the search will go
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")  #removing wikipedia from query
            results = wikipedia.summary(query,sentences = 2)  #.summary is used to return the summary of the information
            print(results)
            speak(results)

        elif 'youtube' in query or 'YouTube' in query:
            speak("okay..")
            import webbrowser
            
            webbrowser.open('https://www.youtube.com')

        elif 'code' in query:
            speak("okay..")
            codePath = "C:\\Users\\91937\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'google' in query:
            speak("okay..")
            webbrowser.open("https://www.google.co.in/")

        elif 'open stack overflow' in query:
            speak("okay..")
            webbrowser.open("https://stackoverflow.com/")

        elif 'play music' in query:
            webbrowser.open("spotify")

        elif 'time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S") 
            print(f"sir, the time is {str_time}")

        elif 'codewithharry' in query:
            webbrowser.open("https://www.youtube.com/watch?v=Lp9Ftuq2sVI&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=121")

        elif 'gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/2/#inbox")

        elif 'linkedin' in query:
            webbrowser.open("https://www.linkedin.com/in/pradumnya-ghadole-0578341a0/")

        elif 'github' in query or 'GitHub' in query:
            webbrowser.open("https://github.com/")

        elif 'shopping' in query:
            webbrowser.open("https://www.flipkart.com/?s_kwcid=AL!739!3!260704327909!e!!g!!flipkart&gclsrc=aw.ds&&semcmpid=sem_8024046704_brand_eta_mobile_goog&gclid=CjwKCAjwgr6TBhAGEiwA3aVuIRLab89DIxig_u1O0F81fEa_5DZbsZIkdFVUaxy6RvgxDpSOEwY0XhoCcCsQAvD_BwE")

        elif 'superset' in  query:
            webbrowser.open("https://joinsuperset.com/")

        elif 'movie information' in query:
            hr = imdb.IMDb()
            speak("Which movie information do you want to search")
            movie_name = input("Enter the movie name: ")
            speak(f"Searching information about {movie_name}")
            movies = hr.search_movie((str(movie_name)))
            index = movies[0].getID()
            movie = hr.get_movie(index)
            title = movie['title']
            year = movie['year']
            cast = movie['cast']
            list_of_cast = ','.join(map(str,cast))

            speak(f"Title of the movie, {title}")
            print(f"Title of the movie, {title}")

            speak(f"year of release, {year}")
            print(f"year of release, {year}")

            speak(f"full cast, {list_of_cast}")
            print(f"full cast, {list_of_cast}")


        elif 'email to pradumnya' in query or 'email to pradyumna' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = "pradumnyaghadole9@gmail.com"
                send_mail('pradumnyacoder9@gmail.com',to,'test mail',content)
                speak('email has been sent')
            except Exception as e:
                print(e)
                speak("I'm not able to send mail!")
                
                
        elif 'todays weather' in query:
            
                search = "weather in nagpur"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"current {search} is {temp}")


        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whom should i send")
                to = input()
                send_mail('pradumnyacoder9@gmail.com', to, 'Zira Send this mail', content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "what's your name" in query or "what is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif 'exit' in query:
            speak('thanks for giving me your time')

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Pradyumna Ghadole.")

        # elif 'joke' or 'tell me a joke' in query:
        #     joke = pyjokes.get_joke('en','neutral');
        #     speak(joke)
        #     print(joke)

        elif 'power point presentation' in query or 'open PPT' in query or 'PPT' in query:
            speak('opening the power point presentation')
            power = "C:\\Users\\91937\\Downloads\\final_ppt_4"
            os.startfile(power)

        elif 'what is love' in query:
            speak("It is 7th sense that destroy all the other senses")

        elif 'reason for you' in query or 'purpose' in query:
            speak("Well !!, I was created as a project phase 1 by Mister Pradumnya but he wished to continue me in the term 2 as well!")

        elif 'news' in query:
            speak("News for today.. Lets begin")
            url = "http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=2ed8f8de46364c4bbfc28bf019db0f77"
            news = requests.get(url).text
            news_dict = json.loads(news)  # json.loads() takes a string and convert it to a python object
            arts = news_dict['articles']  # this is used just to read the article

            for article in arts:
                speak(article['title'])
                print(article['title'])
                speak("Next news is..")

            speak("Thanks for listening...")
            
        elif 'how are you'in query:
            speak("Better than I was a minute ago !!, because you are here now")
        
        
        else:
            speak("Sorry to say, but I cant search that")
            print("Sorry to say, but I cant search that")



  
