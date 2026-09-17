import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])

    if user not in {'r', 'p', 's'}:
        return 'Invalid choice. Please choose r, p, or s.'

    if user == computer:
        return f"Tie! We both chose {user}."

    def is_win(player, opponent):
        if (player == 'r' and opponent == 's') or (player =='s' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
            return True
        return False

    if is_win(user, computer):
        return f"You win! You chose {user}, and I chose {computer}."
    return f"You lose! You chose {user}, and I chose {computer}."


print(play())