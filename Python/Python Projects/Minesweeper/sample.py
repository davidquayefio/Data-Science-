import random


class Board:
    def __init__(self, dim_size, num_bombs):
        if dim_size < 2:
            raise ValueError("Board size must be at least 2.")
        if num_bombs >= dim_size * dim_size:
            raise ValueError("There must be at least one safe square.")

        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set()
        self.flags = set()

    def make_new_board(self):
        board = [[0 for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        positions = random.sample(
            range(self.dim_size * self.dim_size),
            self.num_bombs,
        )

        for position in positions:
            row = position // self.dim_size
            col = position % self.dim_size
            board[row][col] = "*"

        return board

    def assign_values_to_board(self):
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if self.board[row][col] != "*":
                    self.board[row][col] = self.get_num_neighboring_bombs(row, col)

    def get_num_neighboring_bombs(self, row, col):
        count = 0
        for neighbor_row in range(max(0, row - 1), min(self.dim_size, row + 2)):
            for neighbor_col in range(max(0, col - 1), min(self.dim_size, col + 2)):
                if self.board[neighbor_row][neighbor_col] == "*":
                    count += 1
        return count

    def dig(self, row, col):
        if (row, col) in self.flags or (row, col) in self.dug:
            return True
        if self.board[row][col] == "*":
            self.dug.add((row, col))
            return False

        self.dug.add((row, col))
        if self.board[row][col] == 0:
            for neighbor_row in range(max(0, row - 1), min(self.dim_size, row + 2)):
                for neighbor_col in range(max(0, col - 1), min(self.dim_size, col + 2)):
                    if (neighbor_row, neighbor_col) not in self.dug:
                        self.dig(neighbor_row, neighbor_col)
        return True

    def toggle_flag(self, row, col):
        if (row, col) in self.dug:
            return False
        if (row, col) in self.flags:
            self.flags.remove((row, col))
        else:
            self.flags.add((row, col))
        return True

    def has_won(self):
        safe_squares = self.dim_size ** 2 - self.num_bombs
        return len(self.dug) == safe_squares

    def print_board(self, show_mines=False):
        print("\n   " + " ".join(f"{col:2}" for col in range(self.dim_size)))
        for row in range(self.dim_size):
            cells = []
            for col in range(self.dim_size):
                position = (row, col)
                value = self.board[row][col]
                if position in self.flags:
                    display = "F"
                elif position in self.dug or show_mines:
                    display = str(value)
                else:
                    display = "."
                cells.append(f"{display:2}")
            print(f"{row:2} " + " ".join(cells))


def get_coordinates(prompt, board):
    while True:
        try:
            row, col = map(int, input(prompt).split())
            if 0 <= row < board.dim_size and 0 <= col < board.dim_size:
                return row, col
        except ValueError:
            pass
        print(f"Enter two numbers from 0 to {board.dim_size - 1}.")


def play(dim_size=10, num_bombs=10):
    board = Board(dim_size, num_bombs)
    print("\nMINESWEEPER")
    print("Commands: r row col = dig, f row col = flag, q = quit")

    while True:
        board.print_board()
        command = input("\nCommand: ").strip().lower().split()

        if not command:
            print("Enter a command.")
            continue
        if command[0] == "q":
            print("Game ended.")
            return
        if command[0] not in {"r", "f"} or len(command) != 3:
            print("Use r row col, f row col, or q.")
            continue

        try:
            row, col = int(command[1]), int(command[2])
        except ValueError:
            print("Row and column must be numbers.")
            continue

        if not (0 <= row < dim_size and 0 <= col < dim_size):
            print(f"Coordinates must be from 0 to {dim_size - 1}.")
            continue

        if command[0] == "f":
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