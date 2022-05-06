from re import A
from cryptography.fernet import Fernet
def LoadKey():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

def quit():
    print('u have quit ._.')

mainpass = input("create a main passcode (protects all ur passwords): ")

def mainverify():
    global situation, attempts 
    attempts = 3
    while True:
        usrverify = input(f"\nenter ur master password to verify it's u or quit(q)\nu have {attempts} attemps to input ur main password right \n    enter ur attempt: ")
        if usrverify == mainpass:
            print("password correct. u may view ur passwords :-]\n")
            situation = 1  #the first situation: if the user guesses correctly, they may continue
            break
        elif usrverify == "q" or usrverify == "Q": 
            quit()
            situation = 2 #the second situation: if the user quits 
            break
        else:
            attempts = attempts - 1 #continues guessing 

        if attempts == 0:
            print("attempts incorrect. u have been locked out :/")
            situation = 3 #the third situation: the user runs out of attempts
            break

key = LoadKey() + (mainpass.encode())
fer = Fernet(key)

def view(): #displays everything that has been input 
    if situation == 1:
        with open("passwords.txt", "r") as f:
            for line in f.readlines():
                UserPass = line.rstrip()
                showuser, showpass, showphonenumber = UserPass.split("|")
                print("username:", showuser, "| password:", 
                    fer.decrypt(showpass.encode()).decode(), "| phone number:", 
                    fer.decrypt(showphonenumber.encode()).decode()) 
    else:
        print('u can try again, tho :-]')
        pass

def addpass():
    if situation == 1: 
        username = input("enter username: ")
        passw = input("enter password: ")
        Phone = input("enter phone number: ")
        with open("passwords.txt", "a") as f:
            f.write(username + "|" + fer.encrypt(passw.encode()).decode() + "|" + fer.encrypt(Phone.encode()).decode() + "\n")
        print("a new password has been saved successfully :-]\n\n")

    else: #the other 2 sitations, where the code must lock out the user temporarily. they can try again stil, if they choose 
        print('u can try again, tho :-]')
        pass

while True: 
    choose = input("\nview passwords (v) \nadd a password (a) \nquit (q) \n  what would u like to do?: ").lower()
    if choose == "v":
        mainverify() #verification --> guess main pwd
        view() 
        
    elif choose == "a":
        mainverify() #verification --> guess main pwd
        addpass() 

    elif choose == "q":
        quit()
        break #ends loop
    
    else:
        print("invalid ._.")
        continue #repeats loop

