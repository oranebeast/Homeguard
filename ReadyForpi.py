if command == (help):
 -        print('Available commands: admin, mod, laser, upload, opengui, help, exit, version')  #Says available commands
 -        logging.basicConfig(filename='serverlogs.log',level=logging.DEBUG)
 -        logging.debug("Someone has used the help command " + localtime)
 -        time.sleep(2)
 -        command=input()
