"""CP1404 prac 2, exercise 2.2"""

import random


def main():
    """Determine results of scores from user input and random generator."""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)
    random_score = random.uniform(0, 100)
    random_result = determine_result(random_score)
    print(random_result)


def determine_result(score):
    """Determine result based on score."""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
