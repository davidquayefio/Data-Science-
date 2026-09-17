import random
import time


DIFFICULTIES = {
	"1": ("Easy", 50, 8),
	"2": ("Normal", 100, 10),
	"3": ("Hard", 500, 12),
}


def binary_search(values, target):
	"""Return the target index and number of comparisons."""
	low = 0
	high = len(values) - 1
	comparisons = 0

	while low <= high:
		midpoint = (low + high) // 2
		comparisons += 1

		if values[midpoint] == target:
			return midpoint, comparisons
		if target < values[midpoint]:
			high = midpoint - 1
		else:
			low = midpoint + 1

	return -1, comparisons


def linear_search(values, target):
	"""Return the target index and number of comparisons."""
	for comparisons, value in enumerate(values, start=1):
		if value == target:
			return comparisons - 1, comparisons
	return -1, len(values)


def header(title):
	print("\n" + "=" * 60)
	print(title.center(60))
	print("=" * 60)


def get_integer(prompt, minimum=None, maximum=None):
	while True:
		try:
			value = int(input(prompt).strip())
			if minimum is not None and value < minimum:
				raise ValueError
			if maximum is not None and value > maximum:
				raise ValueError
			return value
		except ValueError:
			limits = ""
			if minimum is not None and maximum is not None:
				limits = f" from {minimum} to {maximum}"
			elif minimum is not None:
				limits = f" greater than or equal to {minimum}"
			print(f"Enter a whole number{limits}.")


def choose_difficulty():
	header("DIFFICULTY")
	for key, (name, maximum, attempts) in DIFFICULTIES.items():
		print(f"{key}. {name}: numbers from 1 to {maximum}, {attempts} attempts")
	choice = input("Choose a difficulty: ").strip()
	while choice not in DIFFICULTIES:
		choice = input("Choose 1, 2, or 3: ").strip()
	return DIFFICULTIES[choice]


def computer_search_game(stats):
	name, maximum, _ = choose_difficulty()
	low = 1
	high = maximum
	attempts = 0

	header(f"COMPUTER BINARY SEARCH - {name.upper()}")
	print(f"Think of a number from 1 to {maximum}.")
	input("Press Enter when you are ready...")

	while low <= high:
		guess = (low + high) // 2
		attempts += 1
		print(f"\nMy binary-search guess is: {guess}")
		answer = input("Is it high, low, or correct? ").strip().lower()

		if answer in {"correct", "c", "right"}:
			print(f"I found it in {attempts} comparisons!")
			stats["wins"] += 1
			stats["comparisons"] += attempts
			return
		if answer in {"low", "l"}:
			low = guess + 1
		elif answer in {"high", "h"}:
			high = guess - 1
		else:
			print("Enter high, low, or correct.")

	print("Your clues were inconsistent, so no number is possible.")
	stats["losses"] += 1


def player_search_game(stats):
	name, maximum, attempts_limit = choose_difficulty()
	values = list(range(1, maximum + 1))
	target = random.choice(values)
	low = 0
	high = maximum - 1
	attempts = 0

	header(f"PLAYER BINARY SEARCH - {name.upper()}")
	print(f"Find the hidden number from 1 to {maximum}.")
	print("Use the displayed midpoint to practice the binary-search strategy.")

	while low <= high and attempts < attempts_limit:
		midpoint = (low + high) // 2
		suggested = values[midpoint]
		print(f"\nSuggested midpoint: {suggested}")
		guess = get_integer(
			f"Your guess ({attempts + 1}/{attempts_limit}): ",
			1,
			maximum,
		)
		attempts += 1

		if guess == target:
			print(f"Correct! You found {target} in {attempts} guesses.")
			stats["wins"] += 1
			stats["comparisons"] += attempts
			return
		if guess < target:
			print("Too low. The target is higher.")
			low = max(low, guess)
		else:
			print("Too high. The target is lower.")
			high = min(high, guess - 2)

	print(f"Out of guesses. The hidden number was {target}.")
	stats["losses"] += 1


def benchmark():
	header("SEARCH SPEED CHALLENGE")
	size = get_integer("How many sorted numbers should be tested? ", 10, 100000)
	values = list(range(size))
	targets = random.sample(values, min(size, 1000))

	start = time.perf_counter()
	for target in targets:
		linear_search(values, target)
	linear_time = time.perf_counter() - start

	start = time.perf_counter()
	for target in targets:
		binary_search(values, target)
	binary_time = time.perf_counter() - start

	print(f"Linear search time:  {linear_time:.6f} seconds")
	print(f"Binary search time:  {binary_time:.6f} seconds")
	if binary_time:
		print(f"Binary search was about {linear_time / binary_time:.1f}x faster.")


def show_stats(stats):
	games = stats["wins"] + stats["losses"]
	header("SESSION STATISTICS")
	print(f"Games played:       {games}")
	print(f"Games won:          {stats['wins']}")
	print(f"Games lost:         {stats['losses']}")
	print(f"Total comparisons:  {stats['comparisons']}")
	if games:
		print(f"Win rate:           {stats['wins'] / games:.0%}")


def main():
	stats = {"wins": 0, "losses": 0, "comparisons": 0}

	while True:
		header("BINARY SEARCH ARENA")
		print("1. Let the computer find your number")
		print("2. Find the computer's hidden number")
		print("3. Compare search speeds")
		print("4. View statistics")
		print("5. Quit")
		choice = input("Choose an option: ").strip()

		if choice == "1":
			computer_search_game(stats)
		elif choice == "2":
			player_search_game(stats)
		elif choice == "3":
			benchmark()
		elif choice == "4":
			show_stats(stats)
		elif choice == "5":
			print("Thanks for playing Binary Search Arena!")
			break
		else:
			print("Please choose an option from 1 to 5.")


if __name__ == "__main__":
	main()
