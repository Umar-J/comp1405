# Umar Jan 101270578
# Tutorial 4, Ex. B
from random import randint
random = randint(1, 100)

Flag = True
x=0
while Flag:
    x += 1
    # user takes guess
    userGuess = int(input("\nGuess the number\n>"))

    # break if guesses exceeds 10
    if x > 10:
        print("\nYou have lost because you ran out of tries, Good luck next time!")
        Flag = False

    # break if user gueses correctly
    if userGuess == random:
        print("\nYou have Won and guessed the number correctly. Congrats!!!!!!!!")
        Flag = False

    # Lower or higher depending on the user's guess
    if userGuess > random:
        print("Incorrect, Next time guess Lower")
    elif userGuess < random:
        print("Incorrect, Next time guess Higher")
    