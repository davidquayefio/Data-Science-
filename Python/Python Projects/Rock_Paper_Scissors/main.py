import random


MOVES = {
	"r": "Rock",
	"p": "Paper",
	"s": "Scissors",
}

BEATS = {
	"r": "s",
	"p": "r",
	"s": "p",
}

DIFFICULTIES = {
	"1": ("Easy", 0.0),
	"2": ("Normal", 0.25),
	"3": ("Hard", 0.65),
}


def print_header(title):
	print("\n" + "=" * 52)
	print(title.center(52))
	print("=" * 52)


def get_choice(prompt, choices):
	while True:
		choice = input(prompt).strip().lower()
		if choice in choices:
			return choice
		print(f"Choose one of: {', '.join(choices)}")


def get_number(prompt, minimum, maximum):
	while True:
		try:
			number = int(input(prompt).strip())
			if minimum <= number <= maximum:
				return number
			print(f"Enter a number from {minimum} to {maximum}.")
		except ValueError:
			print("Please enter a whole number.")


def choose_difficulty():
	print_header("DIFFICULTY")
	for key, (name, prediction_chance) in DIFFICULTIES.items():
		description = f"{int(prediction_chance * 100)}% counter-pick chance"
		print(f"{key}. {name:<8} ({description})")
	choice = get_choice("Difficulty: ", DIFFICULTIES)
	return DIFFICULTIES[choice]


def choose_match_type():
	print_header("MATCH TYPE")
	print("1. Single round")
	print("2. Best of 3")
	print("3. Best of 5")
	choice = get_choice("Match type: ", {"1", "2", "3"})
	return {"1": 1, "2": 3, "3": 5}[choice]


def get_computer_move(user_move, prediction_chance):
	if user_move and random.random() < prediction_chance:
		return BEATS[user_move]
	return random.choice(list(MOVES))


def result_for(user_move, computer_move):
	if user_move == computer_move:
		return "tie"
	if BEATS[user_move] == computer_move:
		return "win"
	return "loss"


def show_round(user_move, computer_move, result):
	print(f"\nYou chose:      {MOVES[user_move]}")
	print(f"Computer chose: {MOVES[computer_move]}")
	if result == "win":
		print("Result: You win this round!")
	elif result == "loss":
		print("Result: The computer wins this round.")
	else:
		print("Result: This round is a tie.")


def play_match(stats):
	difficulty, prediction_chance = choose_difficulty()
	rounds_to_play = choose_match_type()
	rounds_needed = rounds_to_play // 2 + 1
	user_score = 0
	computer_score = 0
	ties = 0
	streak = 0
	best_streak = 0

	print_header(f"ROCK PAPER SCISSORS: {difficulty.upper()}")
	print("Enter r for Rock, p for Paper, or s for Scissors.")
	print(f"First to {rounds_needed} wins takes the match.")

	while user_score < rounds_needed and computer_score < rounds_needed:
		print(f"\nScore: You {user_score} - {computer_score} Computer | Ties: {ties}")
		user_move = get_choice("Your move: ", set(MOVES))
		computer_move = get_computer_move(user_move, prediction_chance)
		result = result_for(user_move, computer_move)
		show_round(user_move, computer_move, result)

		if result == "win":
			user_score += 1
			streak += 1
			best_streak = max(best_streak, streak)
		elif result == "loss":
			computer_score += 1
			streak = 0
		else:
			ties += 1

	print_header("MATCH COMPLETE")
	if user_score > computer_score:
		print(f"You won the match {user_score}-{computer_score}!")
		stats["wins"] += 1
	else:
		print(f"The computer won the match {computer_score}-{user_score}.")
		stats["losses"] += 1
	print(f"Rounds: {user_score + computer_score + ties} | Best streak: {best_streak}")
	print(f"Difficulty: {difficulty}")
	stats["rounds"] += user_score + computer_score + ties
	stats["ties"] += ties
	stats["best_streak"] = max(stats["best_streak"], best_streak)


def show_stats(stats):
	print_header("SESSION STATISTICS")
	matches = stats["wins"] + stats["losses"]
	print(f"Matches played: {matches}")
	print(f"Matches won:    {stats['wins']}")
	print(f"Matches lost:   {stats['losses']}")
	print(f"Rounds played:  {stats['rounds']}")
	print(f"Round ties:     {stats['ties']}")
	print(f"Best win streak: {stats['best_streak']}")
	if matches:
		print(f"Match win rate:  {stats['wins'] / matches:.0%}")
	else:
		print("Play a match to start tracking your statistics.")


def show_help():
	print_header("HOW TO PLAY")
	print("Rock beats Scissors.")
	print("Scissors beats Paper.")
	print("Paper beats Rock.")
	print("Choose a move each round, and win enough rounds to take the match.")
	print("Hard mode gives the computer a better chance to counter your move.")


def main():
	stats = {"wins": 0, "losses": 0, "rounds": 0, "ties": 0, "best_streak": 0}

	while True:
		print_header("ROCK PAPER SCISSORS ARENA")
		print("1. Play a match")
		print("2. View statistics")
		print("3. How to play")
		print("4. Quit")
		choice = get_choice("Select an option: ", {"1", "2", "3", "4"})

		if choice == "1":
			play_match(stats)
		elif choice == "2":
			show_stats(stats)
		elif choice == "3":
			show_help()
		else:
			print("\nThanks for playing!")
			break


if __name__ == "__main__":
	main()
