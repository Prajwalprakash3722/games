################################################################################################################################################
# Author: Prajwal Prakash
# Contributors:
# Date: 02/05/2021 09:35:25 IST
# Goal: To Automate Hangman Game, Playing with computer
################################################################################################################################################
from random import randint

# To input a random word from the list of words we have in .txt format.
# defining a function to pick a random word from a head of words in word txt


def position(list, item):  # index() is not used because it doesnot return if there are duplicate letters
    for index in range(len(list)):  
        if list[index] == item:
            return index + 1 # the output is comming partially correct


def Hangman():

    user = []
    count = 0

    word_text_file = open("words.txt", "r", encoding="UTF-8")
    # You can input any word to download the words please check out my github repositry 
    for columns in (raw.strip().split() for raw in word_text_file):
        i = randint(0, 55000)  # random number allocation
        secret_word = columns[i]
        length_secret_word = len(secret_word)  # length of the string
        print("The word you have to guess is ",
              length_secret_word, " letters long: ", secret_word)

        while count < 8:
            # A letter from User as input
            user_guess = input("Guess the word: ").lower()

            if user_guess in secret_word:  # Checking wheather the letter is present in the computer pre selected word

                # checking where the user input letter is present in the computer pre selected word
                print(user_guess, "is in the word")

                user_guess_position = position(secret_word, user_guess)

                print("Your letter guess is situated in", user_guess_position)
                # To update guessed word by user (updates for each successful input)
                user.insert(user_guess_position, user_guess)
                print("The guessed word is : ", user)

            else:
                print(user_guess, "is not in the word")
                count += 1                                # counting of chances
                chances_remaning = 8 - count              # counting of remaning chances
                print("You have ", chances_remaning, "chances remaning !!")

            if user == secret_word:  # not exctuting ?
                print("Congratulations You Won......")
                exit()


def user_intro():  # User Introduction
    name = input("Enter Your name: ")
    choice = input("Do You want to play: (y/n): ").lower()
    if choice == 'y':
        print("Good Luck", name, "!!")
        Hangman()
    else:
        print("Have a great day!!")
        exit()


user_intro()
