"""CP1404 prac 2, exercise 1"""


def main():
    """Print line of stars of same length as valid password from user input."""
    password = get_password()
    print_stars(password)


def get_password():
    """Ask user for password that meets minimum length."""
    password = input("Password: ")
    minimum_length = 5
    while len(password) < minimum_length:
        print(f"Password should contain at least {minimum_length} characters!")
        password = input("Password: ")
    return password


def print_stars(password):
    """Print line of stars of same length as password."""
    print(len(password) * "*")


main()
