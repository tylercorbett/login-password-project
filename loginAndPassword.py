# Login and Password program by Tyler Corbett (thetylercorbett@gmail.com) & Danny Hogan Oct. 2018
# This program is a basic username and password system




loginData = {'Vezro':'Danny123', 'Tiller':'Tyler97'}

username = ''
password = ''

def getUsername ():
    global username
    print('Enter usename:')
    username = input()
    checkUsername()


def getPassword ():
    global password
    print('Enter password: ')
    password = input()
    checkPassword()

def checkUsername ():
    if username in loginData:
        print('Yes it is!')
    else:
        print('No such username')
        getUsername()

def checkPassword ():
    if password == loginData[username]:
        print('Hacked the mainframe')
    else:
        print('Incorrect password')
        getPassword()  

def loginExisting ():
    getUsername()
    getPassword()
