"""
CP1404 practical 7 - More guitars!

Estimate: 45 minutes
Actual: ~50 minutes
"""
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Program to load, order (by year), and display list of Guitars from csv."""
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
    """Ask user for Guitars to add to list, until name is left empty."""
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
