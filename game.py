"""A number-guessing game."""

from random import randint

tries = 0
number = randint(1, 100)

print "Howdy, what's your name?"

name = raw_input("(type in your name) ")

print "{}, I'm thinking of a number between 1 and 100.".format(name)
print "Can you guess what the number is?"

while True:
    guess = int(raw_input("Your guess? "))
    tries = tries + 1

    if guess < number:
        print "Your guess is too low, try again."

    elif guess > number:
        print "Your guess is too high, try again."

    else:
        print "Well done, {}!".format(name)
        print "You found my number in {} tries!".format(tries)

        break
