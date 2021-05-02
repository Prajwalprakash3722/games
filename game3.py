################################################################################################################################################
# Author: Prajwal Prakash
# Contributors: 
# Date: 02/05/2021
# Goal: To Automate Hangman Game, Playing with computer
################################################################################################################################################
from random import randint

# To input a random word from the list of words we have in .txt format.

def pickword():
    
    word_text_file = open("words.txt", "r", encoding="UTF-8")
    for columns in (raw.strip().split() for raw in word_text_file):
        i = randint(0, 1000)
        secret_word = columns[i]
        length_secret_word = len(secret_word)
        print(length_secret_word)


def wordguess():

    
