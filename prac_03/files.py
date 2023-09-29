"""
Make sure you're confident with:

read()
readline()
readlines()
for line in file

"""
# 1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.

name = input("Name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# 2. (In the same file, but as if it were a separate program) Write code that opens "name.txt" and reads the name
# (as above) then prints, "Your name is Bob"

in_file = open("name.txt", 'r')
name = in_file.read()
print(f"Your name is {name}")
in_file.close()

# 3. Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on
# separate lines in the file and save it:
# 17
# 42
# 400
# Write code that opens "numbers.txt", reads only the first two numbers
# and adds them together then prints the result, which should be... 59.

with open("numbers.txt", 'r') as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
print(first_number + second_number)


# 4. Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of
# numbers.

with open("numbers.txt", 'r') as in_file:
    total = 0
    for line in in_file:
        number = int(line)
        total += number
print(total)
