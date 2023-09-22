"""CP1404 prac 2, exercise 3"""

MENU = """(G)et score 
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Get valid score from user and apply function chosen from menu."""
    print(MENU)
    choice = input(">>>: ").upper()
    score = get_valid_score()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(result)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice!")
        print(MENU)
        choice = input(">>>: ").upper()
    print("farewell")


def get_valid_score():
    """Get score in valid range from user input."""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score!")
        score = int(input("Score: "))
    return score


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


def show_stars(score):
    """Print line of stars of same length as score."""
    print(score * "*")


main()
