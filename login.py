#Login
 
import time
import logging
  For name
print('Please enter your username.')
 
name=input()
 
#the three types of users, chnage the names and the password. They act as two codes, the username is a perm based password 
#giving the user a perm, the second is the system wide code, for any changes made
username=  {
'Admin'
'User'
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
        time.sleep(10)
#Logs people that have logged into the console
        logging.basicConfig(filename='previouslogins.log',level=logging.DEBUG)
        logging.debug('Someone Has Logged Into The Console' + username)
        
 
if name != (username):
        print('Please wait')
        time.sleep(2)
        print('')
        print('Incorrect, closing program.')
        time.sleep(1.5)
        exit
