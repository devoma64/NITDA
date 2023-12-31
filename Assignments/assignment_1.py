from abc import ABC, abstractmethod

class Bank(ABC):
    
    def basicinfo(self)-> str:
        print("The is a generic Bank")
        return "Generic bank: 0"
    
    @abstractmethod
    def withdraw(self) -> None:
        pass
    
class Swiss(Bank):
    def __init__(self) -> None:
        self.bal = 1000
        
    
    def basicinfo(self) -> str:
        print("This is the Swiss Bank")
        return f"Swiss Bank: {self.bal}"
    
    def withdraw(self, amount) -> None:
        if amount > self.bal:
            print("Insufficient Funds")
        else:
            self.bal = self.bal - amount
            print(f'Withdrawn amount: {amount}')
            print(f'New Balance: {self.bal}')
        return self.bal
    
def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)
    
  
    
    
if __name__ == "__main__":
    main()