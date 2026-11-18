from Vehicle import Vehicle



class Car(Vehicle):
    
    def calculate_rent(self,days):
        rent_cal = self.rental_price * days + 500
        print('Rent : ',rent_cal)

    def display_vehicle_details(self):
        print('Name : ',self.name)
        print('Year : ',self.year)
        print('Rent : ',self.rental_price)
