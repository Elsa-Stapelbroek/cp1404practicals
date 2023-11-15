"""
CP1404/CP5632 - Practical 3
import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""

# Ran each 3 times

# 1. What did you see on line 1? What was the smallest number you could have seen, what was the largest?

# Results: 5, 19, 19
# randomly generated integers between 5 and 20 (inclusive).
# smallest possible: 5, largest possible: 20


# 2. What did you see on line 2? What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?

# Results: 9, 7, 3
# randomly generated integers from range(3,10,2) i.e. 3,5,7,9.
# Smallest possible: 3, largest possible: 9
# No, 4 isn't part of the specified range.


# 3. What did you see on line 3? What was the smallest number you could have seen, what was the largest?

# Results: 4.560573770921391, 2.513656573124826, 4.313822061831662
# randomly generated floats between 2.5 and 5.5 inclusive, each with 15 decimal points (if not specified otherwise).
# Smallest possible: 2.5, largest possible: 5.5


# 4. Write code, not a comment, to produce (print?) a random number (integer?) between 1 and 100 inclusive.
import random
print(random.randint(1, 100))
