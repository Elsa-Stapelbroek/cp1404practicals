"""CP1404 practical 9 - Intermediate exercise 1: Unreliable Car, test"""
from prac_09.unreliable_car import UnreliableCar

my_unreliable_car = UnreliableCar(name="car but worse", fuel=60, reliability=40.0)

while my_unreliable_car.fuel > 0:
    print(my_unreliable_car)
    my_unreliable_car.drive(20)
    print(my_unreliable_car)
