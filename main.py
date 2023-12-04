from car_manager import CarManager
from customer_manager import CustomerManager
from rental_manager import RentalManager

def main():
    # Initialize car, customer, and rental managers
    car_manager = CarManager()
    customer_manager = CustomerManager()
    rental_manager = RentalManager()

    # Add cars
    car_manager.add_car("Toyota", "Camry", 2022, 50)
    car_manager.add_car("Honda", "Civic", 2022, 40)

    # Display available cars
    car_manager.display_cars()

    # Create customers
    customer1 = customer_manager.create_customer("John Doe")
    customer2 = customer_manager.create_customer("Jane Doe")

    # Display customers
    customer_manager.display_customers()

    # Customers rent cars
    rental_manager.rent_car(customer1, car_manager.get_car_by_index(0), 5)
    rental_manager.rent_car(customer2, car_manager.get_car_by_index(1), 3)

    # Display rental details
    rental_manager.display_rentals()

    # Customers return cars
    rental_manager.return_car(customer1, car_manager.get_car_by_index(0))
    rental_manager.return_car(customer2, car_manager.get_car_by_index(1))

    # Display available cars after returns
    car_manager.display_cars()

if __name__ == "__main__":
    main()
