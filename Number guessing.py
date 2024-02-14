# Classic Number guessing game
# Guess randomized number in 7 or less attempts

import random

def number_guessing_game():
    number = random.randint(1,100)  # randomizing number between 1-100
    guess = 0       # stores guesses
    attempts = 7    # number of attempts

    while attempts > 0:
        guess = int(input("\nEnter your guess: "))
        attempts -= 1

        if guess < number:
            print(f"No, that wasn't it. You have {attempts} attempts left.")
            print("Guess higher...")
        elif guess > number:
            print(f"No, that wasn't it. You have {attempts} attempts left.")
            print("Guess lower...")
        else:
            print("You guessed correctly, you win!")

    print(f"You lost! You couldn't guess the number in 7 attempst!\n The number was {number}\n")

number_guessing_game()


