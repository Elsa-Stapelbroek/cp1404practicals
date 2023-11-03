"""
CP1404 practical 7 - Project management program (do from scratch)

estimate: 90 mins (no idea!)
actual time: 55 mins so far (so it'll probably take quite a bit longer)

Write a program in project_management.py to load and save a data file and use a list of Project objects.

Load projects from the data file when the program starts and save them to it when the user quits.

Options:
Load projects: (Prompt the user for a filename to load projects from and load them)
Save projects: (Prompt the user for a filename to save projects to and save them)
Display projects: (Display two groups: incomplete projects; completed projects, both sorted by priority)
Filter projects by date: (Ask the user for a date and display only projects that start after that date, sorted by date)
Add new project: (Ask the user for the inputs and add a new project to memory)
Update project: (Choose a project, then modify the completion % and/or priority - leave blank to retain existing values)

Expectations:
- Use the datetime module for the project start date
- Write your class to sort/compare Project objects based on priority order
- Think about writing utility/helper methods in your class and main program.
- Follow good design principles like SRP and DRY. Notice that there's two kinds of loading and write one function to handle both. Same for saving.
- Write good clean code (no pylint warnings) with good naming and design (as always!)
- Here are two suggestions to leave until last (iterative development):
    - Error checking. Do no error checking to start with.
    - Date formatting. Just use a string until most everything else works, then, here are some suggestions.
"""

from prac_07.project import Project

FILENAME = "projects.txt"

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    """"""
    projects, headers = load_projects(FILENAME)
    print(MENU)
    menu_choice = input(">>>").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            filename = input("Filename: ")  # maybe extract method later (also to error check for valid filename)?
            projects = load_projects(filename)  # if this is supposed to replace the old projects... not exactly sure
        elif menu_choice == "S":
            filename = input("Filename: ")
            save_projects(projects, filename, headers)
        elif menu_choice == "D":
            display_projects(projects)
        elif menu_choice == "F":
            filter_projects()
        elif menu_choice == "A":
            add_project()
        elif menu_choice == "U":
            # TODO: condense this section into function(s)
            for i, project in enumerate(projects):
                print(f"{i} {project}")
            project_choice = projects[get_number_in_range(len(projects), "Project choice: ")]
            print(project_choice)
            update_project(project_choice)
            projects.sort()
        else:
            print("Invalid input!")
        print(MENU)
        menu_choice = input(">>>").upper()
    save_projects(projects, "temporary_file.txt", headers)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load project list from txt file."""
    projects = []
    with open(filename, 'r') as in_file:
        headers = in_file.readline().strip()
        for line in in_file:
            parts = line.strip().split("\t")
            # print(parts)
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    projects.sort()
    return projects, headers


def save_projects(projects, filename, headers=""):
    """Save updated projects (with headers) to file."""
    with open(filename, 'w') as out_file:
        print(headers, file=out_file)
        for project in projects:
            print(repr(project), file=out_file)


def display_projects(projects):
    """Display projects grouped by completion status and order by priority."""
    completed_projects = []
    print("Incomplete projects:")
    for project in projects:
        print(project) if not project.is_completed() else completed_projects.append(project)
    print("Completed projects:")
    for project in completed_projects:  # DRY??
        print(project)
    # Tried generator, didn't work (figure out why!), surely there's a nicer way?


def filter_projects():
    pass


def add_project():
    pass


def update_project(project):
    """Update the priority and/or completion percentage based on user input."""
    project.priority = get_value(project.priority, "priority")
    new_percentage = get_value(project.completion, "completion")
    while 0 > new_percentage or new_percentage > 100:  # Make sure percentage is in valid range
        print("Invalid percentage")
        new_percentage = get_value(project.completion, "completion")
    project.completion = new_percentage


def get_number_in_range(upper_limit, prompt="Number in range: "):
    """Get number within specified range."""
    number = int(input(prompt))
    while number not in range(upper_limit):
        print("Number outside valid range.")
        number = int(input(prompt))
    return number


def get_value(field, fieldname):  # surely that doesn't have to be two params?
    """Return new field value from user input (no change if input is empty string)."""
    value = input(f"New {fieldname}: ")
    if value == "":
        return field  # Field unchanged
    else:
        return int(value)  # No error checking yet!


def get_number(lower_limit, upper_limit, prompt="Number: "):
    """Get valid integer between lower and upper limits (inclusive) from user input."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(prompt))
            if number < lower_limit or number > upper_limit:
                print(f"Number must be between {lower_limit} and {upper_limit} (inclusive)")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid (not an integer)")
    return number  # Ignore Pycharm warning (impossible error)


main()
