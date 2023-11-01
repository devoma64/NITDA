class Payslips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount
        
        
    def Pay(self):
        self.payment = "yes"
    
    def status(self):
        if self.payment == "yes":
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " not paid " + str(self.amount)
marvelous = Payslips("Marvelous", "no", 99000)
jettison = Payslips("Jettison", "no", 50000)

print(marvelous.status(), "\n", jettison.status())
marvelous.Pay()
jettison.Pay()

print(marvelous.status(), "\n", jettison.status())