"""CP1404 prac 2, practice

Create more_scores.py and copy in only your function from score.py above.
Now write a main program that uses this function:

Ask the user for a number of scores
Generate that many random numbers (scores) between 0 and 100 inclusive
For each of those scores, write the "result" to a file called results.txt as below:

Example file output for 4 random scores:
66 is Passable
4 is Bad
92 is Excellent
51 is Passable
"""
import random


def main():
    number_of_scores = int(input("How many scores: "))
    with open("results.txt", "w") as out_file:
        for i in range(number_of_scores):
            random_score = random.randint(0, 100)
            result = determine_result(random_score)
            print(random_score, "is", result, file=out_file)


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
