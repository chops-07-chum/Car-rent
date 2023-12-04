class CustomerManager:
    def __init__(self):
        self.customers = []

    def create_customer(self, name):
        customer = {'name': name}
        self.customers.append(customer)
        return customer

    def display_customers(self):
        print("Customers:")
        for index, customer in enumerate(self.customers):
            print(f"{index + 1}. {customer['name']}")
        print()
