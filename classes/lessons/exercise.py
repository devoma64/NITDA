class Restuarant:
    
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"My Restaurant name is {self.restaurant_name} and we are known for cooking {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"We are open 24/7 hours")
    
    # method to the set the number of customer served
    def set_number_served(self, customer_served):
        self.number_served = customer_served
        
    # method to increments number of customer served
    def increment_number_served(self, increment_customer):
        self.number_served += increment_customer

class IceCreamStand(Restuarant):
    def __init__(self, restaurant_name, cuisine_type, flavors) -> None:
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        
    def display_flavors(self)->None:
        print(f"Our Restaurant {self.restaurant_name} also make delicous Ice Cream flavors")
        for flavor in self.flavors:
            print(f"-{flavor}")
            
ice_cream_stand = IceCreamStand("Marvelous Home", " Delicous Meal", [
    "Vanilla",
    "Chocolate",
    "Strawberry",
    "Mint Chocolate Chip",
    "Cookies and Cream"
])

ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()