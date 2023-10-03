"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))  # number_of_months might be a better name (not plural or referring to the months themselves)

    for month in range(1, months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))  # replace with f-string; concat not recommended and requires str(month).
        incomes.append(income)  #  maybe say incomes.append((month, income)) instead to avoid repeating line 12. (in which case, reconsider variable name.)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):  # repeating myself to comment on the repetition, but also to note the +1 shift range shift immediately followed by the -1 index shift.
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))  # also make f-string?


main()
