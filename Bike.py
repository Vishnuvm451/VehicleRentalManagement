from Vehicle import Vehicle


class Bike(Vehicle):
    
    def calculate_rent(self,days):
        rent_cal = self.rental_price * days + 100
        print('Rent : ',rent_cal)

    def display_vehicle_details(self):
        print(self.name)
        print(self.year)
        print(self.rental_price)
