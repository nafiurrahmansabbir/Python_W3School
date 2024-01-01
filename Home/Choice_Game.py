# import random
from random import randint

guessNumber=int(input("Enter a random number 1-5: "))
randomNumber=randint(1,5)

if guessNumber==randomNumber:
    print("\nYou are win\n")
else:
    print("\nYou are Lose!\n")
    print("Randam number is ",randomNumber)