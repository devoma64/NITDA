from random import randint
class Die:
     def __init__(self, side =6) -> None:
          self.side = side
     
     def roll_die(self):
          random_number = randint(1, self.side)
          return random_number

six_sided_die = Die()
print("Rolling a 6-sided die 10 time")
for _ in range(10):
     print(six_sided_die.roll_die())
     
ten_sided_die = Die(side = 10)
print("\nRolling a 10-sided die 10 times")
for _ in range(10):
     print(ten_sided_die.roll_die())
     
twenty_sided_die = Die(side = 20)
print("\nRolling a 20-sided die 10 times")
for _ in range(10):
     print(twenty_sided_die.roll_die())