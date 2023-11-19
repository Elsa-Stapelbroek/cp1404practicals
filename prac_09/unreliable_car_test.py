"""CP1404 practical 9 - Intermediate exercise 1: Unreliable Car, test"""
from prac_09.unreliable_car import UnreliableCar

print("Test reliability = 50: ")
my_unreliable_car = UnreliableCar(name="car but worse", fuel=60, reliability=50.0)

while my_unreliable_car.fuel > 0:
    print(my_unreliable_car)
    my_unreliable_car.drive(20)
    print(my_unreliable_car)

starting_fuel = 100
print("Test reliability = 0.0: (car should never move)")
broken_car = UnreliableCar(name="broken car", fuel=starting_fuel, reliability=0.0)
for i in range(500):
    broken_car.drive(10)
assert broken_car.fuel == starting_fuel

print("Test reliability = 100: (car should always move)")
reliable_car = UnreliableCar(name="reliable car", fuel=starting_fuel, reliability=100)
for i in range(500):
    reliable_car.drive(0.2)
assert reliable_car.fuel == 0
