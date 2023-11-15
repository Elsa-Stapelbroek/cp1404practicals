"""
CP1404/CP5632 Practical 4 - Converting data lists to strings
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Extract subject details from file and display neatly"""
    subjects = get_subjects()
    print_subjects(subjects)


def get_subjects():  # would extract_subjects() be better for reading info from file?
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
    input_file.close()
    return data


def print_subjects(subjects):
    """Print neatly formatted subject details."""
    max_name_length = max([len(subject[1]) for subject in subjects])
    max_student_count_length = max([len(str(subject[2])) for subject in subjects])  # might be breaking srp?
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:{max_name_length}} and has {subject[2]:{max_student_count_length}} students")


main()
