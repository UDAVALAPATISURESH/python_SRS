'''                   Project name
                Virtul Talking Friend
          ______ let's Build our own First App ___________________

'''
# first install (pip install pyttsx3) how instal python packeg  fist open chrome searching - pyttsx3 next copy this (pip install pyttsx3)
import pyttsx3
vtf = pyttsx3.init()## object creation => #edhi appudu initializing avuthundhi

""" RATE"""
rate = vtf.getProperty('rate')   # getting details of current speaking rate
# print (rate)                   #printing current voice rate  # print anethi manamu print cheydani use chestamu
vtf.setProperty('rate', 100)     # setting up new voice rate  => #edhi endhuku vaduthamu ante voice sloga ravadani use chestamu

txt = "Hello suresh your python developer!"
print("Speaking..............!")
vtf.say(txt) # txt ane verble thisukokapoyna manamu ella kuda use chey vachu => ptint("Hello suresh your python developer!")
vtf.runAndWait() # tharuvatha (runAndWait) method ni call cheylisivastundhi

txt = input("what should I say :")
print("Speaking..............!")
vtf.say(txt)

vtf.runAndWait()



















