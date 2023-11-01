class Employment:
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last

class Supervisors(Employment):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password
        
class Chefs(Employment):
    def request_leave(self, days):
        return "May i take leave for " + str(days) + " days"
    
marvelous = Supervisors("Adrian", "A", "123456")
jettison = Chefs("jetton", "E")
wisdom = Chefs("Wisdom", "Iffiok")

print(marvelous.password)
print(jettison.request_leave(4))
print(wisdom.name)