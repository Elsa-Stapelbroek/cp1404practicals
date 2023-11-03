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
            for i, project in enumerate(projects):
                print(f"{i} {project}")
            project_to_update = projects[
                get_number(0, len(projects) - 1, "Project choice: ")]  # currently relies on enumerate starting at 0
            print(project_to_update)
            update_project(project_to_update)
            # update_project()
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
    return projects, headers


def save_projects(projects, filename, headers=""):
    """Save updated projects (with headers) to file."""
    with open(filename, 'w') as out_file:
        print(headers, file=out_file)
        for project in projects:
            print(repr(project), file=out_file)


def display_projects(projects):
    """Display projects grouped by completion status and order by priority."""
    projects.sort()
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
    pass
    # new_priority = input("New priority: ")
    # try:
    #     project.priority = int(new_priority)
    # except ValueError:
    #     if new_priority != "":
    #         print("Invalid input")


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

"""
imports
constants

main:
load projects (default txt)
print menu & get choice
choice not quit:
    - load:
        - get filename -> file
        - load projects (file) -> projects
            - completion and priority: ints
            - name: str
            - cost: float
            - start: datetime
            projects.sort
            return projects
            
    - save:
        - get filename -> file
        - save projects (projects, file)
        
    - display:  # figure this one out!
        - display (projects)
            projects.sort()
            complete = []
            print("Incomplete projects:")
            for project in projects:
                print project if incomplete, else add to complete
            print("complete")
            
    - filter by date:       
        - get date:
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            date = datetime.datetime.strptime(date_string, "%d%m%Y"   # check formatting (dmY would be eg 01/02/2004)
            return date
        - print filtered projects (projects, date)
            for project in projects:
                print project if project.date > date
    
    -  add project(projects):
        - name = input "project name: "
        - date = get date
        - priority = get number?
        - cost = float input "cost: "
        - completion = get number?
               
    - update project(projects)
        - print:  i, project for ... enum(projects)
        - get number (within range(len(projects)) 
        - 

- get number 
    (for updating, 
sort projects at end of loading, adding and updating.
         
"""
