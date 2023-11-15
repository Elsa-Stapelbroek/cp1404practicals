for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number = int(input("Number: "))
for i in range(number):
    print("*", end='')
print()

for i in range(1, number + 1):
    print(i * "*")
print()
