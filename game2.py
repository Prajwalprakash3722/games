from random import randint
import sys

wins = 0
tied = 0
loses = 0
v = ['rock', 'paper', 'scissor']
computer_move = v[randint(0, 2)]

player = False
while player is False:
    print("Welcome to the game! "
          "Enter Your moves")
    pm = input(''' rock 
 paper
 scissor
 (q) to Quit
    ''')
    if pm == computer_move:
        print("This game is Tied! ")
        tied = tied + 1
        print(f"Ties: {tied}")
    elif pm == 'rock':
        if computer_move == 'paper':
            print('Computer Wins! ')
            loses = loses + 1
            print(f'Loses: {loses}')
            if computer_move == 'scissor':
                print('You Win! ')
                wins = wins + 1
                print(f"Wins: {wins}")
            elif pm == 'paper':
                if computer_move == 'rock':
                    print("You Win! ")
                    wins = wins + 1
                    print(f"Wins: {wins}")
                    if computer_move == 'scissor':
                        print("Computer Wins! ")
                        loses = loses + 1
                        print(f'Loses: {loses}')
                    elif pm == 'scissor':
                        if computer_move == 'rock':
                            print("Computer Wins! ")
                            loses = loses + 1
                            print(f'Loses: {loses}')
                            if computer_move == 'paper':
                                print("You Win! ")
                                wins = wins + 1
                                print(f"Wins: {wins}")
                            elif pm == 'q':
                                sys.exit(0)
                            else:
                                print(
                                    f"Enter valid keywords, you entered {pm} instead of (rocks, paper, scissor) Case-sensitive")

