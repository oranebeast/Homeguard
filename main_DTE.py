# Copyright (C) 2014 Vitanoxi <Vitanoxi@gmail.com>

#Login
 
import time
import logging

print('Please enter your username.')
 
name=input()
 
#the three types of users, chnage the names and the password. They act as two codes, the username is a perm based password 
#giving the user a perm, the second is the system wide code, for any changes made
username=  {
'Admin',
'User',
'Moderator'
} 
if name == (username):
        print('Please wait')
        time.sleep(1.5)
        print('')
        print('Correct, please enter your password.')
 
password=input()
 
enterpassword='pass'
if password == (enterpassword):
        print('Please wait')
        time.sleep(2)
        print('')
        print('Correct, logging in.')
        time.sleep(1.5)
        print('Welcome '+username)
        time.sleep(2)
#Logs people that have logged into the console
        logging.basicConfig(filename='previouslogins.log',level=logging.DEBUG)
        logging.debug(time + username + " has logged in")
        
 
if name != (username):
        print('Please wait')
        time.sleep(2)
        print('')
        print('Incorrect, closing program.')
        time.sleep(1.5)
        exit

#Group Command Structure:
#Admin
#Mod
#User       

#executes commands when entered

print('Welcome to your HomeGuard command console by Vitanoxi')
print(version+'Please input your command below.')

command=input()

version='HomeGuard Version 1.'
creator='Vitanoxi <Vitanoxi@gmail.com>'

commands={
    'adminpass',
    'modpass',
    'laser',
    'upload',
    'light',
    'opengui',
    'help',
    'exit',
    'version'
}
#Put this in to make it simple
if command == (creator):
        print(version+creator)

#if command==(adminpass):
#          print('Please wait')
 #         time.sleep(1.5)
 #         print(Please Enter Admin Password!)
#          adminpassword=input()
 #         if adminpassword == (Admin):
 #                          group='Admin'
#                           print('Logged in as Admin')
#          if adminpassword != (Admin)
 #                          print('Incorrect password')
#                           command=input()

#if command==(modpass):
 #         print('Please wait')
  #        time.sleep(1.5)
 #         print(Please Enter Moderator Password!)
 #         modpassword=input()
#          if modpassword == (Mod):
#                         group='Moderator'
#                         print('Logged in as Moderator')
#          if modpassword != (Mod)
#                           print('Incorrect password')
#                           command=input()
         
if command == (laser):
        print('Please wait')
        time.sleep(1.5)
        execfile("laser.py")
        print('Executing command')
        logging.basicConfig(filename='Previouscommands.log',level=logging.DEBUG)
        logging.debug(time + username + "has used the laser command")

if command == (light):
        print('Please wait')
        time.sleep(1.5)
        execfile("light.py")
        print('Executing command')
        logging.basicConfig(filename='Previouscommands.log',level=logging.DEBUG)
        logging.debug(time + username + "has used the light command")
          
if command == (upload):
        print('Please wait')
        time.sleep(1.5)
        execfile("upload.py")
        print('Executing command')
        logging.basicConfig(filename='Previouscommands.log',level=logging.DEBUG)
        logging.debug(time + username + "has used the upload command")

if command == (opengui):
        print('Please wait')
        time.sleep(1.5)
        execfile("gui.py")
        print('Executing command')
        logging.basicConfig(filename='Previouscommands.log',level=logging.DEBUG)
        logging.debug(time + username + "has used the open gui command")
          
if command == (help):
        print('admin, mod, laser, upload, opengui, help, exit, version')
          
if command == (egg):
        print('Congrats you have found the easter egg here is your prize!')
        time.sleep(5)
        exit          
          
if command == (exit):
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
        exit
          
if command !=(commands):
        print('Please Wait')
        time.sleep(1.5)
        print('No Such Command Please Try Again')
        command=input()
        ;
    ;    
;    
