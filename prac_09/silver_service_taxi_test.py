"""CP1404 practical 9 - Intermediate exercise 2: SilverServiceTaxi, test"""
from prac_09.silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi(name='Hummer', fuel=200, fanciness=4)
print(hummer)

other_taxi = SilverServiceTaxi(name='Other Taxi', fuel=120, fanciness=2)
other_taxi.drive(18)
print(other_taxi)
print(other_taxi.get_fare())
assert other_taxi.get_fare() == 48.80
