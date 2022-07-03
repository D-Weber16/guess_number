import random

secret_number = random.randint(1, 100)

print("Welcome to my guessing game!")

guess = int(input("Please make a guess! ", ))

while guess != secret_number:
    if guess < secret_number:
        print("Too low.")
        guess = int(input("Try again: "))
    elif guess > secret_number:
        print("Too high.")
        guess = int(input("Try again: "))

if guess == secret_number:
    print("You win!!")