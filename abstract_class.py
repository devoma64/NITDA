from abc import ABC, abstractmethod
class Employee(ABC):
    
    @abstractmethod
    def donate(self):
        pass
    
class Donation(Employee):
    def donate(self):
        a = input ("How much do you want to donate: ")
        return a
    
amounts = []

john = Donation()
j = john.donate()
amounts.append(j)

print(amounts)


marvelous = Donation()
m = marvelous.donate()
amounts.append(m)

print(amounts)

        
        