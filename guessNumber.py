# number guessing game
import random

guess = 0

computers_number = random.randint(0, 9)
print(computers_number)
condition = True
while condition:
    user_guess = input("Guess the number (0-9) or exit: ")
    if user_guess == "exit":
        print("Hope to see you again.")
        condition = False
    elif computers_number == int(user_guess):
        guess += 1
        print("Congratulation! You guessed correct number in", guess, "tries.")
        condition = False
    elif computers_number < int(user_guess):
        print("Too high!")
        guess += 1
    elif computers_number > int(user_guess):
        print("Too low!")
        guess += 1
    else:
        print("Sorry! Something went wrong.")




# created by Suman Nepali May, 2019
