# import pywhatkit
# whno = input("Enter user whatsapp no :")
# msg = input("Enter user message : ")
# hr = int(input("Enter Hour(24 hours format):"))
# mnt = int(input("Enter Minutes :"))
#
# pywhatkit.sendwhatmsg('+91'+ whno,msg,hr,mnt)

import pywhatkit
def whastapp(whnos,msgs,hrs,mnts):
    return whnos,msgs, hrs, mnts

whno = input("Enter user whatsapp no :")
msg = input("Enter user message : ")
hr = int(input("Enter Hour(24 hours format):"))
mnt = int(input("Enter Minutes :"))
pywhatkit.sendwhatmsg('+91'+ whno,msg,hr,mnt)
whastapp(whno,msg,hr,mnt)


