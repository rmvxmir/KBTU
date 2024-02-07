# Task 13 from functions1.py
from random import randint

print("Hello! What is your name?")
name = input("")

print(f"Well, {name}, I am thinking of a number between 1 and 20.")
random_num = randint(1, 20)

def take_guess():
    return int(input("Take a guess: "))

def check_guess(random_num, guess):
    if guess < random_num:
        print("Your guess is too low.")
        return False
    elif guess > random_num:
        print("Your guess is too high.")
        return False
    else:
        return True

def game(name, random_num):
    guess_count = 0
    while True:
        guess = take_guess()
        if check_guess(random_num, guess):
            guess_count += 1
            print(f"Good job, {name}! You guessed my number in {guess_count} guesses!")
            break
        guess_count += 1

game(name, random_num)