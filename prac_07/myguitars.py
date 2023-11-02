"""
CP1404 practical 7 - More guitars!

Estimate: 45 minutes
Actual: ~50 minutes

Format: Name,Year,Cost
- Write a program to read all of these guitars and store them in a list of Guitar objects, using class.
- Display these using a loop.

- sort the list by year (oldest to newest) and display them in sorted order
    - define how the < operator should work.
    - Write code for the __lt__ (less than) method so that it compares Guitars by year.
    - Then test and see if it sorts correctly now.

- Add to your program to ask the user to enter their new guitars (just like your program from an earlier prac).
    - Store these new guitars in your list of guitar objects, then
    - write all of your guitars to the data file guitars.csv.
- Test that this worked by opening the data file, and by running the program again to make sure it reads new guitars.
"""
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Program to order (by year) and display Guitar objects loaded from csv."""
    guitars = load_guitars()
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    get_more_guitars(guitars)
    save_guitars(guitars)


def load_guitars():
    """Store guitar data from csv as list of Guitar objects."""
    guitars = []
    with open(FILENAME, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    return guitars


def get_more_guitars(guitars):
    """Add guitars from user input to list until given an empty name."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")


def save_guitars(guitars):
    """Save updated guitar list to csv."""
    with open(FILENAME, 'w') as out_file:
        for guitar in guitars:
            print(guitar.name, guitar.year, guitar.cost, sep=',', file=out_file)


main()
