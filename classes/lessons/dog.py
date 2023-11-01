class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def sit(self):
        print(f"{self.name} is sitting")
    
    def roll(self):
        print(f"{self.name} rolled over.")
        
my_dog = Dog('Willie', 25)
our_dog = Dog("Jane", 12)


print(f"My dog is name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()


print(f"Our dog name is {our_dog.name}")
print(f"Our dog age is {our_dog.age}")
our_dog.roll()


