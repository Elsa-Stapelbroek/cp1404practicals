"""CP1404/CP5632 Practical 4 - Do-from-scratch exercise
MAIN:
ask input
generate lines
print
"""
import random


NUMBERS_IN_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        quick_pick = generate_numbers()


def generate_numbers():
    """Generate sequence containing specified amount of non-repeating numbers."""
    numbers = []
    while len(numbers) < NUMBERS_IN_LINE:
        number = random.randint(MINIMUM, MAXIMUM)
        if number not in numbers:
            numbers.append(number)
    return numbers


main()
