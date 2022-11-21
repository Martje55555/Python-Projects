# Libraries to use the random int function, and to clear the terminal
import random
import os

#Enter the minimum and maximum limits of the dice rolls below
min_val = 1
max_val = 6

#the variable that stores the user’s decision
roll_again = "yes"

def num_die():
    while True:
        try:
            num_dice = input('Number of dice: ')
            valid_responses = ['1', 'one', 'two', '2']
            if num_dice not in valid_responses:
                raise ValueError('1 or 2 only')
            else:
                return num_dice
        except ValueError as err:
            print("({})".format(err))


while roll_again.lower() == "yes" or roll_again.lower() == "y":
    os.system('cls' if os.name=='nt' else 'clear')
    amount = num_die()
    if amount == '2' or amount == 'two':
        os.system('cls' if os.name=='nt' else 'clear')
        print("Dices rolling...")
        print("The values are:")

        # Getting random value for dice
        dice1 = random.randint(min_val, max_val)
        dice2 = random.randint(min_val, max_val)

        #Printing the randomly generated variable of the first dice
        print('Dice One: ', dice1)
        #Printing the randomly generated variable of the second dice
        print('Dice Two: ', dice2)
        # Print total of two Dice
        print('Total: ', dice1+dice2)

        #Here the user enters yes or y to continue and any other input ends the program
        roll_again = input("Roll the Dices Again?")
    else:
        print("Die is rolling...")
        print("The value is:")

        # Getting random value for dice
        dice1 = random.randint(min_val, max_val)

        #Printing the randomly generated variable of the first dice
        print('Dice One: ', dice1)

        roll_again = input("Roll the Dices Again?")