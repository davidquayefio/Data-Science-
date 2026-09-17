import random


def guess(x):
    random_num = random.randint(1, x)
    user_guess = 0

    while user_guess != random_num:
        user_guess = int(input(f"Guess a number between 1 and {x}: "))

        if user_guess < random_num:
            print("Sorry, guess again. Too low.")
        elif user_guess > random_num:
            print("Sorry, guess again. Too high.")

    print(f"Congratulations! You guessed the number {random_num}.")


guess(10)