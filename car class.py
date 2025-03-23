class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Car Details: {self.year} {self.make} {self.model}")
        
        
class ElectricCar(Car):
    def __init__(self, make: str, model: str, year: int, battery_size: int):
        super().__init__(make, model, year)  # Call the parent class __init__ method
        self.battery_size = battery_size

    def charge(self):
        print(f"{self.make} {self.model} is charging...")
        