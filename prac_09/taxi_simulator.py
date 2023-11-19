"""CP1404 practical 9 - Do-from-scratch exercise: Taxi Simulator"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
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
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = choose_taxi(taxi_choice, taxis)
        elif choice == 'd':
            try:
                current_taxi.start_fare()
                current_taxi.drive(int(input("Drive how far? ")))
                print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
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
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxi_choice, taxis):
    if taxi_choice in range(len(taxis)):
        return taxis[taxi_choice]
    else:
        print("Invalid taxi choice")


main()
