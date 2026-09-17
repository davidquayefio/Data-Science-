from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


class TicTacToe:
	def __init__(self):
		self.board = [" " for _ in range(9)]
		self.current_winner = None

	def print_board(self):
		print("\n" + "\n---+---+---\n".join(
			" {} | {} | {} ".format(*self.board[index:index + 3])
			for index in range(0, 9, 3)
		))

	@staticmethod
	def print_board_numbers():
		print("\n" + "\n---+---+---\n".join(
			" {} | {} | {} ".format(*range(index, index + 3))
			for index in range(0, 9, 3)
		))

	def available_moves(self):
		return [index for index, spot in enumerate(self.board) if spot == " "]

	def empty_squares(self):
		return " " in self.board

	def make_move(self, square, letter):
		if square not in self.available_moves():
			return False

		self.board[square] = letter
		if self.winner(square, letter):
			self.current_winner = letter
		return True

	def winner(self, square, letter):
		row_index = square // 3
		row = self.board[row_index * 3:(row_index + 1) * 3]
		if all(spot == letter for spot in row):
			return True

		column_index = square % 3
		column = [self.board[column_index + index * 3] for index in range(3)]
		if all(spot == letter for spot in column):
			return True

		if square % 2 == 0:
			diagonals = ([0, 4, 8], [2, 4, 6])
			return any(
				all(self.board[index] == letter for index in diagonal)
				for diagonal in diagonals
			)

		return False


def choose_opponent():
	print("\nChoose your opponent:")
	print("1. Random computer")
	print("2. Smart computer")

	while True:
		choice = input("Opponent: ").strip()
		if choice == "1":
			return RandomComputerPlayer("O")
		if choice == "2":
			return SmartComputerPlayer("O")
		print("Please choose 1 or 2.")


def play_game(stats):
	game = TicTacToe()
	human = HumanPlayer("X")
	computer = choose_opponent()
	players = {"X": human, "O": computer}
	current_letter = "X"

	print("\nChoose a square using its number:")
	game.print_board_numbers()

	while game.empty_squares():
		game.print_board()
		current_player = players[current_letter]
		square = current_player.get_move(game)
		game.make_move(square, current_letter)

		if game.current_winner:
			game.print_board()
			print(f"\n{current_letter} wins!")
			stats[current_letter] += 1
			return current_letter

		current_letter = "O" if current_letter == "X" else "X"

	game.print_board()
	print("\nIt's a tie!")
	stats["ties"] += 1
	return "tie"


def show_stats(stats):
	games = stats["X"] + stats["O"] + stats["ties"]
	print("\n========== SESSION SCORE ==========")
	print(f"Games played: {games}")
	print(f"You wins:     {stats['X']}")
	print(f"Computer wins:{stats['O']}")
	print(f"Ties:         {stats['ties']}")


def show_help():
	print("\n========== HOW TO PLAY ==========")
	print("You play as X. The computer plays as O.")
	print("Choose a numbered empty square to place your mark.")
	print("Get three marks in a row, column, or diagonal to win.")
	print("The smart computer uses a strategy that cannot be beaten.")


def main():
	print("Welcome to Tic-Tac-Toe!")
	print("You are X, and the computer is O.")
	stats = {"X": 0, "O": 0, "ties": 0}

	while True:
		print("\n1. Play game")
		print("2. View score")
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
			print("Thanks for playing!")
			break
		else:
			print("Please choose an option from 1 to 4.")


if __name__ == "__main__":
	main()
