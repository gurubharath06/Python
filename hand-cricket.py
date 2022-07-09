# a program to play hand cricket game with the computer
#import all required packages
import random
def computer_random_choice():
    options_available = [0,1,2,3,4,5,6,10,12,20]
    computer_choice = random.choice(options_available)
    return computer_choice