# class Recipe:
#    def __init__(self, dish, items, time) -> None:
#       self.dish = dish
#       self.items = items
#       self.time = time

#    def contents(self):
#         print("The " + self.dish + " has " + str(self.items) +  " and " + str(self.time) + " min to prepare")

# pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45)
# pasta = Recipe("Pasta", ["Penne", "Sauce"], 55)

# print(pizza.items)
# print(pasta.items)

# print(pizza.contents())
# print(pasta.contents())

# Creating a recipes like app


class Recipe:
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time
        
    def contents(self):
        print("The " + self.dish + "has " + str(self.items) + " and " + str(self.time) + " min to prepare the them")
pizza = Recipe("Pizza:", ["Cheese", "Bread", "Tomato"], 45)
pasta = Recipe("Pasta:", ["Penne", "Sauce"], 55)

print(pizza.contents())
print(pasta.contents())
        