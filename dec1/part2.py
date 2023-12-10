# DAY 1 - December 1 2023
# What is the sum of all of the calibration values?

# Each line is the concat of first digit and last digit to form a two-digit number.
# Example
# 1abc2 = 12.
# pqr3stu8vwx = 38
# a1b2c3d4e5f = 15
# treb7uchet = 77
# sum is 142

# Goal: for any given string input:
# - find the first digit
# - find the last digit
# - add them together
# - add this value to the total sum

# Part 2
import re

# Spelled numbers also count as valid numbers.
spelled = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# Map each spelled number to its digit
spelled_mapping = {word: index + 1 for index, word in enumerate(spelled)}
# returns a dictionary like {'one': 1, 'two': 2, ...}


def concat_digits(string):
    new_string = ""
    for i in string:
        if i.isdigit():
            new_string += i
    return int(new_string[0] + new_string[-1])


def replace_match(match):
    return str(spelled_mapping[match.group(0)])


def string_replace(string):
    # Create a pattern that matches any of the words
    pattern = re.compile("|".join(spelled_mapping.keys()))

    # Use re.sub to replace the words with digits
    string = pattern.sub(replace_match, string)
    return string


with open("./input.txt", "r") as f:
    # read each test case and put it into a list
    cases = f.read().splitlines()

    # initialize the sum
    total = 0

    # part 2: replace each spelled number with its digit first
    for i, case in enumerate(cases):
        cases[i] = string_replace(case)

    # for each case, concatenate the digits and add to the total
    for case in cases:
        total += concat_digits(case)

    print(total)
