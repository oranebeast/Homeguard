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
dapassword="pass"
beta="True"
version="version"
current_version="1.7 Beta"
Developer="False"
adminpass="admin"
Admin="False"
file = open('Logging/Logs.log', 'r')

#Group Define
if beta == ("True"):
        Developer = "True"
        logging.basicConfig(filename='Logging/logs.log',level=logging.DEBUG)
        logging.debug("Developer logged in at: " + localtime)


#Startup sequence
print('#####################################################################')
print('                              HOMEGUARD                              ')
print('                              (C) 2014                               ')
print(                               'Version '  + current_version           )
print('#####################################################################')
time.sleep(1)
if beta != ("True"):
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
        
if beta != ("True"):
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
        if password == (adminpass):
                Admin="True"
                print('Please wait')
                time.sleep(2)
                print('Correct, logging in.')
                time.sleep(1.5)
                print('Welcome Admin')
                time.sleep(2)
                logging.basicConfig(filename='Logging/logs.log',level=logging.DEBUG)
                logging.debug("Admin logged in at: " + localtime)        
        if password != (dapassword or adminpass):
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
if beta == ("False"):
        print('Welcome to your HomeGuard command console by Vitanoxi')
        print('Please input your command')
if beta == ("True"):
        print('Welcome Developer')
        print('Please input your command')
if Admin == ("True"):
        print('Welcome to Admin. You are in control)
        print('Please input your command')

#def _mainloop_():

command=input()

#Admin commands
if command ==("log") and Admin ==("True"):
        print file.read()

#Put this in to make it simple

if command == ("laser"):
        print('Please wait')
        time.sleep(1.5)
        execfile("laser.py")
        print('Executing command')
        logging.basicConfig(filename='Logging/logs.log',level=logging.DEBUG)
        logging.debug("Someone has used the laser command: " + localtime)
        time.sleep(2)
        command=input()
        
if command == ("light"):
        print('Please wait')
        time.sleep(1.5)
        execfile("light.py")
        print('Executing command')
        logging.basicConfig(filename='Logging/logs.log',level=logging.DEBUG)
        logging.debug("Someone has used the light command: " + localtime)
        time.sleep(2)
        command=input()
        
if command == ("upload"):
        print('Please wait')
        time.sleep(1.5)
        execfile("upload.py")
        print('Executing command')
        logging.basicConfig(filename='Logging/logs.log',level=logging.DEBUG)
        logging.debug("Someone has used the upload command: "  + localtime)
        time.sleep(2)
        command=input()

if command == ("opengui"):
        print('Please wait')
        time.sleep(1.5)
        execfile("gui.py")
        print('Executing command')
        logging.basicConfig(filename='Logging/logs.log',level=logging.DEBUG)
        logging.debug("Someone has used the open gui command: "  + localtime)
        time.sleep(2)
        command=input()

if command == ("help"):
        print('admin, mod, laser, upload, opengui, help, exit, version')
        logging.basicConfig(filename='Logging/logs.log',level=logging.DEBUG)
        logging.debug("Someone has used the help command: " + localtime)
        time.sleep(2)
        command=input()

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

if command == ("version"):
        print('#####################################################################')
        print('                              HOMEGUARD                              ')
        print('                              (C) 2014                               ')
        print(                               'Version ' + current_version            )
        print('#####################################################################')

if command != ("laser" or "light" or "upload" or "opengui" or "help" or "egg" or "exitprogram" or "version") and Developer != ("True"):
        print('Incorrect command input!')

if command != ("laser" or "light" or "upload" or "opengui" or "help" or "egg" or "exitprogram" or "version") and Developer == ("True"):
        print('NIGGA YOU FAIL AT LIFE!')
        
        
        

        
        

        

        
        
        
