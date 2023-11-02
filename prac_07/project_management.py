"""
CP1404 practical 7 - Project management program (do from scratch)

estimate: 90 mins (no idea!)
actual time:

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

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    """"""
    projects = load_projects()
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            load_projects()
        elif choice == "S":
            save_projects()
        elif choice == "D":
            display_projects()
        elif choice == "F":
            filter_projects()
        elif choice == "A":
            add_project()
        elif choice == "U":
            update_project()
        else:
            print("Invalid input!")
        print(MENU)
        choice = input(">>>").upper()
    save_projects()
    print("Thank you for using custom-built project management software.")


def load_projects(filename="projects.txt"):
    pass


def save_projects():
    pass


def display_projects():
    pass


def filter_projects():
    pass


def add_project():
    pass


def update_project():
    pass
