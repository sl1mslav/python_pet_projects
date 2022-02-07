"""
Inverse TicTacToe game with a field of 10x10.
"""

import random
import time

board = [f"{(3 - len(str(num))) * ' '}{num}" for num in range(1, 101)]
player_marks = ['X', '0']


def display_board(board_list):
    """A function designed to display the board."""
    for i in range(1, 101, 10):
        print(' | '.join(board_list[-i:-i - 10:-1]))


def choose_mark():
    """A function which returns the player's chosen marker, and then the computer's."""
    chosen_mark = ""
    while chosen_mark not in player_marks:
        chosen_mark = input("Would you like to play with X or 0? \nType 'X' or '0':\n").upper()
    return chosen_mark, [x for x in player_marks if x != chosen_mark][0]


def choose_first_turn():
    """Randomly return whose turn will be the first."""
    return player_marks[random.choice((0, 1))]


def check_empty_tile(board_list, index):
    """Check if a tile is empty. I doubt some of these functions even need comments."""
    return not ("X" in board_list[index] or "0" in board_list[index])


def mark_tile(board_list, tile_index, player_mark):
    """This function hacks into the Pentagon."""
    board_list[tile_index] = f"  {player_mark}"


def full_board_marked(board_list):
    """Return if the board is fully marked by either X or 0."""
    return len(set(map(str.strip, board_list))) == 2


def check_win(board_list, index):
    """Checks for a win condition. Or loss, in this case..."""

    # returns True if five of the same markers come in a row in a given list.
    def five_in_row(l):
        if len(l) > 4:
            for i in range(len(l) - 4):
                if l[i].strip() == l[i + 1].strip() == l[i + 2].strip() == l[i + 3].strip() == l[i + 4].strip():
                    return True
        return False

    # all the numbers in range of 5 horizontally
    horiz_from = lambda n: n - n % 10 if n % 10 < 4 else n - 4
    horiz_to = lambda n: n + 9 - n % 10 if n % 10 > 5 else n + 4

    # same but vertically
    vert_to = lambda n: n + 10 * (9 - n // 10) if n // 10 > 5 else n + 40
    vert_from = lambda n: n % 10 if n < 40 else n - 40

    # same but diagonally
    diag_right_to = lambda n: n + 9 * (min(9 - n // 10, n % 10)) if n // 10 > 6 or n % 10 < 4 else n + 36
    diag_right_from = lambda n: n - 9 * (min(9 - n % 10, n // 10)) if n % 10 > 5 or n // 10 < 4 else n - 36
    diag_left_to = lambda n: n + 11 * min(9 - n // 10, 9 - n % 10) if n % 10 > 5 or n // 10 > 5 else n + 44
    diag_left_from = lambda n: n - 11 * min(n % 10, n // 10) if n % 10 < 5 or n // 10 < 4 else n - 44

    return (
            five_in_row(board_list[horiz_from(index):horiz_to(index) + 1])
            or five_in_row(board_list[vert_from(index):vert_to(index) + 1:10])
            or five_in_row(board_list[diag_right_from(index):diag_right_to(index) + 1:9])
            or five_in_row(board_list[diag_left_from(index):diag_left_to(index) + 1: 11])
    )


def ai_turn(board_list, computer_mark):
    """Simulates a turn of an AI. The game would be very long if it constantly checked for a win (loss) condition
    in the chosen tile, so I made it randomly choose an empty one so as not to bore the player."""
    while True:
        tile_index = random.randint(1, 100)
        if check_empty_tile(board_list, tile_index - 1):
            mark_tile(board_list, tile_index - 1, computer_mark)
            break
    print("Thinking...")
    time.sleep(1.5)
    print(f"Computer has chosen tile {tile_index}")
    return tile_index - 1


def player_choice(board_list, chosen_mark):
    """Lets the player choose the next available tile to mark."""

    index = 0

    while index not in [num for num in range(1, 101)]:
        try:
            index = int(input(f"Player '{chosen_mark}', please choose a tile from 1 to 100: "))
        except ValueError as exc:
            print(f"Incorrect value: {exc}. Please, try again.")

    if check_empty_tile(board_list, index - 1):
        return index - 1

    return False


def replay():
    """Suggest a replay of the game"""

    decision = ""
    while decision not in ('yes', 'no'):
        decision = input(
            "Would you like to give it another go? Type 'yes' or 'no'\n"
        ).lower()

    return decision == 'yes'


def clear_screen():
    """Clearing the screen by adding new lines"""
    print('\n' * 2)


def switch_player(chosen_mark):
    """Switching the player's role"""
    return '0' if chosen_mark == 'X' else 'X'


def check_game_finished(board_list, index):
    if check_win(board_list, index):
        print(
            f"Player {board_list[index].strip()} has lost! Congratulations, player {[x for x in player_marks if x != board_list[index].strip()][0]}!")
        return True
    elif full_board_marked(board_list):
        print("Ladies and gentlemen, it's a draw!")
        return True
    else:
        return False


print("Welcome to the game of inverse TicTacToe")

player_marks = choose_mark()
player_mark = player_marks[0]
computer_mark = player_marks[1]
current_player_mark = choose_first_turn()

print(f"Player '{current_player_mark}' goes first.")
print("Initial field: \n")
while True:
    display_board(board)
    print(f"Now it's the turn of player '{current_player_mark}':")
    if current_player_mark == computer_mark:
        player_position = ai_turn(board, computer_mark)
        clear_screen()
    else:
        player_position = player_choice(board, current_player_mark)
        mark_tile(board, player_position, current_player_mark)
        clear_screen()

    if check_game_finished(board, player_position):
        display_board(board)
        if not replay():
            break
        else:
            board = [f"{(3 - len(str(num))) * ' '}{num}" for num in range(1, 101)]
            player_marks = choose_mark()
            current_player_mark = choose_first_turn()
    else:
        current_player_mark = switch_player(current_player_mark)
