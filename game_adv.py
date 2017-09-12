"""A more sophisticated number-guessing game."""

from random import randint

best_score = 99999

print "Howdy, what's your name?"
name = raw_input("(type in your name) ")

while True:
    number = randint(1, 100)
    tries = 0

    print "{}, I'm thinking of a number between 1 and 100.".format(name)
    print "Can you guess what the number is?"

    while True:
        try:
            guess = int(raw_input("Your guess? "))

        except ValueError:
            print "That's not an integer, try again"
            continue

        if guess < 1 or guess > 100:
            print "That's not between 1 and 100. Try again."
            continue

        tries = tries + 1

        if guess < number:
            print "Your guess is too low, try again."

        elif guess > number:
            print "Your guess is too high, try again."

        else:
            print "Well done, {}!".format(name)
            print "You found my number in {} tries!".format(tries)
            break

    if tries < best_score:
        best_score = tries

    answer = raw_input("Do you want to play again? ").upper()

    if answer != 'Y' and answer != 'YES':
        break

print "Your best score was {}.".format(best_score)
