# program to play rock, paper, scissor with user.
#importing all required packages:
import random
flag = True
while flag == True:
    #instructions
    print("\033[1mWelcome to the rock, paper, scissor match!!")
    no_of_times = int(input("How many games do you want to play? :"))
    print("Enter either rock, paper or scissor in every game")

    #actual program flow
    computer_score, user_score = 0, 0
    for i in range(no_of_times):
        print("\033[0mGame number", i+1)
        user_input = str.lower(input("You: "))

        #code for generating random list
        options_list = ['rock', 'paper', 'scissor']
        computer_choice =  random.choice(options_list)
        print("Computer:",computer_choice)

        #check for the score
        if user_input == 'rock' and computer_choice == 'scissor':
            user_score = user_score + 1
            print("You won this game")
        elif user_input == 'paper' and computer_choice == 'rock':
            user_score = user_score + 1
            print("You won this game")
        elif user_input == 'scissor' and computer_choice == 'paper':
            user_score = user_score + 1
            print("You won this game")
        elif user_input == computer_choice:
            print("This game is a tie as both are same")
        else:
            computer_score = computer_score + 1
            print("Computer won this game")

    # to determine winner of match
    if computer_score>user_score:
        print("\033[1mThe computer defeats you by",computer_score-user_score,"points")
    elif user_score>computer_score:
        print("\033[1mYou defeated the computer by",user_score-computer_score,"points")
    else:
        print("\033[1mBoth the computer and you are at a tie at",user_score,"each")
    # if player wishes to play again
    print("\033[0mDo you want to play again")
    play_again_response = str.lower(input("Yes/No :"))
    if play_again_response == 'yes':
        flag = True
    elif play_again_response == 'no':
        flag = False