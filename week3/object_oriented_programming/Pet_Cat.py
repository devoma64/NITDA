class Pet:
    def __init__(self, name, size, color) -> None:
        self.name = name
        self.size = size
        self.color = color
        
class Cat(Pet):
    def __init__(self, name, size, color, age) -> None:
        super().__init__(name, size, color)
        self.age = age
        
    def origin(self, org):
        return "I come from" + str(org)
    
cat = Cat("Cat", "Big", "red", 4)
print(cat.name, cat.size, cat.color, cat.age)