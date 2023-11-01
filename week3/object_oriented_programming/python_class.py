class House:
    
    num_rooms = 5
    bathrooms = 2
    
    
    def cost_evaluation(self, rate):
        # functionality to calculate the cost of the area of the house
        
        cost = rate * self.num_rooms
        return cost
house = House()
print(house.num_rooms)
print(house.bathrooms)

house.num_rooms = 7
print(house.num_rooms)
print(house.bathrooms)