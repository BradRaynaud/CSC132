# This program guesses a number from 1-5
# By- Brad Raynaud
import random

correct = ""
print("Please think of a number from 1-5, enter 1 when you are ready to proceed")
ready = input()
while correct != 1:
    guess = random.randint(1,5)
    print("Is your number {}, if so enter 1 if not enter 0").format(guess)
    correct = input()