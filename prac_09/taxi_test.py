"""CP1404 practical 9 - Walkthrough example: Test Taxi"""
from prac_09.taxi import Taxi

my_taxi = Taxi("Prius1", 100)
my_taxi.drive(40)
print(my_taxi)
print(my_taxi.get_fare())

my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi)
print(my_taxi.get_fare())
