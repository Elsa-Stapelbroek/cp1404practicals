"""CP1404 practical 9 - Do-from-scratch exercise: Taxi Simulator


"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi(name="Limo", fuel=100, fanciness=2),
             SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)]

    print(MENU)
    choice = input(">>> ").lower()
    current_taxi = None
    while choice != 'q':
        if choice == 'c':
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = choose_taxi(taxi_choice, taxis)

        print(MENU)
        choice = input(">>> ").lower()


def choose_taxi(taxi_choice, taxis):
    if taxi_choice in range(len(taxis)):
        return taxis[taxi_choice]
    else:
        print("Invalid taxi choice")


def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
