class RentalManager:
    def __init__(self):
        self.rentals = []

    def rent_car(self, customer, car, days):
        rental = {'customer': customer, 'car': car, 'days': days}
        cost = car_manager.rent_car(car_manager.cars.index(car), days)
        rental['cost'] = cost
        self.rentals.append(rental)

    def return_car(self, customer, car):
        car_manager.return_car(car_manager.cars.index(car))

    def display_rentals(self):
        print("Rental Details:")
        for rental in self.rentals:
            print(f"Customer: {rental['customer']['name']}, Car: {rental['car']['make']} {rental['car']['model']}, Days: {rental['days']}, Cost: ${rental['cost']}")
        print()
