"""
CP1404/CP5632 Practical 4 - Walkthrough example
Starter code for cumulative total income program

Line 21 is an exact repeat of line 15 and the +1 range shift is immediately undone by the [month-1] index in line 22.
If still the case after refactoring, maybe experiment with some other approaches (and compare runtimes etc.).
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month:2}: "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
