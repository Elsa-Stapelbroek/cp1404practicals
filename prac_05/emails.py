"""
CP1404/CP5632 Practical 5 - Do-from-scratch exercise 2
Emails
Estimate: 40 minutes
Actual: 22 minutes  # works, but can definitely be improved

Recommended to use join function for this one... not sure where
"""


def main():
    """Store and display email addresses and names from user input."""
    email_to_name = {}
    email = input("Email: ")
    while email != '':
        name = extract_name(email)
        name_check = input(f"Is your name {name}? (Y/n)").upper()
        if name_check != "Y" and name_check != '':
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract name from email address."""
    return email[:email.find('@')].title().replace('.', ' ')  # currently not accounting for other special characters


main()
