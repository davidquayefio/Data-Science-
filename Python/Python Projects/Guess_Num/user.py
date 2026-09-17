import random


DIFFICULTIES = {
	"1": ("Easy", 50, 8),
	"2": ("Medium", 100, 7),
	"3": ("Hard", 500, 9),
	"4": ("Expert", 1000, 10),
}


def get_number(prompt, minimum, maximum):
	while True:
		try:
			number = int(input(prompt))
			if minimum <= number <= maximum:
				return number
			print(f"Enter a number from {minimum} to {maximum}.")
		except ValueError:
			print("Please enter a whole number.")


def choose_difficulty():
	print("\nChoose a difficulty:")
	for key, (name, maximum, attempts) in DIFFICULTIES.items():
		print(f"{key}. {name}: 1-{maximum}, {attempts} attempts")

	choice = get_number("Difficulty: ", 1, len(DIFFICULTIES))
	return DIFFICULTIES[str(choice)]


def get_feedback():
	while True:
		feedback = input("Is my guess high, low, or correct? ").strip().lower()
		if feedback in {"high", "h", "too high"}:
			return "high"
		if feedback in {"low", "l", "too low"}:
			return "low"
		if feedback in {"correct", "c", "right"}:
			return "correct"
		print("Please enter high, low, or correct.")


def player_guesses(stats):
	difficulty, maximum, max_attempts = choose_difficulty()
	secret = random.randint(1, maximum)
	score = max_attempts * 100

	print(f"\n{difficulty} mode: guess the number from 1 to {maximum}.")
	print(f"You have {max_attempts} attempts.")

	for attempt in range(1, max_attempts + 1):
		guess = get_number(f"Attempt {attempt}/{max_attempts}: ", 1, maximum)
		if guess == secret:
			points = max(score, 10)
			print(f"\nCorrect! You earned {points} points.")
			stats["wins"] += 1
			stats["points"] += points
			return
		if guess < secret:
			print("Too low.")
		else:
			print("Too high.")
		score -= 100

	print(f"\nOut of attempts! The number was {secret}.")
	stats["losses"] += 1


def computer_guesses(stats):
	_, maximum, _ = choose_difficulty()
	print(f"\nThink of a number from 1 to {maximum}.")
	input("Press Enter when you are ready...")

	low = 1
	high = maximum
	attempts = 0

	while low <= high:
		computer_guess = (low + high) // 2
		attempts += 1
		print(f"\nMy guess is {computer_guess}.")
		feedback = get_feedback()

		if feedback == "correct":
			points = max(1000 - (attempts - 1) * 100, 100)
			print(f"I guessed it in {attempts} attempts and earned {points} points!")
			stats["wins"] += 1
			stats["points"] += points
			return
		if feedback == "low":
			low = computer_guess + 1
		else:
			high = computer_guess - 1

	print("Your clues contradicted each other, so there is no possible number left.")
	stats["losses"] += 1


def show_stats(stats):
	games = stats["wins"] + stats["losses"]
	print("\n========== PLAYER STATS ==========")
	print(f"Games played: {games}")
	print(f"Wins: {stats['wins']}")
	print(f"Losses: {stats['losses']}")
	print(f"Total points: {stats['points']}")
	if games:
		print(f"Win rate: {stats['wins'] / games:.0%}")


def main():
	stats = {"wins": 0, "losses": 0, "points": 0}
	print("=================================")
	print("       NUMBER GUESSER ARENA")
	print("=================================")

	while True:
		print("\n1. Guess the computer's number")
		print("2. Let the computer guess your number")
		print("3. View player stats")
		print("4. Quit")
		choice = get_number("Choose an option: ", 1, 4)

		if choice == 1:
			player_guesses(stats)
		elif choice == 2:
			computer_guesses(stats)
		elif choice == 3:
			show_stats(stats)
		else:
			print("Thanks for playing!")
			break


if __name__ == "__main__":
	main()
