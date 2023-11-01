from privileges import Privileges
from users import User

class Admin(User):
    def __init__(self, first_name, last_name, age, DOB, sex, contact, privileges) -> None:
        super().__init__(first_name, last_name, age, DOB, sex, contact)
        self.privileges = Privileges(privileges)