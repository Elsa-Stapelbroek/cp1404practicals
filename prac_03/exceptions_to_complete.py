"""
CP1404/CP5632 - Practical 3
Practice exception based error checking.
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)  # "undefined" error warning safe to ignore.
