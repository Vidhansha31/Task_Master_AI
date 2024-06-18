import datetime
import operator
import os
import random
import smtplib
import sys
import time
import webbrowser
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import PyPDF3
import cv2
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit as kit
import requests
import speech_recognition as sr
import speedtest
import wikipedia
import psutil
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
from requests import get

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180-200)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
    try:
        print("recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "none"
    return query


def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    # print(hour)
    if hour <= 0 and hour < 12:
        speak(f"Good Morning Sir, its{tt}")
    elif hour > 12 and hour <= 15:
        speak(f"Good Afternoon Sir, its{tt}")
    else:
        speak(f"Good Evening Sir, its{tt}")
    speak("Your Assistant is here...What are the Tasks for today ?")


# def sendEmail(to, content):
#         try:
#             server = smtplib.SMTP('smtp.gmail.com', 587)
#             #server.ehlo()
#             server.starttls()
#             email_address = "vidhan31102002@gmail.com"
#             password = "kvmf cowa sawp tjok"
#             server.login(user=email_address, password=password)
#             server.sendmail(email_address, to, content)
#             # server.close()
#             server.quit()
#         except SMTPAuthenticationError as e:
#             print(f"SMTP Authentication Error: {e}")
#             print("Make sure your email and password are correct, and less secure apps access is enabled.")
#
#         except Exception as e:
#             print(f"An error occurred: {e}")

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=5855b5c5fe054f2188a08c31380034e9'

    main_page = requests.get(main_url).json()
    print(main_page)
    articles = main_page["articles"]
    print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f" todays {day[i]} news is:  {head[i]}")


def pdf_reader():
    book = open('C:\\Users\\Dell\\PycharmProjects\\AI\\Semester Registration Form (1).pdf', 'rb')
    pdfReader = PyPDF3.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number in this book are{pages} ")
    speak("sir please enter the page number which i have to read")
    pg = int(input("please enter the page number: "))
    if pg < 0 or pg >= pages:
        speak("Invalid page number. Please enter a valid page number.")
        return
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)


def seacrh_wikihow(how, max_results):
    pass


if __name__ == '__main__':
    wish()
    # takecommand()
    # speak("hello Sir you are too good")
    while True:
        if 1:
            query = takecommand().lower()

            if "open notepad" in query:
                speak("ok sir, opening Notepad")
                npath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)
            elif "open excel" in query:
                speak("Opening....sir" )
                npath = "C:\\WINDOWS\\system32\\excel.exe"
                os.startfile(npath)

            elif "close notepad" in query:
                speak("Ok sir....closing notepad")
                os.system("TASKKILL /F /IM notepad.exe")

            elif "how are you" in query:
                speak("I am good sir , thanks for asking")

            elif "open command prompt" in query:
                speak("Ok sir, Opening command prompt")
                os.system("start cmd")

            elif "close command prompt" in query:
                speak("Ok sir....closing command prompt ")
                os.system("taskkill /F /IM cmd.exe")


            # elif "set alarm" in query:
            #     nn = int(datetime.datetime.now().hour)
            #     if nn == 0:
            #         music_dir = 'E:\\music'
            #         song = os.listdir(music_dir)
            #         os.startfile(os.path.join(music_dir, song[0]))

            elif "set alarm" in query:
                speak("Please specify the hour for the alarm (in 24-hour format)")
                alarm_hour = int(input("Please specify the hour for the alarm (in 24-hour format): "))
                speak("Please specify the minute for the alarm")
                alarm_minute = int(input("Please specify the minute for the alarm: "))
                speak("I have setted the alarm")


                while True:
                    current_time = datetime.datetime.now()
                    if current_time.hour == alarm_hour and current_time.minute == alarm_minute:
                        music_dir = 'E:\\music'
                        song = os.listdir(music_dir)
                        os.startfile(os.path.join(music_dir, song[0]))
                        break


            elif "open camera" in query:
                speak("press Escape key to close the camera")
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(10)
                    if k == 27:
                        break
                cap.release()
                cv2.waitKey(5)
                cv2.destroyAllWindows()

            # elif "do some calculation" in query:
            #     r = sr.Recognizer()
            #     with sr.Microphone() as source:
            #         print("listening...")
            #         r.adjust_for_ambient_noise(source)
            #         audio = r.listen(source, timeout=5, phrase_time_limit=5)
            #     try:
            #         print("recognizing")
            #         my_string = r.recognize_google(audio, language='en-in')
            #         print(f"user said: {query}")
            #
            #
            #         def get_operator_fn(op):
            #             return {
            #                 '+': operator.add,
            #                 '-': operator.sub,
            #                 '*': operator.mul,
            #                 'divided': operator.truediv,
            #             }[op]
            #
            #
            #         def reval_binary_expr(op1, oper, op2):
            #             op1, op2 = int(op1), int(op2)
            #             return get_operator_fn(oper)(op1, op2)
            #
            #
            #         speak("Your Result is")
            #         speak(reval_binary_expr(*(my_string.split())))
            #     except Exception as e:
            #         print(e)
            #         speak("Sorry, I couldn't understand that.")

            elif "do some calculation" in query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("OK what do want to calculate :Exammple 3 pus 3")
                    print("listening...")
                    r.adjust_for_ambient_noise(source)
                    # r.pause_threshold = 1
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                try:
                    print("recognizing")
                    my_string = r.recognize_google(audio, language='en-in')
                    print(f"user said: {query}")


                    def get_operator_fn(op):
                        return {
                            '+': operator.add,  # plus
                            '-': operator.sub,  # minus
                            '*': operator.mul,  # multiply by
                            'devided': operator.__truediv__,  # devided
                        }[op]


                    def reval_binary_expr(op1, oper, op2):
                        op1, op2 = int(op1), int(op2)
                        return get_operator_fn(oper)(op1, op2)


                    speak("Your Result is")
                    speak(reval_binary_expr(*(my_string.split())))

                except Exception as e:
                    print(e)
                    speak("Sorry, I couldn't understand that.")





            # not needed code
            elif "close camera" in query:
                speak("Ok sir....closing Camera ")
                os.system("taskkill /F /IM CameraApp.exe")

            elif "play music" in query:
                music_dir = "E:\\music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))

            # to be checked
            elif "stop music" in query:
                os.system("taskkill /F /IM vlc.exe")


            elif "what is current temperature" in query:
                search = "Temperature in bangalore"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current {search} is {temp}")


            elif "what is my ip address" in query:
                ip = get('https://api.ipify.org').text
                speak(f"Your ip address is{ip}")

            elif "wikipedia" in query:
                speak("Searching wikipedia")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
                print(results)


            elif "open youtube" in query:
                webbrowser.open("youtube.com")

            # to be checked
            #     chrome_path = "C:\Program Files\Google\Chrome\Application"
            # elif "open youtube" in query:
            #
            #     url = "https://www.youtube.com"
            #     webbrowser.get(chrome_path).open(url)
            #    # webbrowser.open("youtube.com")

            elif "open google" in query:
                speak("Sir, what should i search on google")
                cm = takecommand().lower()
                webbrowser.open(f"{cm}")
            # to be checked
            elif "open stack overflow" in query:
                webbrowser.open("stackoferflow.com")
            # to be checked
            elif "open geeks for geeks" in query:
                webbrowser.open("geeksforgeeks.org.com")
            # to be checked
            elif "send message" in query:
                kit.sendwhatmsg("+916260419871", "AI is sending this message", 15, 1)

            elif "play my favourite song" in query:
                kit.playonyt("One love")

            elif "activate how to do mod" in query:
                speak("How to do Mode is activated")
                while True:
                    speak("Please tell me what do you want to know")
                    how = takecommand()
                    try:
                        if "exit" in how or "close" in how:
                            speak("okay sir,exited How to do mode")
                            break
                        else:
                            max_results = 1
                            how_to = search_wikihow(how, max_results)
                            assert len(how_to) == 1
                            how_to[0].print()
                            speak(how_to[0].summary)
                    except Exception as e:
                        print(e)
                        speak("Sorry sir , i am not able to find this")

            elif "send email" in query:
                speak("what to write in email sir")
                query = takecommand().lower()
                if "send a file" in query:
                    try:
                        email_address = 'vidhan31102002@gmail.com'
                        password = 'kvmf cowa sawp tjok'
                        send_email_to = 'vidhan9848@gmail.com'
                        speak("ok sir, what will be the subject for this email")
                        query = takecommand().lower()
                        subject = query
                        speak("and sir , what to write in email")
                        query2 = takecommand().lower()
                        message = query2
                        speak("sir please enter the correct path of the file into the shell")
                        file_location = "F:\\KIA.docx"
                        input("please enter the path here")
                        file_location = input("please enter the path here: ")
                        speak("please wait sir, i am sending the email now")

                        msg = MIMEMultipart()
                        msg['From'] = email_address
                        msg['To'] = send_email_to
                        msg['Subject'] = subject

                        msg.attach(MIMEText(message, 'plain'))

                        filename = os.path.basename(file_location)
                        attachment = open(file_location, "rb")
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition', 'attachment; filename="%s"' % filename)

                        msg.attach(part)

                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(email_address, password)
                        text = msg.as_string()
                        server.sendmail(email_address, send_email_to, text)
                        server.quit()
                        speak("email has been sent with the file attached to it")
                    except Exception as e:
                        print(e)
                        speak(f"Sorry sir not able to send email with file because {e}")

                else:
                    email_address = 'vidhan31102002@gmail.com'
                    password = 'kvmf cowa sawp tjok'
                    send_email_to = 'nandinirathod3562@gmail.com'
                    message = query

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email_address, password)
                    server.sendmail(email_address, send_email_to, message)
                    server.quit()
                    speak("email has been sent without any file attached to it")

            #     try:
            #         speak("What to write in email...sir")
            #         content = takecommand().lower()
            #         to = "vidhi1950@gmail.com"
            #         sendEmail(to, content)
            #         speak("Done Sir,Email has been sent")
            #
            # except Exception as  e:
            #     print(e)
            #     speak("Sorry sir, i am not able to send this Email")
            # to be checked
            elif "crack a joke" in query:
                joke = pyjokes.get_jokes()
                if joke:
                    joke = random.choice(joke)
                    speak("Here it is...!")
                    speak(joke)
                else:
                    speak("Sorry i did'nt found any joke")


            elif "shut down the system" in query:
                speak("Bye Sir......")
                os.system("shutdown /s /t 5")

            elif "restart the system" in query:
                speak("Ok sir , Restarting")
                os.system("shutdown /r /t 5")

            elif "turn on the sleep mode" in query:
                speak("Ok sir, turning onn")
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            # elif "switch the window" in query:
            #     speak("switching...sir")
            #     pyautogui.keyUp("alt")
            #     pyautogui.press("tab")
            #     time.sleep(1)
            #     pyautogui.keyUp("alt")

            elif "switch the window" in query:
                speak("switching...sir")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif"what is my current location"in query:
                speak("Wait sir let me check it through our ip address")
                try:
                    ipadd = requests.get('https://api.ipify.org').text
                    print(ipadd)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipadd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(f"Sir i am not sure but i think we are in {city} city and {country} Country")
                except Exception as e:
                    speak("Sorry sir i am not able to fetch our location")
                    print(e)
                    pass


            elif "tell me top news for today" in query:
                speak("Ok sir, fetching the latest news")
                news()
            # to be checked
            elif "take a screenshot" in query:
                speak("Sir please tell me the name of this screenshot file")
                name = takecommand().lower()
                speak("Please hold the screen for a few minutes i am taking the screen shot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("Screenshot taken and saved as {}.png".format(name))
                speak("I am done sir the screen shot is taken")

            elif "read pdf" in query:
                pdf_reader()

            elif"what is the battery percentage" in query:
                import psutil
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"Sir the battery percentage is {percentage}")
                if percentage<=75:
                    speak("We have enough power to work")
                elif percentage>=75 and percentage<50:
                    speak("You Should look for the charger")
                elif percentage>=50 and percentage< 20:
                    speak("The system will shut down very soon charge it son")
                elif percentage<10:
                    speak("The system is getting shut down")


            elif"what is the internet speed" in query:
                st = speedtest.Speedtest()
                d1 =st.download()
                up = st.upload()
                speak(f"Sir you are having {d1} bits per seconds as download speed and {up} bits per second as our upload speed")

            #This is a another way to get the internet speed in mbps
            # elif"internet speed" in query:
            #     try:
            #         os.system('cmd /k "speedtest"')
            #     except:
            #         print("there is no internet connection")
            #         speak("there is no internet connection")


            elif"send text message" in query:
                speak("Sir what should i say")
                msz = takecommand()

                from twilio import Client

            elif "you can sleep now" in query:
                speak("Thankyou Sir..., have a good day")
                sys.exit()

        speak(" sir,...Do you have any other tasks ??")
