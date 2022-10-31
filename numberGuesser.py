###############################
##### Number Guesser Game #####
###############################

from random import *
import os, time, platform

if platform.system() == 'Windows':
    def clear():
        os.system('cls')
if platform.system() == 'Linux':
    def clear():
        os.system('clear')
else:
    exit()

def game():

    cor = 0
    inc = 0

    answer = randint(1, 100)
    nmin = answer - randint(1, 10)
    nmax = answer + randint(1, 10)

    while True:
        clear()

        print(f"Correct: {cor}")
        print(f"Incorrect: {inc}")

        try:
            guess = int(input(f"Guess the number between {nmin} and {nmax} > "))
        except:
            clear()

        if guess < nmin:
            print("Out of range, too low!")
            time.sleep(1)
            clear()

        if guess > nmax:
            print("Out of range, too high!")
            time.sleep(1)
            clear()

        if guess > answer:
            print("You guessed incorrectly, too high!")
            time.sleep(1)
            inc += 1
            clear()
    
        if guess < answer:
            print("You guessed incorrectly, too low!")
            time.sleep(1)
            inc += 1
            clear()

        if guess == answer:
            print("You guessed correctly!")
            time.sleep(2)
            cor += 1
            clear()
            break

while True:
    game()
