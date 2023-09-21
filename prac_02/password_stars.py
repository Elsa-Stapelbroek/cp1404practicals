password = input("Password: ")
minimum_length = 5
while len(password) < minimum_length:
    print(f"Password should contain at least {minimum_length} characters!")
    password = input("Password: ")
print(len(password) * "*")
