"""
CP1404 practical 7 - Project management program (do from scratch)

estimate: 90 minutes (no idea!)
actual time: honestly don't know (was somewhat on track at around 55 minutes, then got fixated on some details and ended
up taking way more time.).

notes/questions:
- currently storing start_date as a string (despite being mismatched data structure), since I wasn't sure about using
modules inside classes. (not sure if that makes sense)
- so many functions for getting numbers... seems unnecessary (also inconsistent approach to range check for the
percentage in update project section).
"""
from datetime import datetime
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
    """Program to track and update project list files."""
    projects, headers = load_projects(FILENAME)
    print(MENU)
    menu_choice = input(">>>").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif menu_choice == "S":
            filename = input("Filename: ")
            save_projects(projects, filename, headers)
        elif menu_choice == "D":
            display_projects(projects)
        elif menu_choice == "F":
            filter_projects(projects)
        elif menu_choice == "A":
            add_project(projects)
        elif menu_choice == "U":
            project_choice = get_project_choice(projects)
            update_project(project_choice)
            projects.sort()
        else:
            print("Invalid input!")
        print(MENU)
        menu_choice = input(">>>").upper()
    save_projects(projects, "temporary_file.txt", headers)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load list of Projects from file."""
    projects = []
    with open(filename, 'r') as in_file:
        headers = in_file.readline().strip()
        for line in in_file:
            parts = line.strip().split("\t")
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
    """Display projects grouped by completion status."""
    completed_projects = []
    print("Incomplete projects:")
    for project in projects:
        print(project) if not project.is_completed() else completed_projects.append(project)
    print("Completed projects:")
    for project in completed_projects:
        print(project)


def filter_projects(projects):
    """Display projects started after specified date."""
    date_threshold = get_date("Show projects that start after date")  # Should this be outside the function?
    for project in projects:
        start_date = datetime.strptime(project.start_date, "%d/%m/%Y").date()
        if start_date >= date_threshold:
            print(project)


def add_project(projects):
    """Add project from user input."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = get_date("Start date").strftime("%d/%m/%Y")  # TODO: COMMENT/EXPLAIN YOURSELF
    priority = get_number("Priority: ")
    cost_estimate = float(input("Cost estimate: $"))  # not yet error-checked
    completion = get_number_in_range(100, "Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate, completion))
    projects.sort()


def get_project_choice(projects):
    """Get valid project choice from user."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = projects[
        get_number_in_range(len(projects), "Project choice: ")]
    print(project_choice)
    return project_choice


def update_project(project):
    """Update the priority and/or completion percentage based on user input."""
    project.priority = get_new_value(project.priority, "priority")
    new_percentage = get_new_value(project.completion, "completion")
    while new_percentage < 0 or new_percentage > 100:  # Make sure percentage is in valid range
        print("Invalid percentage")
        new_percentage = get_new_value(project.completion, "completion")
    project.completion = new_percentage


def get_date(prompt):
    """Get valid date from user input."""
    is_valid_date = False
    while not is_valid_date:
        try:
            date_string = input(f"{prompt} (dd/mm/yy): ")
            date = datetime.strptime(date_string, "%d/%m/%Y").date()
            is_valid_date = True
        except ValueError:
            print("Invalid date!")
    return date  # Ignore Pycharm warning (impossible error)


def get_number(prompt="Number: "):
    """Get valid integer from user input."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Invalid input")
    return number  # Ignore Pycharm warning (impossible error)


def get_number_in_range(upper_limit, prompt="Number in range: "):
    """Get number within specified range."""
    number = get_number(prompt)
    while number not in range(upper_limit):
        print("Number outside valid range.")
        number = get_number(prompt)
    return number


def get_new_value(field, fieldname):
    """Return new field value from user input (no change if input is empty string)."""
    value = input(f"New {fieldname}: ")
    if value == "":
        return field  # Field unchanged
    else:
        return int(value)  # Not yet error checked!


main()
