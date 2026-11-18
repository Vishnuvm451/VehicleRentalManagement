from abc import ABC,abstractmethod

class Vehicle(ABC):

    def __init__(self,name,year,rental_price):
        self.name = name 
        self.year = year
        self.__rental_price = rental_price

    @abstractmethod
    def calculate_rent(self):
        pass

    @property
    def rental_price(self):
        return self.__rental_price

    def display_vehicle_details(self):
        print('Vehicle Details ')
        print('Name :',self.name)
        print('Year : ',self.year)
        print('Rent : ',self.__rental_price)
