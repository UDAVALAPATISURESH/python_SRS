import pyttsx3
vtf = pyttsx3.init()

""" RATE"""
rate = vtf.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
vtf.setProperty('rate', 125)     # setting up new voice rate

def vtf_speak(text):
    print("Speaking.............!")
    vtf.say(text)
    vtf.runAndWait()

txt = 'Hello suresh your python developer!'
vtf_speak(txt)

while txt != 'bye':
    txt = input("What shoul I say :")
    txt = txt.lower()

    if txt != "bye":
        vtf_speak(txt)

    else:
         vtf_speak("See you again friend, that was nice talking to you ")

