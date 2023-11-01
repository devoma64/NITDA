class Employees:
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last
        
class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password
        
class Chefs(Employees):
    def leaves_request(self, days):
        return "May i take a leave for " + str(days) + " days"
    
adrian = Supervisors("Adrian", "A", "Apple")
emily = Chefs("Emily", "E")
Junior = Chefs("Junior", "J")

print(emily.leaves_request(3))
print(adrian.password)
print(emily.name)