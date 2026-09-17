from sample import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        for row in [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]:
            print("| " + " | ".join(row) + " |")

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
            diagonal_one = [self.board[index] for index in (0, 4, 8)]
            diagonal_two = [self.board[index] for index in (2, 4, 6)]
            if all(spot == letter for spot in diagonal_one):
                return True
            if all(spot == letter for spot in diagonal_two):
                return True

        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        print("\nChoose a square by entering its number:")
        game.print_board_nums()

    letter = "X"
    players = {"X": x_player, "O": o_player}

    while game.empty_squares():
        if print_game:
            print("\nCurrent board:")
            game.print_board()

        square = players[letter].get_move(game)
        game.make_move(square, letter)

        if game.current_winner:
            if print_game:
                game.print_board()
                print(f"\n{letter} wins!")
            return letter

        letter = "O" if letter == "X" else "X"

    if print_game:
        game.print_board()
        print("\nIt's a tie!")
    return None


def main():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, and the computer is O.")

    while True:
        game = TicTacToe()
        x_player = HumanPlayer("X")
        o_player = RandomComputerPlayer("O")
        play(game, x_player, o_player)

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
               