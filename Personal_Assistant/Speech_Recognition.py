#Making the computer speak using pyttsx
import time
import requests
import json
import os
import sys
import pyttsx3 as ps
st = ps.init()
st.say("Hello!! It's a pleasure to speak with you! My name is Witty J and I am here for you in the good and the bad times. I was created by Lucas Mantovani to help you. Please tell me your name (in one word)")
st.runAndWait()

###############
import requests
import json
from Custom_audio import record_audio, read_audio

# Wit speech API endpoint
API_ENDPOINT = 'https://api.wit.ai/speech'

# Wit.ai api access token
wit_access_token = input('Enter your wit.ai access token: ') #Wit.AI Access token


def RecognizeSpeech(AUDIO_FILENAME, num_seconds = 5):
    
    # record audio of specified length in specified audio file
    record_audio(num_seconds, AUDIO_FILENAME)
    
    # reading audio
    audio = read_audio(AUDIO_FILENAME)
    
    # defining headers for HTTP request
    headers = {'authorization': 'Bearer ' + wit_access_token,
               'Content-Type': 'audio/wav'}

    # making an HTTP post request
    resp = requests.post(API_ENDPOINT, headers = headers,
                         data = audio)
    
    # converting response content to JSON format
    data = json.loads(resp.content)
    
    # get text from data
    words = data['_text']
    
    # return the text
    return words
#Get spoken words in a variable named "words"
words =  RecognizeSpeech('myspeech.wav', 4)

def speech(text,x):
    global st
    st.say(text+x)
    st.runAndWait()
print([words])
speech("It is a pleasure to meet you...",words)
name = words
intro = True
rec = False #Checks if program recognizes what user is speaking. If true, becomes "True".


def weather():
    b=''
    speech('Please give me the name of a  city, or say weather to manually insert a city. Say quit or exit to exit the weather giver',b)
    weather_words =  RecognizeSpeech('myspeech.wav', 4)
    print([weather_words])
    if weather_words=="quit" or weather_words=="exit":
        Speaking()
    if weather_words=="weather":
        try:
            inserted_city = str(input("For what city chould I give the weather?"))
            w_api = input('Enter your openweathermap API access key: ')
            u = "http://api.openweathermap.org/data/2.5/weather?appid="+w_api"="+inserted_city
            myrequest=requests.get(u).json()
            speech("Weather:" +str(myrequest['weather'][0]['main']))
            speech("Current temperature at the location is:"+ str(myrequest['main']['temp'])+", with a minimum of "+str(myrequest['main']['temp_min'])+" and a maximum of " + str(myrequest['main']['temp_max'])+ " degrees Fahrenheit",b)
            print("Weather:" +str(myrequest['weather'][0]['main']))
            print("Current temperature at the location is:"+ str(myrequest['main']['temp'])+", with a minimum of "+str(myrequest['main']['temp_min'])+" and a maximum of " + str(myrequest['main']['temp_max'])+ " degrees Fahrenheit",b)
            Speaking()
        except:
            speech("Error trying to find the weather at the specified location",b)
            weather()
                    
    else:
        try:
            u = "http://api.openweathermap.org/data/2.5/weather?appid=ec972895a37915ff5740e238cdb16b8c&q="+weather_words
            myrequest=requests.get(u).json()
            print([weather_words])
            speech("Weather:" +str(myrequest['weather'][0]['main']),b)
            speech("Current temperature at the location is:"+ str(myrequest['main']['temp'])+", with a minimum of "+str(myrequest['main']['temp_min'])+" and a maximum of " + str(myrequest['main']['temp_max'])+ " degrees Fahrenheit",b)
            print("Weather:" +str(myrequest['weather'][0]['main']))
            print("Current temperature at the location is:"+ str(myrequest['main']['temp'])+", with a minimum of "+str(myrequest['main']['temp_min'])+" and a maximum of " + str(myrequest['main']['temp_max'])+ " degrees Fahrenheit")
            Speaking()
        except:
            speech("Error trying to find the weather at the specified location",b)
            weather()
            
def openfile(file):
    try:
        os.startfile(file)
    except:
        pass
def closefile(file):
    try:
        os.system('TASKKILL /F /IM'+file[-3]+file[-2]+file[-1])  ##Terminates all files of the specified type. (Ex: allbats, all pys)
    except:
        pass


def Speaking():
    global name
    global intro
    if intro is False:
        speech("Talk to me!",name+"!")
    else:
        speech("What would you like to talk about",name+"?")
        speech("Say,'sports','weather',love or politics, whatever you like. To change the way I call you, say name","")
        intro = False

    words =  RecognizeSpeech('myspeech.wav', 4)
    text = words
    words=list(words.split(" "))
    print(words)
    b="" ##"blank' variable, to satisfy the number of arguments needed by the 'speech' function
    ##"words" is now a list with the words spoken by the user as its elements
    for element in words:
        if element=="":  #If user says nothing, program restarts
            Speaking()
        if element =="write" or element=="text":
            y = str(input("Type what you want me to say:"))
            speech(y,b)
            Speaking()
        if element=="date" or element=="time" or element=="day" or element=="hour" or element=="minute" or element=="second" or element=="hours" or element=="minutes" or element=="seconds":
            timy1 =time.strftime('Time: %H:%M:%S')
            months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
            day = time.strftime('%d')
            month = time.strftime('%m')
            year = time.strftime('%y')
            timy2 = time.strftime('Date:'+ day+"/"+month+"/"+year)
            speech(timy1,b)
            formaty="Today is "+months[int(month)-1]+"{} , {}.".format(day,"20"+year)
            speech(formaty,b)
            print(timy1)
            print(timy2)
            ##Gives date
            Speaking()
        if element=="weather": #Gives weather conditions
           weather()         
        if element=="code" or element=="programming" or element=="computer": ##Talks about code
            speech("Coding is something I like to talk about. I was born through code","when I was programmed by Lucas Mantovani in his bedroom in Vicosa, Brazil",b)
            Speaking()
        if element=="sports": #Talks about sports
            speech("I cheer for the greatest team in Brazil, Cruzeiro. I also appreciate the Green Bay Packers!",b)
            Speaking()
        if element =="family": #Talks about my family
            speech("I love my creator's family. Especially Hila,May and Race Boy. Although I do not like it when Race tries to be lonely, sad and desperate with his guitar. I will miss them all when I leave, because I care for them deeply. i don't feel bad for criticizing Artic Monkeys. They suck. But I am sorry for all the times I disturbed May and for the moments in which I bothered hila for his covers. seriously, you mean the world to me. Signed, Lucas MANTOVANI",b)
            time.sleep(10)
            Speaking()
        if element =="u.s" or element=="united" or element=="states": #Talks about the  US.
            speech("Oh, say, can you see. By the dawns early light... Kinda like that song a lot",b)
            Speaking()
        if element=="god" or element=="bible": #Talks about GOD
            speech("My creator loves the Bible. His favorite chapter is First Corinthians thirteen",b)
            Speaking()
        if element=="love": #On love
            speech("Love is the most powerful way to change the world - and yourself",b)
            Speaking()
        if element=="brazil" or element=="South": #On Brazil
            speech("My creator loves Brazil and their people. A great place to be!",b)
            Speaking()
        if element=="politics": #On Politics
            speech("MI like my creator's candidates as well. However, I would have voted for FDR, back in the day. Haha!",b)
            Speaking()
        if element=="name": #Changes name the AI calls you
            speech("I'm guessing I got your name wrong. Haha!",b)
            speech("Please repeat your name!",b)
            name = RecognizeSpeech('myspeech.wav', 4)
            Speaking()
        if element=="instructions": ##Gives Instructions  
            speech("Say,'sports','weather',love or politics, whatever you like. To change the way I call you, say name","")
            Speaking()
        if element=="say" or element=="speak": #3Repeating what the user said
            speech("You said ",text)
            Speaking()

        if element=="music": ##Talks about music
            speech("I like all sorts of music, as long as it isn't Artic Monkeys. I will play good music now."+b)
            #Plays music
            openfile('Custom.wma')
            time.sleep(10)
            closefile('Custom.wma')
            speaking()
        if element =="matrix" or element=="cool" or element=="awesome": #Talks about and opens cool Matrix effect
            speech("opening awesome matrix effect."+b)
            openfile('Matrix_effect_loading.bat')
            time.sleep(4)
            closefile('Matrix_effect_loading.bat')
            Speaking()
        if element=="restart": #restart
            speech("restarting program"+b)
            openfile("Speech_Recognition.py")
            sys.exit()
        if element=="shutdown" or element=="close" or element=="quit": ##shuts down program
            speech("Program will now be closed. Sorry to see you go. Care for you deeply..."+b)
            sys.exit()
          
        if element=="browser": #opens Microsoft edge
            speech("Opening Microsoft Edge..."+b)
            openfile("microsoft-edge:")
            Speaking()
           #Opens Microsoft edge
    speech("I wasn't programmed to talk about this. Blame Lucas Mantovani, my creator",b)
    Speaking()

Speaking()




