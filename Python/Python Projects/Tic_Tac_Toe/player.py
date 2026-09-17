import random


class Player:
	def __init__(self, letter):
		self.letter = letter

	def get_move(self, game):
		raise NotImplementedError


class HumanPlayer(Player):
	def get_move(self, game):
		while True:
			choice = input(
				f"{self.letter}'s turn. Choose a square from 0 to 8: "
			).strip()

			try:
				square = int(choice)
			except ValueError:
				print("Please enter a whole number from 0 to 8.")
				continue

			if square in game.available_moves():
				return square

			print("That square is unavailable. Choose an empty square.")


class RandomComputerPlayer(Player):
	def get_move(self, game):
		square = random.choice(game.available_moves())
		print(f"Computer chooses square {square}.")
		return square


class SmartComputerPlayer(Player):
	def get_move(self, game):
		print("Computer is thinking...")
		score, square = self.minimax(game, self.letter)
		print(f"Computer chooses square {square}.")
		return square

	def minimax(self, game, player):
		available_moves = game.available_moves()

		if game.current_winner == "O":
			return 1, None
		if game.current_winner == "X":
			return -1, None
		if not available_moves:
			return 0, None

		if player == "O":
			best_score = -2
			best_move = None
			for move in available_moves:
				game.board[move] = "O"
				if game.winner(move, "O"):
					game.current_winner = "O"
				score, _ = self.minimax(game, "X")
				game.board[move] = " "
				game.current_winner = None

				if score > best_score:
					best_score = score
					best_move = move
			return best_score, best_move

		best_score = 2
		best_move = None
		for move in available_moves:
			game.board[move] = "X"
			if game.winner(move, "X"):
				game.current_winner = "X"
			score, _ = self.minimax(game, "O")
			game.board[move] = " "
			game.current_winner = None

			if score < best_score:
				best_score = score
				best_move = move
		return best_score, best_move
