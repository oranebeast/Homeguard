import logging
print('Please input info for info on our potential CEOs, or type the names of Bryce, Jack or Sabian to vote for them!')

info=input()

if info == ("info"):
        print('Bryce:')
        print('')
        print('Hi, i have been coding for numerous years. I have made games,')
        print(' software and programs such as this script you are looking at now.')
        print('I beleive that i would be a good ceo because I have completed the BP')
        print('business challenge and i know what it takes to run a business.')
        print('')
        print('')
        print('')
        
        

election=input()

if election == ("Bryce" or "bryce"):
        logging.basicConfig(filename='RESULTS.log',level=logging.DEBUG)
        logging.debug("Bryce has been picked as CEO")

if election == ("Jack" or "jack"):
        logging.basicConfig(filename='RESULTS.log',level=logging.DEBUG)
        logging.debug("Jack has been picked as CEO")

if election == ("Sabian" or "sabian"):
        logging.basicConfig(filename='RESULTS.log',level=logging.DEBUG)
        logging.debug("Sabian has been picked as CEO")        
        
