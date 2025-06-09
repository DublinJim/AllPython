import os
import sys
# Clear the console screen (for Windows)
os.system('cls')

items =['Rock','Paper','Scissors']

def MyBanner():
    line01 = "*" * 20
    line02 = "*" + " " * 18 + "*"
    line03 = "*    JMK Code      *"
    print("")
    print(line01)
    print(line02)
    print(line03)
    print(line02)
    print(line01)
    print("")
    

MyBanner()

def askChoice():
    user_choice = input('Enter 1 for Rock, 2 for Paper, 3 for Scissors: ')
    isValidChoice = False
    while not isValidChoice:
        if user_choice == '1':
            print('You chose Rock')
            return 'Rock'
            
        elif user_choice == '2':
            print('You chose Paper')
            return 'Paper'
            
        elif user_choice == '3':
            print('You chose Scissors')
            isValidChoice = True
            return 'Scissors'
        else:
            print('Invalid option, TRY AGAIN')
            user_choice = input('Enter 1 for Rock, 2 for Paper, 3 for Scissors: ')


myChoice = askChoice()

