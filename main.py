from Vehicle import Vehicle
from Car import Car
from Bike import Bike


car = Car('Kawa',2020,5000)
bike = Bike('Honda',2000,4000)

print(' ')
print('--- CAR DETAILS ---\n')
car.display_vehicle_details()

print(' ')
print('--- CAR RENT ---\n')
car.calculate_rent(3)


print(' ')
print('--- BIKE DETAILS ---\n')
car.display_vehicle_details()

print(' ')
print('--- BIKE RENT ---\n')
bike.calculate_rent(3)
print(' ')