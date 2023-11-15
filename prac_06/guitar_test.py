"""Guitars part 2: Testing"""
from prac_06.guitar import Guitar

CURRENT_YEAR = 2023  # Doesn't affect program, maybe edit class for CURRENT_YEAR to be determined in client code?

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
other = Guitar("another guitar", 2013)

print(f"{gibson.name} get_age() - Expected {101}. Got {gibson.get_age()}")
print(f"{other.name} get_age() - Expected {10}. Got {other.get_age()}")

print(f"{gibson.name} is_vintage() - Expected {True}. Got {gibson.is_vintage()}")
print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")

print(gibson)
print(other)
