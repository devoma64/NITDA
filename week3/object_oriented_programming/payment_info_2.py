from datetime import date

class Payslips:
    def __init__(self, name, payment, amount, payment_date) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount
        self.payment_date = payment_date
        
    def Pay(self):
        self.payment = "Yes"
        # self.payment_date = date.today()
        
    def status(self):
        if self.payment == "Yes":
            return self.name + " is paid " + str(self.amount) + " " + str(self.payment_date)
        else:
            return self.name + " is not paid yet" + str(self.amount) + " " + str(self.payment_date)
marvelous = Payslips("Marvelous ", "yes", 100000, date.today())
jettison = Payslips("Jettison ", "yes", 500000, date.today())

print(marvelous.status(), "\n", jettison.status())

marvelous.Pay()
jettison.Pay()
print(marvelous.status(), "\n", jettison.status())
        