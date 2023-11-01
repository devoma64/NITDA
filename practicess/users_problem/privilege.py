class Privileges:
     def __init__(self, privileges) -> None:
          self.privileges = privileges
          
     def show_privileges(self):
          print(f"The admin has the following privileges: ")
          for privilege in self.privileges:
               print(f"-{privilege}")