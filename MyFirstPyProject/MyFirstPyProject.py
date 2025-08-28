
import random

secret = random.randint(1, 100)
guess = 0
tries = 1

while guess != secret:
    guess = int(input("Guess the number (1-100): "))
    if guess < secret:
        print("Too low!")
        tries += 1
    elif guess > secret:
        print("Too high!")
        tries += 1
    else:
        print(f"You got it! The number was {secret}!")
        print(f"It took you {tries} tries to guess the number")
