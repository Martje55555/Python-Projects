""" Rock Paper Scissors

----------------------------------------

"""

import random
import os
import re

def check_play_status():
    while True:
        try:
            valid_responses = ['yes', 'no']
            response = input('Do you wish to play again?')

            if response.lower() not in valid_responses:
                raise ValueError('Yes or No only')
            if response.lower() == 'yes':
                break
            else:
                os.system('cls' if os.name=='nt' else 'clear')
                print("Thanks for playing!")
                exit()
        except ValueError as err:
            print("({})".format(err))
    return True

play = True

while play:
    os.system('cls' if os.name=='nt' else 'clear')
    print ("\n")
    print ("Rock, Paper, Scissors - Shoot!")

    userChoice = input("Choose your weapon [R]ock], [P]aper, or [S]cissors: ")

    if not re.match("[SsRrPp]", userChoice):
        print("Please choose a letter:")
        print("[R]ock, [S]cissors or [P]aper.")
        continue

# Echo the user's choice
    
    print("You chose: " + userChoice)

    choices = ['R', 'P', 'S']
    opponenetChoice = random.choice(choices)

    print("I chose: " + opponenetChoice)

    if opponenetChoice == str.upper(userChoice):
        print("Tie! ")
        play = check_play_status()
        
    elif opponenetChoice == 'R' and userChoice.upper() == 'S':
        print("Rock beats scissors, I win! ")
        play = check_play_status()

    elif opponenetChoice == 'S' and userChoice.upper() == 'P':
        print("Scissors beats paper! I win! ")
        play = check_play_status()

    elif opponenetChoice == 'P' and userChoice.upper() == 'R':
        print("Paper beat rock, I win!")
        play = check_play_status()

    else:
        print("You win!\n")
        play = check_play_status()
