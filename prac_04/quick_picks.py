"""CP1404/CP5632 Practical 4 - Do-from-scratch exercise"""

from random import randint

NUMBERS_IN_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Generate specified number of quick-picks and print neatly."""
    number_of_quick_picks = int(input("How many quick picks? "))
    length_of_maximum = len(str(MAXIMUM))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_IN_LINE):
            number = randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(' '.join(f"{number:{length_of_maximum}}" for number in quick_pick))


main()
