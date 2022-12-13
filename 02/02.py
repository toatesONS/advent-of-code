from typing import List


def run_part_1():
    moves = read_input_file('input.txt')

    total_score = 0
    for opponent_move, friendly_move in moves:
        opponent_move = convert_move_to_int(opponent_move)
        friendly_move = convert_move_to_int(friendly_move)
        total_score += get_score(opponent_move, friendly_move)

    print(f"Total score (part 1): {total_score}")


def run_part_2():
    moves = read_input_file('input.txt')

    total_score = 0
    for opponent_move, desired_outcome in moves:
        opponent_move = convert_move_to_int(opponent_move)
        friendly_move = get_friendly_move(opponent_move, desired_outcome)
        total_score += get_score(opponent_move, friendly_move)

    print(f"Total score (part 2): {total_score}")


def read_input_file(input_file: str) -> List[List[str]]:
    """
    Read input file and return as individual moves
    Returns list of lists of [opponent's move, friendly move]
    Or for part 2 it is [opponent's move, whether we need to win]
    """

    with open(input_file, 'r') as file:
        input_data = file.read().strip()

    return [line.split() for line in input_data.split('\n')]


def convert_move_to_int(move: str) -> int:
    """
    Convert encoded move to integer form
    rock=1, paper=2, scissors=3
    """

    try:
        return {'A': 1, 'B': 2, 'C': 3}[move]
    except KeyError: # For part 1
        return {'X': 1, 'Y': 2, 'Z': 3}[move]


def get_score(opponent_move: int, friendly_move: int) -> int:
    """
    Get score from single turn of rock paper scissors
    Moves are given as integers, rock=1, paper=2, scissors=3
    """

    return friendly_move + get_score_from_winning(opponent_move, friendly_move)


def get_score_from_winning(opponent_move: int, friendly_move: int) -> int:
    """
    Get score associated with a win, loss or draw
    Ignore scores simply from what friendly player chooses (i.e. ignore
    1 for rock, 2 for scissors, 3 for paper).
    Return 0=lose, 3=draw, 6=win
    Moves are given as integers, rock=1, paper=2, scissors=3
    """

    if opponent_move == friendly_move:
        return 3
    else:
        return (friendly_move == get_winning_move(opponent_move)) * 6


def get_winning_move(opponent_move: int) -> int:
    """
    Figure out which move would beat opponent's move
    Moves are given as integers, rock=1, paper=2, scissors=3
    """

    # Select next item in list, and wrap around if we get to the end
    return [1, 2, 3][opponent_move % 3]


def get_losing_move(opponent_move: int) -> int:
    """
    Figure out which move would lose to opponent's move
    Moves are given as integers, rock=1, paper=2, scissors=3
    """

    # Select previous item in list, and wrap around if we get to the end
    return [1, 2, 3][(opponent_move - 2) % 3]


def get_friendly_move(opponent_move: int, desired_outcome: str) -> int:
    """
    Get which move will result in the desired outcome against opponent
    X = lose
    Y = draw
    Z = win
    """

    if desired_outcome == 'X':
        return get_losing_move(opponent_move)
    elif desired_outcome == 'Y':
        return opponent_move
    else:
        return get_winning_move(opponent_move)


if __name__ == '__main__':
    run_part_1()
    run_part_2()