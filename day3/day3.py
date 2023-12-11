# Day 3
"""
This script finds and validates part numbers in a schematic.

A valid part number has a symbol next to, above, below, or diagonal to it.
An invalid part number is surrounded by periods in all directions.

The script reads the schematic from a file, finds the coordinates of the part numbers,
validates them, and sums their values.
"""

# PART NUMBERS
# Goal: SUM the value of the part numbers in the schematic.
# A VALID part number has a symbol: [next to, above, below, diagonal to] a number.
# An INVALID part number has only periods surrounding it in all directions.

# THREE STEPS TO VALIDATE
# Step 0: Find the number in x, y space
# Step 1: Is there a symbol next to the number
# Step 2: Is there a symbol above or below the number
# Step 3: Is there a symbol diagonal to the number


def find_number_coordinates(file_content):
    """
    Find the coordinates of the numbers in the schematic.
    :param file_content: list of strings, each string is a line of the schematic
    :return: list of tuples (y, x, length, number)
    """
    _coordinates = []
    start = None
    length = 0
    number = ""
    for y, line in enumerate(file_content):
        for x, char in enumerate(line):
            if char.isdigit():
                if start is None:
                    start = (y, x)
                length += 1
                number += char
            elif start is not None:
                _coordinates.append((*start, length, int(number)))
                start = None
                length = 0
                number = ""
        if start is not None:  # for numbers at the end of a line
            _coordinates.append((*start, length), int(number))
            start = None
            length = 0
            number = ""
    if start is not None:  # handle numbers at the end of the file
        _coordinates.append((*start, length, int(number)))
    return _coordinates  # list of tuples (y, x, length, number)


def validate(file_content, number_coordinates):
    """
    Validates part numbers in a schematic.

    A number is considered valid if it has a symbol (not a digit or a period) in any
    of the 8 directions around it or in its length.

    Parameters:
    :param file_content (list of str): The content of the schematic file, with each
    string representing a line.

    :param number_coordinates (list of tuple): The coordinates of the numbers in the
    schematic. Each tuple contains the y-coordinate, the x-coordinate, the length
    of the number, and the number itself.

    Returns:
    :return: list of int: The list of valid numbers.

    @dev
    Note this function does check inside the number itself, which is unnecessary
    but handled with != .isdigit() in the inner loop.
    """
    _valid_numbers = []
    for y, x, length, number in number_coordinates:
        for dy in [-1, 0, 1]:
            for dx in list(range(-1, length + 1)):
                if dy == dx == 0:  # skip the number itself
                    continue
                ny, nx = y + dy, x + dx
                if (
                    0 <= ny < len(file_content)  # is the new y pos in the file
                    and 0 <= nx < len(file_content[ny])  # is the new x pos in the file
                    and not file_content[ny][nx].isdigit()  # is the new pos a digit
                    and file_content[ny][nx] != "."  # is the new pos a period
                ):
                    _valid_numbers.append(number)
                    break  # no need to check other positions if one is valid
            else:
                continue  # executed if the inner loop completed normally (no break)
            break  # executed if 'continue' was skipped (break)
    return _valid_numbers


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        data = f.readlines()

    coordinates = find_number_coordinates(data)
    valid_numbers = validate(data, coordinates)
    print(sum(valid_numbers))
