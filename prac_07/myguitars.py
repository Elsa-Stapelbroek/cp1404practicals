"""
CP1404 practical 7 - More guitars!

Estimate: 45 minutes
Actual:

Format: Name,Year,Cost
- Write a program to read all of these guitars and store them in a list of Guitar objects, using class.
- Display these using a loop.

- sort the list by year (oldest to newest) and display them in sorted order
    - define how the < operator should work.
    - Write code for the __lt__ (less than) method so that it compares Guitars by year.
    - Then test and see if it sorts correctly now.
"""
from prac_07.guitar import Guitar


def main():
    """Program to order (by year) and display Guitar objects loaded from csv."""
    guitars = load_guitars()
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def load_guitars():
    """Store guitar data from csv as list of Guitar objects."""
    guitars = []
    with open("guitars.csv", 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    return guitars


main()
