import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as speech
import smtplib


eng = pyttsx3.init('sapi5')
voices = eng.getProperty('voices')
eng.setProperty('rate',200)
eng.setProperty('voice',voices[1].id)


def talk(sentence):
    eng.say(sentence)
    eng.runAndWait()

def greeting():
    hr = int(datetime.datetime.now().hour)
    if hr>=0 and hr<12:
        talk("Good Morning Miss Aditi. I am Anna, How may I be of Assistance?")
    elif hr>=12 and hr<16:
        talk("Good Afternoon Miss Aditi. I am Anna, How may I be of Assistance?")
    else:
        talk("Good Evening Miss Aditi. I am Anna, How may I be of Assistance?")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('SENDER_EMAIL_ID', 'PASSWORD')
    server.sendmail('SENDER_EMAIL', to, content)
    server.close()



def command():
    #Speech to text(String)
    r = speech.Recognizer()
    with speech.Microphone() as src:
        print("Listening..")
        r.pause_threshold = 1   #non speaking time
        audio = r.listen(src)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:",query)
    except Exception as e:
        print(e)
        print("Say that again Please")
        return "None"
    return query

if __name__ == "__main__":
    greeting()
    while True:
      query = command().lower()

      #Executing tasks based on input
      if 'wikipedia' in query:
          talk('Searching Wikipedia...')
          query = query.replace("wikipedia","")
          result = wikipedia.summary(query,sentences=2)
          talk("According to wikipedia,")
          talk(result)

      elif 'open youtube' in query:
          webbrowser.open("youtube.com")

      elif 'open google' in query:
          webbrowser.open("google.com")

      elif 'open stackoverflow' in query:
          webbrowser.open("stackoverflow.com")

      elif 'play music' in query:
          dirm = 'E:\\Songs'  #add path to directory with music in it
          songs = os.listdir(dirm)
          os.startfile(os.path.join(dirm,songs[0]))

      elif 'the time' in query:
          startTime = datetime.datetime.now().strftime("%H:%M:%S")
          talk (f" The time is {startTime}")

      elif 'open discord' in query:
          codepath = "PATH_TO WHERE DISCORD IS INSTALLED"
          os.startfile(codepath)

      elif 'send email' in query:
          try:
              talk("What should I say?")
              content = command()
              to = 'RECEIVER EMAIL'
              sendEmail(to,content)
              talk("Email has been sent!")
          except Exception as e:
              print(e)
              talk("Some Error Occured. Not able to send email at the moment")

      elif 'quit' in query:
          talk("Closing Interface. Have a good day Miss Aditi.")
          break



