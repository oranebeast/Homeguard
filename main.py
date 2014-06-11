# Copyright (C) 2014 Vitanoxi <Vitanoxi@gmail.com>

#Login
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
import datetime
import termcolor
from termcolor import colored

#Variables
now = datetime.datetime.now()
#localtime = time.asctime( time.localtime(time.time()) )
enterpassword='pass'
version1='HomeGuard Version 1.1'
laser='laser'
light='light'
upload='upload'
opengui='opengui'
help='help'
egg='egg'
exitprogram='exitprogram'
version='version'
time = print now.strftime("%Y-%m-%d %H:%M")
current_version="1.5"

#Startup sequence
print('#####################################################################')
print('                              HOMEGUARD                              ')
print('                              (C) 2014                               ')
print('                             Version ' + current_version'            ')
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
time.sleep(5)
print("Loaded Vitanoxi Verstion " + current_version)
time.sleep(1)
print('Please enter your Password.')
password=input()

if password == (enterpassword):
        print('Please wait')
        time.sleep(2)
        print('')
        print('Correct, logging in.')
        time.sleep(1.5)
        print('Welcome User')
        time.sleep(2)
#Logs people that have logged into the console
        logging.basicConfig(filename='Logging/log.log',level=logging.DEBUG)
        logging.debug("User logged in at " + time)


if password != ("pass"):
        print('Please wait')
        time.sleep(2)
        print('')
        print('Incorrect, closing program.')
        time.sleep(1.5)
        exit("Closed")
        
#Group Command Structure:
#Admin
#Mod
#User

#executes commands when entered
print('Welcome to your HomeGuard command console by Vitanoxi')
print('Please input your command below.')

command=input()

#Put this in to make it simple

if command !=(laser.lower or light.lower or upload.lower or opengui.lower or help.lower or egg or exitprogram.lower or version.lower):
        print('Please Wait')
        time.sleep(1.5)
        print('No Such Command Please Try Again')
        time.sleep(2)
        command=input()        


if command == (laser.lower):
        print('Please wait')
        time.sleep(1.5)
        execfile("laser.py")
        print('Executing command')
        logging.basicConfig(filename='Logging/log.log',level=logging.DEBUG)
        logging.debug("Someone has used the laser command " + time)
        time.sleep(2)
        command=input()

if command == (light.lower):
        print('Please wait')
        time.sleep(1.5)
        execfile("light.py")
        print('Executing command')
        logging.basicConfig(filename='Logging/log.log',level=logging.DEBUG)
        logging.debug("Someone has used the light command " + time)
        time.sleep(2)
        command=input()

if command == (upload.lower):
        print('Please wait')
        time.sleep(1.5)
        execfile("upload.py")
        print('Executing command')
        logging.basicConfig(filename='Logging/log.log',level=logging.DEBUG)
        logging.debug("Someone has used the upload command "  + time)
        time.sleep(2)
        command=input()

if command == (opengui.lower):
        print('Please wait')
        time.sleep(1.5)
        execfile("gui.py")
        print('Executing command')
        logging.basicConfig(filename='Logging/log.log',level=logging.DEBUG)
        logging.debug("Someone has used the open gui command "  + time)
        time.sleep(2)
        command=input()

if command == (help.lower):
        print('Available commands: admin, mod, laser, upload, opengui, help, exit, version')  #Says available commands
        logging.basicConfig(filename='Logging/log.log',level=logging.DEBUG)
        logging.debug("Someone has used the help command " + time)
        time.sleep(2)
        command=input()


if command == (egg):
        print('Congrats you have found the easter egg here is your prize!')
        time.sleep(5)
        exit()

if command == (exitprogram.lower):
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
        
        
if command == (version.lower):
        print('#####################################################################')
        print('                              HOMEGUARD                              ')
        print('                              (C) 2014                               ')
        print('                             Version ' + current_version'            ')
        print('#####################################################################')
        
        
        
        time.sleep(5)
        exit()
        
        
        
