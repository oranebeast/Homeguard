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

#Variables
localtime = time.asctime( time.localtime(time.time()) )
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

print('#####################################################################')
print('                              HOMEGUARD                              ')
print('                              (C) 2014                               ')
print('#####################################################################')
time.sleep(4)
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
        logging.debug("User logged in at " + localtime)


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

if command !=(laser or light or upload or opengui or help or egg or exitprogram or version):
        print('Please Wait')
        time.sleep(1.5)
        print('No Such Command Please Try Again')
        time.sleep(2)
        command=input()        


if command == (laser):
        print('Please wait')
        time.sleep(1.5)
        execfile("laser.py")
        print('Executing command')
        logging.basicConfig(filename='Logging/log.log',level=logging.DEBUG)
        logging.debug("Someone has used the laser command " + localtime)
        time.sleep(2)
        command=input()

if command == (light):
        print('Please wait')
        time.sleep(1.5)
        execfile("light.py")
        print('Executing command')
        logging.basicConfig(filename='Logging/log.log',level=logging.DEBUG)
        logging.debug("Someone has used the light command " + localtime)
        time.sleep(2)
        command=input()

if command == (upload):
        print('Please wait')
        time.sleep(1.5)
        execfile("upload.py")
        print('Executing command')
        logging.basicConfig(filename='Logging/log.log',level=logging.DEBUG)
        logging.debug("Someone has used the upload command "  + localtime)
        time.sleep(2)
        command=input()

if command == (opengui):
        print('Please wait')
        time.sleep(1.5)
        execfile("gui.py")
        print('Executing command')
        logging.basicConfig(filename='Logging/log.log',level=logging.DEBUG)
        logging.debug("Someone has used the open gui command "  + localtime)
        time.sleep(2)
        command=input()

if command == (help):
        print('Available commands: admin, mod, laser, upload, opengui, help, exit, version')  #Says available commands
        logging.basicConfig(filename='Logging/log.log',level=logging.DEBUG)
        logging.debug("Someone has used the help command " + localtime)
        time.sleep(2)
        command=input()


if command == (egg):
        print('Congrats you have found the easter egg here is your prize!')
        time.sleep(5)
        exit()

if command == (exitprogram):
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
        
        
        
