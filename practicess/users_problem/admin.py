from user import User
from privilege import Privileges

class Admin(User):
     def __init__(self, first_name, last_name, age, DOB, sex, contact, privileges) -> None:
          super().__init__(first_name, last_name, age, DOB, sex, contact)
          self.privilegs = Privileges(privileges)
          