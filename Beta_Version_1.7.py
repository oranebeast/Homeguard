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
version="version"
current_version="1.7 Beta"
Developer="False"
adminpass="admin"
Admin="False"
End="False"
incorrect1="False"
incorrect2 ="False"
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
#First Chance        
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
                Loop="True"
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
                Loop="True"
        if password != (dapassword or adminpass):
                        print('Please wait')
                        time.sleep(2)                        
                        print('Incorrect Password You have TWO Attempts Left')
                        time.sleep(1)
                        incorrect1="True"
#Second Chance 
        if incorrect1 == ("True"):
                print('Please enter your Password again.')
                password1=input()
                if password1 == (dapassword):
                        print('Please wait')
                        time.sleep(2)
                        print('Correct, logging in.')
                        time.sleep(1.5)
                        print('Welcome User')
                        time.sleep(2)
                        logging.basicConfig(filename='Logging/logs.log',level=logging.DEBUG)
                        logging.debug("User logged in at: " + localtime)
                        Loop="True"
                if password1 == (adminpass):
                        Admin="True"
                        print('Please wait')
                        time.sleep(2)
                        print('Correct, logging in.')
                        time.sleep(1.5)
                        print('Welcome Admin')
                        time.sleep(2)
                        logging.basicConfig(filename='Logging/logs.log',level=logging.DEBUG)
                        logging.debug("Admin logged in at: " + localtime) 
                        Loop="True"
                if password1 != (dapassword or adminpass):
                        print('Please wait')
                        time.sleep(2)
                        print('Incorrect Password You have ONE MORE Attempts Left')
                        time.sleep(1)
                        incorrect2="True"
#Final Chance   
        if incorrect2 == ("True"):
                print('Please enter your Password again.')
                password2=input()
                if password2 == (dapassword):
                        print('Please wait')
                        time.sleep(2)
                        print('Correct, logging in.')
                        time.sleep(1.5)
                        print('Welcome User')
                        time.sleep(2)
                        logging.basicConfig(filename='Logging/logs.log',level=logging.DEBUG)
                        logging.debug("User logged in at: " + localtime)
                        Loop="True"
                if password2 == (adminpass):
                        Admin="True"
                        print('Please wait')
                        time.sleep(2)
                        print('Correct, logging in.')
                        time.sleep(1.5)
                        print('Welcome Admin')
                        time.sleep(2)
                        logging.basicConfig(filename='Logging/logs.log',level=logging.DEBUG)
                        logging.debug("Admin logged in at: " + localtime) 
                        Loop="True"
                if password2 != (dapassword or adminpass):
                        print('Please wait')
                        time.sleep(2)
                        print('Incorrect Password You have NO MORE Attempts Left')
                        time.sleep(1)
                        print('Shutting Down')
                        exit("Closed")

#Group Command Structure:
#Admin
#Mod
#User
if beta == ("False"):
        print('Welcome to your HomeGuard command console by Vitanoxi')
        print('Please input your command')
        command=input()
if beta == ("True"):
        print('Welcome Developer')
        print('Please input your command')
        command=input()
if Admin == ("True") and beta == ("False"):
        print('Welcome to Admin. You are in control)
        print('Please input your command')
        command=input()
if Admin == ("False") or beta == ("True"):
        print('Beta is enabled please disable it and try again!')
        time.sleep(5)
        exit("Closed")
        
                        
#################################################ADMIN COMMANDS##########################################################
while Loop == ("True"):
        if command == ("log") and Admin ==("True"):
                print file.read()
                if command == ("help") and Admin == ("True"):
                        print('Commands:')
                        print('mod\nlaser\nupload\nopengui\nhelp\nexitprogram\nversion')
                        print('')
                        print('Admin Commands:')
                        print('log\nhelp')
                        logging.basicConfig(filename='Logging/logs.log',level=logging.DEBUG)
                        logging.debug("Someone has used the help command: " + localtime)
                        time.sleep(2)
                        command=input()
                        
####################################################USER COMMANDS#######################################################
                        
                        if command == ("opengui"):
                                print('Please wait')
                                time.sleep(1.5)
                                execfile("dropbox_shorts.py")
                                print('Executing command')
                                logging.basicConfig(filename='Logging/logs.log',level=logging.DEBUG)
                                logging.debug("Someone has used the open gui command: "  + localtime)
                                time.sleep(2)
                                command=input()
                        if command == ("help") and Admin == ("False"):
                                print('Commands:')
                                print('admin\nmod\nlaser\nupload\nopengui\nhelp\nexitprogram\nversion')
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
                                command=input()
                        if command != ("opengui" or "help" or "egg" or "exitprogram" or "info") and Developer != ("True"):
                                print('Incorrect command input!')
                                command=input()
                                #End="True"
                        if command != ("opengui" or "help" or "egg" or "exitprogram" or "info") and Developer == ("True"):
                                print('NIGGA YOU FAIL AT LIFE!')
                                command=input()
                                #End="True"
''''
                        if End == ("True"):
                                time.sleep(5)
                                print('Due to tech problems we regret to inform you that you will have to restart the program!')
                                time.sleep(2)
                                print('Exit? Y or N')
                                exit=input()
                        if exit == ("Y" or "yes" or "y" or "Yes"):
                                print('Closing')
                                time.sleep(2)
                                exit("Closed")
                        if exit == ("N" or "no" or "n" or "No"):
                                print('Ok. Thats fine do it yourself!')
'''
