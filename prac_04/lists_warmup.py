"""
CP1404/CP5632 Practical 4 - Warm-up

a. numbers[0]
b. numbers[-1]
c. numbers[3]
d. numbers[:-1]
e. numbers[3:4]
f. 5 in numbers
g. 7 in numbers
h. "3" in numbers
i. numbers + [6, 5, 3]
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# a. 3
# b. 2
# c. 1
# d. [3, 1, 4, 1, 5, 9]
# e. 1
# f. True
# g. False
# h. False
# i. [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


# 1. Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"

# 2. Change the last element of numbers to 1
numbers[-1] = 1

# 3. Print all the elements from numbers except the first two (slice)
print(numbers[2:])

# 4. Print whether 9 is an element of numbers
print(9 in numbers)
