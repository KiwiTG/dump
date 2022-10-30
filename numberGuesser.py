###############################
##### Number Guesser Game #####
###############################

from random import *
import os, time, platform

cor = 0
inc = 0

if platform.system() == 'Windows':
    def clear():
        os.system('cls')
if platform.system() == 'Linux':
    def clear():
        os.system('clear')
else:
    exit()

if __name__ == '__main__':
    while True:
        clear()
        num = randint(1, 100)
        nmin = num - randint(1, 10)
        nmax = num + randint(1, 10)
        print(f"Correct: {cor}")
        print(f"Incorrect: {inc}")
        try:
            guess = int(input(f"Guess the number between {nmin} and {nmax} > "))
        except:
            clear()

        if guess < nmin or guess > nmax:
            print("Out of range!")
            time.sleep(1)
            os.system('clear')

        if guess == num:
            print("You guessed correctly!")
            time.sleep(2)
            cor += 1
        else:
            print("You guessed incorrectly!")
            time.sleep(2)
            inc += 1
