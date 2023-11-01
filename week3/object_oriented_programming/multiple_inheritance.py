class Fruit():
    def __init__(self, fruit):
        print("Fruit type: ", fruit)
        
class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print("Apple is sweet")
        
# class Fruit():
#     def __init__(self, fruit) -> None:
#         print("Fruit type", fruit)

# class FruitFlavour(Fruit):
#     def __init__(self, fruit) -> None:
#         super().__init__('Apple')
#         print("The fruit is very sweet")
        
# frut = FruitFlavour()