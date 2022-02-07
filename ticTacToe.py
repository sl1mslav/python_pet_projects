"""
Inverse TicTacToe game with a field of 10x10.
"""

import random
import time


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


board = [f"{(3 - len(str(num))) * ' '}{num}" for num in range(1, 101)]
player_marks = ["X", "0"]


def display_board(board_list):
    """A function designed to display the board."""

    def disp_tile(board_list, index):
        zero = f" | {colored(0, 255, 0, '0')}"
        x = f" | {colored(255, 0, 0, 'X')}"
        element = board_list[index]
        to_print = ""
        if element.strip() == "X":
            to_print += x
        elif element.strip() == "0":
            to_print += zero
        else:
            to_print += f" |{(3 - len(str(element))) * ' '}{element}"
        if index % 10 == 0:
            to_print += "\n"
        print(to_print, end="")

    for i in range(-1, -101, -1):
        disp_tile(board_list, i)


def choose_mark(player_marks):
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
    return not ("X" == board_list[index].strip() or "0" == board_list[index].strip())


def mark_tile(board_list, tile_index, player_mark):
    """This function hacks into the Pentagon."""
    board_list[tile_index] = f"  {player_mark}"


def full_board_marked(board_list):
    """Return if the board is fully marked by either X or 0."""
    return len(set(map(str.strip, board_list))) == 2


def check_win(board_list, index):
    """Checks for a win condition. Or loss, in this case..."""

    # returns True if five of the same markers come in a row in a given list.
    def five_in_row(formed_list):
        if len(formed_list) > 4:
            for i in range(len(formed_list) - 4):
                if formed_list[i].strip() == formed_list[i + 1].strip() == formed_list[i + 2].strip() \
                        == formed_list[i + 3].strip() == formed_list[i + 4].strip():
                    return True
        return False

    # all the numbers in range of 5 horizontally
    def horiz_from(n):
        if n % 10 < 4:
            return n - n % 10
        else:
            return n - 4

    def horiz_to(n):
        if n % 10 > 5:
            return n + 9 - n % 10
        else:
            return n + 4

    # same but vertically
    def vert_to(n):
        if n // 10 > 5:
            return n + 10 * (9 - n // 10)
        else:
            return n + 40

    def vert_from(n):
        if n < 40:
            return n % 10
        else:
            return n - 40

    # same but diagonally
    def diag_right_to(n):
        if n // 10 > 6 or n % 10 < 4:
            return n + 9 * (min(9 - n // 10, n % 10))
        else:
            return n + 36

    def diag_right_from(n):
        if n % 10 > 5 or n // 10 < 4:
            return n - 9 * (min(9 - n % 10, n // 10))
        else:
            return n - 36

    def diag_left_to(n):
        if n % 10 > 5 or n // 10 > 5:
            return n + 11 * min(9 - n // 10, 9 - n % 10)
        else:
            return n + 44

    def diag_left_from(n):
        if n % 10 < 5 or n // 10 < 4:
            return n - 11 * min(n % 10, n // 10)
        else:
            return n - 44

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
    while True:
        while index not in [num for num in range(1, 101)]:
            try:
                index = int(input(f"Player '{chosen_mark}', please choose a tile from 1 to 100: "))
            except ValueError as exc:
                print(f"Incorrect value: {exc}. Please, try again.")

        if check_empty_tile(board_list, index - 1):
            return index - 1
        else:
            print("Whoops, this tile is already marked. Please, choose another.")
            index = 0


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
            f"Player {board_list[index].strip()} has lost! Congratulations, "
            f"player {[x for x in player_marks if x != board_list[index].strip()][0]}!")
        return True
    elif full_board_marked(board_list):
        print("Ladies and gentlemen, it's a draw!")
        return True
    else:
        return False


print("Welcome to the game of inverse TicTacToe")

player_marks = choose_mark(player_marks)
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
            player_marks = choose_mark(player_marks)
            player_mark = player_marks[0]
            computer_mark = player_marks[1]
            current_player_mark = choose_first_turn()
    else:
        current_player_mark = switch_player(current_player_mark)
