# Copyright (C) 2014 Vitanoxi <Vitanoxi@gmail.com>

#  _    _                                                _ 
# | |  | |                                              | |
# | |__| | ___  _ __ ___   ___  __ _ _   _  __ _ _ __ __| |
# |  __  |/ _ \| '_ ` _ \ / _ \/ _` | | | |/ _` | '__/ _` |
# | |  | | (_) | | | | | |  __/ (_| | |_| | (_| | | | (_| |
# |_|  |_|\___/|_| |_| |_|\___|\__, |\__,_|\__,_|_|  \__,_|
#                               __/ |                      
#                              |___/                 

#import cv2
#import sys
#import hashlib
#import getpass
import time
import logging

#########LOOP DO NOT TOUCH!!!#########
Loop="False"                         #
#########LOOP DO NOT TOUCH!!!#########

#Variables
localtime = time.asctime( time.localtime(time.time()) )
dapassword="pass"
beta="True"
current_version="1.8 Beta"
#file=open('Logging/Logs.log', 'r')

#Group Define
if beta == ("True"):
        logging.basicConfig(filename='Logging/logs.log',level=logging.DEBUG)
        logging.debug("Beta Tester logged in at: " + localtime)


#Startup sequence
print('#####################################################################')
print('                              HOMEGUARD                              ')
print('                              (C) 2014                               ')
print(                               'Version '  + current_version           )
print('#####################################################################')
time.sleep(1)

print("Loading 10%")
time.sleep(0.25)
print("Loading 20%")
time.sleep(0.25)
print("Loading 30%")
time.sleep(0.25)
print("Loading 40%")
time.sleep(0.25)
print("Loading 50%")
time.sleep(0.25)
print("Loading 60%")
time.sleep(0.25)
print("Loading 70%")
time.sleep(0.25)
print("Loading 80%")
time.sleep(0.25)
print("Loading 90%")
time.sleep(0.25)
print("Loading 99%")
time.sleep(1)
#First Chance        

print("Loaded Vitanoxi Verstion " + current_version)
time.sleep(1)
print('Please enter your Password.')
password=input()
if password == (dapassword):
        print('Please wait')
        time.sleep(2)
        print('Correct, logging in.')
        time.sleep(1.5)
        print('Welcome User')
        time.sleep(2)
        logging.basicConfig(filename='Logging/logs.log',level=logging.DEBUG)
        logging.debug("User logged in at: " + localtime)
        Loop="True"
if password != (dapassword):
                print('Please wait')
                time.sleep(2)                        
                print('Incorrect Password')
                time.sleep(2)
                exit()                
#Group Command Structure:
#Admin
#Mod
#User
if beta == ("False"):
        print('Welcome to your HomeGuard command console by Vitanoxi')
        print('Please input your command')
else:
        print('Welcome Beta Tester!')
        print('Please input your command')
command=input() 
####################################################USER COMMANDS#######################################################
while Loop == ("True"):                                   
        if command == ("help") and Admin == ("False") and Developer == ("False"):
                 print('Commands:')
                 print('admin\nmod\nlaser\nupload\nopengui\nhelp\nexitprogram\nversion')
                 logging.basicConfig(filename='Logging/logs.log',level=logging.DEBUG)
                 logging.debug("Someone has used the help command: " + localtime)
                 time.sleep(2)
        if command == ("egg"):
                 print('Congrats you have found the easter egg here is your prize!')
                 logging.basicConfig(filename='Logging/logs.log',level=logging.DEBUG)
                 logging.debug("SOMEONE HAS FOUND THE EASTER EGG! ")
                 time.sleep(5)
                 exit()
        if command == ("exitprogram"):
                 print('Please wait')
                 time.sleep(1.5)
                 print('Exiting Vitanoxi HomeGuard Console')
                 print('Exiting in 5')
                 time.sleep(1)
                 print('4')
                 time.sleep(1)
                 print('3')
                 time.sleep(1)
                 print('2')
                 time.sleep(1)
                 print('1')
                 time.sleep(1)
                 exit("Closed")
        if command == ("info"):
                 print('#####################################################################')
                 print('                              HOMEGUARD                              ')
                 print('                              (C) 2014                               ')
                 print(                               'Version ' + current_version            )
                 print('                                                                     ')
                 print('CEO/JrDev: Sabian Coomber-Nickerson                                  ')
                 print('Project Manager/Developer: Bryce Simpson                             ')
                 print('Developer: Jack Heikel                                               ')
                 print('#####################################################################')
                 
        if command == ("opengui" or "help" or "egg" or "exit" or "info"):
                 command=input()
