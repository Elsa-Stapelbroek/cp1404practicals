"""
CP1404/CP5632 Practical 4 - Walkthrough example
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month:2}: "))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    """Print individual and cumulative incomes for each month."""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, 1):
        total += income  # not sure if printing and tracking total is too much for srp, but struggling to think of a nicer way to do this.
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")  # should maybe put more space between income and total


main()
