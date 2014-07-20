# Copyright (C) 2014 Vitanoxi <Vitanoxi@gmail.com>

#
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

#Variables
#now = datetime.datetime.now()
localtime = time.asctime( time.localtime(time.time()) )
enterpassword='pass'
#time = now.strftime("%Y-%m-%d %H:%M")
current_version="1.6"
developers="Bryce Simpson, Jack Heikell and Sabian Coomber-Nickerson"

#Startup sequence
print('#####################################################################')
print('                              HOMEGUARD                              ')
print('                              (C) 2014                               ')
print(                             'Version: ' + current_version             )
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
password=input('Password: ')

if password == 'pass':
        print('Please wait')
        time.sleep(2)
        print('Correct, logging in.')
        time.sleep(1.5)
        print('Welcome User')
        time.sleep(2)
#Logs people that have logged into the console
        logging.basicConfig(filename='Logging/log.log',level=logging.DEBUG)
        logging.debug("User logged in at " + time)
        else
        print('Please wait')
        time.sleep(2)
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

command=input('Command: ')

#Put this in to make it simple
        
if command == ('laser' or 'light' or 'upload' or 'opengui' or 'help' or 'egg' or 'exitprogram' or 'version' or 'credits'):
        print('I LIKE MEG!')
        else
        print('I LIKE AMY!')
                  
