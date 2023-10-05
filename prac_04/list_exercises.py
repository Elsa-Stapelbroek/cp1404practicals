""" CP1404/CP5632 Practical 4 - Intermediate exercises 1 and 2 """

# 1. Basic list operations: Prompt user for 5 numbers, store in list, output information about numbers.
numbers = [int(input("Number: ")) for i in range(5)]
average = sum(numbers) / len(numbers)

print(f"""The first number is {numbers[0]}
The last number is {numbers[-1]}
The smallest number is {min(numbers)}
The largest number is {max(numbers)}
The average of the numbers is {average}""")
