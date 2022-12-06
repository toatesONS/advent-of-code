"""
Solutions to Advent of Code day 6
https://adventofcode.com/2022/day/6
"""


def part1(input_data: str) -> int:
    """Get location of first start-of-packet marker"""
    return find_marker(input_data, 4)


def part2(input_data: str) -> int:
    """Get location of first start-of-message marker"""
    return find_marker(input_data, 14)


def find_marker(input_data: str, marker_length: int) -> int:
    """
    Find location of end of first marker in string.
    This is the number of characters from the beginning of the input
    to the end of the first set of unique characters of length
    market_length.

    Args:
        input_data (str): input data to search.
        marker_length (int): The number of unique characters that must
            be seen in a row to indicate the marker.

    Returns:
        int: First time marker
    """

    for i in range(0, len(input_data)):
        substr = input_data[i:i+marker_length]
        if len(set(substr)) == marker_length:
            return i + marker_length


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_data = file.read()

    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")