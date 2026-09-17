import copy
import sys


BOARD_TEMPLATE = """
    a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""

WHITE_SQUARE = "||"
BLACK_SQUARE = "  "

PIECES = {
    "wP": "♙",
    "wN": "♘",
    "wB": "♗",
    "wR": "♖",
    "wQ": "♕",
    "wK": "♔",
    "bP": "♟",
    "bN": "♞",
    "bB": "♝",
    "bR": "♜",
    "bQ": "♛",
    "bK": "♚",
}

STARTING_PIECES = {
    "a8": "♜", "b8": "♞", "c8": "♝", "d8": "♛",
    "e8": "♚", "f8": "♝", "g8": "♞", "h8": "♜",
    "a7": "♟", "b7": "♟", "c7": "♟", "d7": "♟",
    "e7": "♟", "f7": "♟", "g7": "♟", "h7": "♟",
    "a2": "♙", "b2": "♙", "c2": "♙", "d2": "♙",
    "e2": "♙", "f2": "♙", "g2": "♙", "h2": "♙",
    "a1": "♖", "b1": "♘", "c1": "♗", "d1": "♕",
    "e1": "♔", "f1": "♗", "g1": "♘", "h1": "♖",
}


def print_chessboard(board):
    squares = []
    is_white_square = True

    for rank in "87654321":
        for file in "abcdefgh":
            position = file + rank

            if position in board:
                squares.append(board[position])
            elif is_white_square:
                squares.append(WHITE_SQUARE)
            else:
                squares.append(BLACK_SQUARE)

            is_white_square = not is_white_square

        is_white_square = not is_white_square

    print(BOARD_TEMPLATE.format(*squares))


def valid_position(position):
    return (
        len(position) == 2
        and position[0] in "abcdefgh"
        and position[1] in "12345678"
    )


def main():
    main_board = copy.deepcopy(STARTING_PIECES)

    print("Interactive Chessboard")
    print("Commands:")
    print("  move e2 e4")
    print("  remove e2")
    print("  set e2 wP")
    print("  reset")
    print("  clear")
    print("  fill wP")
    print("  quit")

    while True:
        print_chessboard(main_board)
        response = input("> ").strip().split()

        if not response:
            continue

        command = response[0].lower()

        try:
            if command == "move" and len(response) == 3:
                source, destination = response[1], response[2]

                if not valid_position(source) or not valid_position(destination):
                    print("Invalid position.")
                elif source not in main_board:
                    print(f"No piece at {source}.")
                else:
                    main_board[destination] = main_board.pop(source)

            elif command == "remove" and len(response) == 2:
                position = response[1]

                if valid_position(position):
                    main_board.pop(position, None)
                else:
                    print("Invalid position.")

            elif command == "set" and len(response) == 3:
                position, piece = response[1], response[2]

                if not valid_position(position) or piece not in PIECES:
                    print("Use a valid position and piece, such as e2 wP.")
                else:
                    main_board[position] = PIECES[piece]

            elif command == "reset":
                main_board = copy.deepcopy(STARTING_PIECES)

            elif command == "clear":
                main_board.clear()

            elif command == "fill" and len(response) == 2:
                piece = response[1]

                if piece not in PIECES:
                    print("Invalid piece. Example: fill wP")
                else:
                    main_board = {
                        file + rank: PIECES[piece]
                        for rank in "12345678"
                        for file in "abcdefgh"
                    }

            elif command == "quit":
                sys.exit()

            else:
                print("Invalid command.")

        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()