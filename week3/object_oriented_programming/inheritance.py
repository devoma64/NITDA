class Employees:
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last
        
class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password

class Chefs(Employees):
    def request_leave(self, days):
        return "Please may i take a leave for " +  str(days) + " days"
    
won = Supervisors("Marvelous", "Won", "password")
gift = Chefs("Esin", "Gift")
vicky = Chefs("Okpe", "Victoria")

print(won.password, won.name)
print(gift.request_leave(5))
print(vicky.name)