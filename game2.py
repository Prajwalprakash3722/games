####################################################################################################################################################################
# Author: Prajwal Prakash
# Date: 16/11/2020, Updated on 31/05/2021
# Goal: To play Rock Paper Scissor with computer
###################################################################################################################################################################
from random import randint, choice
import sys

v = ["Rock", "Paper", "Scissors"]

computer_move = choice(v)

player_move = False
tie = 0
win = 0
lose = 0
while not player_move:
    player_move = input("""Rock,
Paper,
Scissors,
(Q) to Quit
""")
    if player_move == computer_move:
        tie += 1
        print("-->Tie! Total ties:", tie)
    elif player_move == "Rock":
        if computer_move == "Paper":
            lose += 1
            print("-->You lose! Total loses:", lose)
        else:
            win += 1
            print("-->You win! Total wins:", win)
    elif player_move == "Paper":
        if computer_move == "Scissors":
            lose += 1
            print("-->You lose! Total loses:", lose)
        else:
            win += 1
            print("-->You win!")
    elif player_move == "Scissors":
        if computer_move == "Rock":
            lose += 1
            print("-->You lose! Total loses:", lose)
        else:
            win += 1
            print("--> You win! Total wins:", win)
    elif player_move == "Q":
        sys.exit(0)
    else:
        print("-->That's not a valid play. Check your spelling (Case sensitive)")
    player_move = False
    computer_move = v[randint(0, 2)]
    
