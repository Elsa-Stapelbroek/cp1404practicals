"""
CP1404/CP5632 - Practical 3
Answer the following questions:
1. When will a ValueError occur?
    When the input isn't recognised as an integer (eg: 2.53, 1.0, seven)
2. When will a ZeroDivisionError occur?
    When the denominator is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Add while loop (following error-checking pattern) that asks for a different input if the denominator input is 0.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
