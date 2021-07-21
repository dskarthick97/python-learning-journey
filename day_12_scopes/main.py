""" Number guessing game """

import random


logo = """ 
  ________                         __  .__                                 ___.                 
 /  _____/ __ __   ____   ______ _/  |_|  |__   ____     ____  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___/ \   __\  |  \_/ __ \   /    \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \   |  | |   Y  \  ___/  |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >  |__| |___|  /\___  > |___|  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/             \/     \/       \/            \/    \/     \/     
"""

print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")

actual_number = random.randint(1, 100)


def get_no_of_attempts():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "hard":
        return 10
    
    return 5


def is_passed(guessed_number):
    if guessed_number > actual_number:
        print("Too high")
    else:
        print("Too low")


def guess_number():
    attempts = get_no_of_attempts()

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessed_number = int(input("Make a guess: "))

        if guessed_number == actual_number:
            attempts = 0
            return f"You got it! The answer was {guessed_number}"
        else:
            attempts -= 1
            is_passed(guessed_number)
            print("Guess again.")

    return f"Your attempts over!"


print(guess_number())
