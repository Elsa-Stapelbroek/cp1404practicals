"""CP1404 practical 9 - Do-from-scratch exercise: Taxi Simulator"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Menu based taxi simulator that uses Taxi and SilverServiceTaxi classes."""
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi(name="Limo", fuel=100, fanciness=2),
             SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)]
    current_taxi = None
    total_cost = 0.00

    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'c':
            print("Taxis available:")
            display_taxis(taxis)
            current_taxi = choose_taxi(taxis)  # None if taxi choice is invalid
        elif choice == 'd':
            try:
                drive_taxi(current_taxi)
                total_cost += current_taxi.get_fare()
            except AttributeError:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_cost:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_cost:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display numbered list of available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Get Taxi choice from user input."""
    try:
        return taxis[int(input("Choose taxi: "))]
    except ValueError:
        print("Invalid taxi choice")
    except IndexError:
        print("Invalid taxi choice")


def drive_taxi(taxi):
    """Get driving distance from user input and display fare."""
    taxi.start_fare()
    taxi.drive(int(input("Drive how far? ")))
    print(f"Your {taxi.name} trip cost you ${taxi.get_fare():.2f}")


main()
