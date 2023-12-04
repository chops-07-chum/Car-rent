class CarManager:
    def __init__(self):
        self.cars = []

    def add_car(self, make, model, year, price_per_day):
        car = {'make': make, 'model': model, 'year': year, 'price_per_day': price_per_day, 'available': True}
        self.cars.append(car)

    def display_cars(self):
        print("Available Cars:")
        for index, car in enumerate(self.cars):
            availability = "Available" if car['available'] else "Rented"
            print(f"{index + 1}. {car['year']} {car['make']} {car['model']} - {availability}")
        print()

    def get_car_by_index(self, index):
        return self.cars[index]

    def rent_car(self, index, days):
        car = self.cars[index]
        if car['available']:
            car['available'] = False
            return car['price_per_day'] * days
        else:
            print("Car not available for rent.")
            return 0

    def return_car(self, index):
        self.cars[index]['available'] = True
