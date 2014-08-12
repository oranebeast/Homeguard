import logging
print('Please input info for info on our potential CEOs, or type the names of Bryce, Jack or Sabian to vote for them!')

info=input()

if info == ("info"):
        print('Bryce:')
        print('')
        print('Hi, I have been coding for numerous years. I have made games,')
        print('software and programs such as this script you are looking at now.')
        print('I beleive that i would be a good ceo because I have completed the BP')
        print('business challenge and i know what it takes to run a business.')
        print('')
        print('')
        print('Jack:')
        print('Im Jack and I am known to be the tech guy, Ive made plenty of games')
        print('ranging from the 36th funnest game in a 2500 people competition, and ')
        print('plenty of othe un-released titles, I have also made great design changes')
        print('To home guard and many other games (See RoboFor by crefossus) I am also')
        print('a well followed twitter guy with almost 50 followers!')
        print('Id be a great leader because of my keen legal sense and strategic ideas')
        print('')
        print('Sabian:')
        print('')
        print('Hello, I am Sabian I am not the best at coding however I still,')
        print('Enjoy doing it and helping out everyone else on github when I can.')
        print('I would say I am great at making ideas and can help with minor tasks')
        print('so I would be great at being an idea manager and or leader.')
        print('')
        print('VOTE JACK!!!!!!!!!!! VOTE SABIAN!!!!!!!!!! VOTE BRYCE!!!!!!!!!!!')
        time.sleep(5)
        print('Now you know all about us please input a name to vote for your selected person!')
        
election=input()

if election == ("Bryce" or "bryce"):
        logging.basicConfig(filename='RESULTS.log',level=logging.DEBUG)
        logging.debug("Bryce has been picked as CEO")
        print('Thank you! You have voted for Bryce!')

if election == ("Jack" or "jack"):
        logging.basicConfig(filename='RESULTS.log',level=logging.DEBUG)
        logging.debug("Jack has been picked as CEO")
        print('Thank you! You have voted for Jack!')

if election == ("Sabian" or "sabian"):
        logging.basicConfig(filename='RESULTS.log',level=logging.DEBUG)
        logging.debug("Sabian has been picked as CEO")
        print('Thank you! You have voted for Sabian!')
        
