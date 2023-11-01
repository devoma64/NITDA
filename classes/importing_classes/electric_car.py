from car import Car

          
class Battery:
     """A simple attempt to model a battery for an electric car
     """
     def __init__(self, battery_size = 40) -> None:
          self.battery_size = battery_size
     
     def describe_battery(self):
          print(f"This car has a {self.battery_size}-kwh battery.")
          
     def get_range(self):
          range = 0
          if self.battery_size == 40:
               range = 150
          elif self.battery_size == 65:
               range = 225
          print(f"This car can go about {range} miles when fully charged.")
     

class ElectricCar(Car):
     def __init__(self, make, model, year) -> None:
          super().__init__(make, model, year)
          self.battery = Battery()