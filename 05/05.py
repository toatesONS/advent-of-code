"""
Solutions to Advent of Code day 5
https://adventofcode.com/2022/day/5
"""


from typing import List, Dict

import numpy as np


def parse_input(input_data: str):
    """
    Take input data and convert into a list of instructions and dict
    of crates.
    """

    crate_stacks, instructions = input_data.split('\n\n')
    crate_stacks = parse_crate_stacks(crate_stacks)
    instructions = parse_instructions(instructions)
    return crate_stacks, instructions


def parse_crate_stacks(crate_stacks_str: str) -> Dict[str, List[str]]:
    """
    Take crates diagram in string form and output as dictionary.

    Example input:
    [V]
    [B]     [D]
    [H] [M] [N]
     1   2   3

    Example output:
    {1: ['V', 'B', 'V'],
     2: ['M', '', ''],
     3: ['N', 'D', '']}
    """

    # Reverse so bottom of stacks are first in list
    crate_rows = list(reversed(crate_stacks_str.split('\n')))

    # Split each row into separate columns, then convert to numpy array
    # for easy transpose
    crate_rows = np.array([split_crate_row(crate_row) for crate_row in crate_rows])
    crate_stacks = crate_rows.T.tolist()

    # First item in each stack in stack number, remaining are stacks
    # 'if crate' removes any empty spots with no crate
    return {int(crate_stack[0]): [crate for crate in crate_stack[1:] if crate]
            for crate_stack in crate_stacks}


def split_crate_row(row: str) -> List[str]:
    """
    Split row of crates diagram into separate crates/labels.

    Args:
        row (str): A single row of the crates diagram.
        column_width (int): The number of characters in each columns,
            excluding the gaps between columns.
        gap_length (int): The width of the gap between columns.

    Returns:
        List[str]: List of contents of each column in the given row.
            e.g. ['N', 'D', '']
    """

    return [row[i:i+4].strip().replace('[', '').replace(']', '')
            for i in range(0, len(row), 4)]


def parse_instructions(instructions: str) -> List[Dict[str, int]]:
    """
    Take string of instructions and convert to list of dicts
    Each dict is of format
    {'move': 5, 'from': 3, 'to': 2}
    """

    return [parse_instruction(instruction)
            for instruction in instructions.strip().split('\n')]


def parse_instruction(instruction: str):
    """
    Take single line of instructions and convert to dict
    Output is in form
    {'move': 5, 'from': 3, 'to': 2}
    """

    instruction = instruction.split()
    return {instruction[i]: int(instruction[i+1])
            for i in range(0, len(instruction), 2)}


def follow_instructions(
        crate_stacks: Dict[int, List[str]],
        instructions: List[Dict[str, int]]
) -> Dict[int, List[str]]:
    """
    Follow each instruction to move crates around
    """

    for ins in instructions[0:]:
        for i in range(0, ins['move']):
            crate_stacks[ins['to']].append(crate_stacks[ins['from']].pop(-1))
    return crate_stacks


def follow_instructions_part_2(
        crate_stacks: Dict[int, List[str]],
        instructions: List[Dict[str, int]]
) -> Dict[int, List[str]]:
    """
    Follow each instruction to move crates around
    This time follow part 2 instructions
    """

    for ins in instructions[0:]:
        crates_to_move = []

        # This time pop them off one by one then reverse them before
        # adding to the other stack
        for i in range(0, ins['move']):
            crates_to_move.append(crate_stacks[ins['from']].pop(-1))
        crates_to_move = list(reversed(crates_to_move))
        crate_stacks[ins['to']] += crates_to_move
    return crate_stacks


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        input_data = file.read()

    crate_stacks, instructions = parse_input(input_data)
    crate_stacks = follow_instructions(crate_stacks, instructions)

    print("Top of each stack:")
    print("".join(stack[-1] for stack in crate_stacks.values()))

    crate_stacks, instructions = parse_input(input_data)
    crate_stacks = follow_instructions_part_2(crate_stacks, instructions)

    print("\nTop of each stack in part 2:")
    print("".join(stack[-1] for stack in crate_stacks.values()))
