class Car:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self)-> None:
       long = f"{self.make} {self.model} {self.year}"
       return long.title()
    
    # function to read odometer
    def read_odometer(self)-> None:
        print(f"This car has {self.odometer_reading} miles on it.")
        
    # let creat a method to update the odometer value
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back an odometer")
    
    # let create a method to increment the value of the odometer after reading from django.conf import settings
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    def __init__(self, battery_size = 65) -> None:
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")    
        
    def get_range(self):
        distance = 0
        if self.battery_size == 40:
            distance = 150
        elif self.battery_size == 65:
            distance = 225
            print(f"This car can go about {distance} miles on a full charge")
        else:
            print(f"Battery not fully charged")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
        else:
            print(f"Battery size already at it maximum {self.battery_size}")
        
        
class ElectricCar(Car):
    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)
        self.battery  = Battery()
        
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")
    
    def fill_gas_tank(self):
        print(f"This car {self.model} doesn't have a gas tank!")
    

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

print(" ")
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()