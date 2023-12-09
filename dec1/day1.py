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


def concat_digits(string):
    new_string = ""
    for i in string:
        if i.isdigit():
            new_string += i
    return int(new_string[0] + new_string[-1])


with open("./input.txt", "r") as f:
    # read each test case and put it into a list
    cases = f.read().splitlines()

    # initialize the sum
    total = 0

    # for each case, concatenate the digits and add to the total
    for i in cases:
        total += concat_digits(i)

    print(total)
