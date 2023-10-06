"""CP1404 prac 2, practice

Create more_scores.py and copy in only your function from score.py above. Now write a main program that uses this function:

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


# def main():
#     """Determine results of scores from user input and random generator."""
#     score = float(input("Enter score: "))
#     result = determine_result(score)
#     print(result)
#     random_score = random.uniform(0, 100)
#     random_result = determine_result(random_score)
#     print(random_result)
"""
OUTPUT_FILE =
def main():
    get_number_of_scores():
    generate_scores()
    
    number_of_scores = int(input("How many scores: "))
    out_file = open(OUTPUT_FILE, 'w')
    
    
    
    
"""
def main():
    number_of_scores = int(input("How many scores: "))
    for i in range(number_of_scores):
        random_score = generate_score()
        determine_result(random_score)



def generate_score():
    random_score = random.uniform(0, 100)
    return random_score


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

def write_to_txt(filename):
    out_file = open(filename, "w")


main()
