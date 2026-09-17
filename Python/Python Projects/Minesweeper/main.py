from sample import Board


def read_command(board):
	while True:
		parts = input("\nCommand: ").strip().lower().split()

		if parts and parts[0] == "q":
			return "quit", None, None

		if len(parts) != 3 or parts[0] not in {"r", "f"}:
			print("Use r row col to reveal, f row col to flag, or q to quit.")
			continue

		try:
			row, col = int(parts[1]), int(parts[2])
		except ValueError:
			print("Row and column must be numbers.")
			continue

		if not (0 <= row < board.dim_size and 0 <= col < board.dim_size):
			print(f"Coordinates must be from 0 to {board.dim_size - 1}.")
			continue

		return parts[0], row, col


def play(dim_size=10, num_bombs=10):
	board = Board(dim_size, num_bombs)

	print("\nMINESWEEPER")
	print("Reveal every safe square without hitting a mine.")
	print("Commands: r row col = reveal, f row col = flag, q = quit")

	while True:
		board.print_board()
		command, row, col = read_command(board)

		if command == "quit":
			print("Game ended.")
			return

		if command == "f":
			board.toggle_flag(row, col)
			continue

		if not board.dig(row, col):
			board.print_board(show_mines=True)
			print("\nYou hit a mine. Game over!")
			return

		if board.has_won():
			board.print_board(show_mines=True)
			print("\nCongratulations! You cleared the board!")
			return


if __name__ == "__main__":
	play()
