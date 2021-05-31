####################################################################################################################################################################
# Author: Prajwal Prakash
# Date: 16/11/2020, Updated on 31/05/2021
# Goal: To play Rock Paper Scissor with computer
###################################################################################################################################################################
from random import choice

v = ["Rock", "Paper", "Scissors"]
playing = False
tie = 0
win = 0
lose = 0
while not playing:
    computer_move = choice(v).lower()
    player_move = input("""Rock,
Paper,
Scissors,
(Q) to Quit
""").lower()
    if player_move == computer_move:
        tie += 1
        print("-->Tie! Total ties:", tie)
    elif player_move == "Rock".lower():
        if computer_move == "Paper".lower():
            lose += 1
            print("-->You lose! Total loses:", lose)
        else:
            win += 1
            print("-->You win! Total wins:", win)
    elif player_move == "Paper".lower():
        if computer_move == "Scissors".lower():
            lose += 1
            print("-->You lose! Total loses:", lose)
        else:
            win += 1
            print("-->You win!")
    elif player_move == "Scissors".lower():
        if computer_move == "Rock".lower():
            lose += 1
            print("-->You lose! Total loses:", lose)
        else:
            win += 1
            print("--> You win! Total wins:", win)
    elif player_move == "Q".lower():
        playing = True
    else:
        print("-->That's not a valid play. Check your spelling")
