import random
import string

from words import words


def get_valid_word(word_list):
    selected_word = random.choice(word_list)

    while "_" in selected_word or " " in selected_word:
        selected_word = random.choice(word_list)

    return selected_word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        print("\nUsed letters:", " ".join(sorted(used_letters)))

        word_display = [
            letter if letter in used_letters else "-"
            for letter in word
        ]
        print("Current word:", " ".join(word_display))

        user_letter = input("Guess a letter: ").upper()

        if len(user_letter) != 1 or user_letter not in alphabet:
            print("Invalid input. Enter one letter.")
            continue

        if user_letter in used_letters:
            print("You already used that letter.")
            continue

        used_letters.add(user_letter)

        if user_letter in word_letters:
            word_letters.remove(user_letter)
            print("Correct!")
        else:
            print("Incorrect!")

    print(f"\nCongratulations! You guessed the word: {word}")


hangman()