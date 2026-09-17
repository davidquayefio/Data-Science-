import random
import string

from words import words


HANGMAN_ART = [
	"  +---+\n  |   |\n      |\n      |\n      |\n=========",
	"  +---+\n  |   |\n  O   |\n      |\n      |\n=========",
	"  +---+\n  |   |\n  O   |\n  |   |\n      |\n=========",
	"  +---+\n  |   |\n  O   |\n /|   |\n      |\n=========",
	"  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n=========",
	"  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n=========",
	"  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n=========",
]

DIFFICULTIES = {
	"1": ("Easy", 8, 150),
	"2": ("Normal", 6, 200),
	"3": ("Hard", 5, 300),
}


def print_header(title):
	print("\n" + "=" * 58)
	print(title.center(58))
	print("=" * 58)


def choose_difficulty():
	print_header("DIFFICULTY")
	print("1. Easy   - 8 wrong guesses")
	print("2. Normal - 6 wrong guesses")
	print("3. Hard   - 5 wrong guesses")

	while True:
		choice = input("Choose a difficulty: ").strip()
		if choice in DIFFICULTIES:
			return DIFFICULTIES[choice]
		print("Please choose 1, 2, or 3.")


def choose_word():
	valid_words = [word.strip().upper() for word in words if word.isalpha()]
	return random.choice(valid_words)


def get_guess(guessed_letters):
	while True:
		guess = input("Guess a letter or type 'hint': ").strip().upper()
		if guess == "HINT":
			return guess
		if len(guess) == 1 and guess in string.ascii_uppercase:
			if guess not in guessed_letters:
				return guess
			print("You already guessed that letter.")
		else:
			print("Enter one letter from A-Z, or type hint.")


def display_word(secret_word, guessed_letters):
	return " ".join(
		letter if letter in guessed_letters else "_"
		for letter in secret_word
	)


def play_game(stats):
	difficulty, max_wrong, points_per_letter = choose_difficulty()
	secret_word = choose_word()
	guessed_letters = set()
	wrong_letters = set()
	hints_left = 1
	score = len(set(secret_word)) * points_per_letter

	print_header(f"HANGMAN - {difficulty.upper()}")
	print(f"The word has {len(secret_word)} letters. You have {hints_left} hint.")

	while len(set(secret_word) - guessed_letters) > 0 and len(wrong_letters) < max_wrong:
		wrong_count = len(wrong_letters)
		drawing_index = min(wrong_count, len(HANGMAN_ART) - 1)
		print(HANGMAN_ART[drawing_index])
		print(f"\nWord: {display_word(secret_word, guessed_letters)}")
		print(f"Wrong guesses: {', '.join(sorted(wrong_letters)) or 'none'}")
		print(f"Guesses remaining: {max_wrong - wrong_count} | Hints: {hints_left}")

		guess = get_guess(guessed_letters)
		if guess == "HINT":
			if hints_left == 0:
				print("You have no hints left.")
				continue
			hidden_letters = set(secret_word) - guessed_letters
			hint_letter = random.choice(sorted(hidden_letters))
			guessed_letters.add(hint_letter)
			hints_left -= 1
			score = max(score - 50, 0)
			print(f"Hint used! The letter {hint_letter} has been revealed.")
			continue

		guessed_letters.add(guess)
		if guess in secret_word:
			print("Correct guess!")
		else:
			wrong_letters.add(guess)
			score = max(score - 25, 0)
			print("That letter is not in the word.")

	if len(set(secret_word) - guessed_letters) == 0:
		print(HANGMAN_ART[len(wrong_letters)])
		print(f"\nCongratulations! You solved the word: {secret_word}")
		print(f"Score: {score}")
		stats["wins"] += 1
		stats["points"] += score
	else:
		print(HANGMAN_ART[-1])
		print(f"\nGame over! The word was: {secret_word}")
		stats["losses"] += 1


def show_stats(stats):
	print_header("SESSION STATISTICS")
	games = stats["wins"] + stats["losses"]
	print(f"Games played: {games}")
	print(f"Games won:    {stats['wins']}")
	print(f"Games lost:   {stats['losses']}")
	print(f"Total points: {stats['points']}")
	if games:
		print(f"Win rate:     {stats['wins'] / games:.0%}")
	else:
		print("Play a game to start tracking statistics.")


def show_help():
	print_header("HOW TO PLAY")
	print("Guess the hidden word one letter at a time.")
	print("Correct letters are revealed; incorrect letters build the hangman.")
	print("You can type hint once per game to reveal a letter, but it costs points.")
	print("Solve the word before you run out of guesses to win.")


def main():
	stats = {"wins": 0, "losses": 0, "points": 0}

	while True:
		print_header("HANGMAN ARENA")
		print("1. Play Hangman")
		print("2. View statistics")
		print("3. How to play")
		print("4. Quit")
		choice = input("Choose an option: ").strip()

		if choice == "1":
			play_game(stats)
		elif choice == "2":
			show_stats(stats)
		elif choice == "3":
			show_help()
		elif choice == "4":
			print("Thanks for playing Hangman!")
			break
		else:
			print("Please choose an option from 1 to 4.")


if __name__ == "__main__":
	main()
