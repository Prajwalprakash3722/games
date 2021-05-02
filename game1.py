####################################################################################################################################################################
# Author: Prajwal Prakash
# Date: 02/11/2020
# Goal: To play Random Number guessing with computer.
###################################################################################################################################################################
import math, random
def generatenumber():
  

    digits = "0123456789"
    number = ""


    for i in range(1):
        number += digits[math.floor(random.random() * 10)]

    return number


if __name__ == "__main__":

 guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess= int(input("Guess: "))
    guess_count +=1
    if guess==generatenumber():
        print("you won")
        break
else:
      print(f"You exceeded your chances, the random number was  {generatenumber()}")
