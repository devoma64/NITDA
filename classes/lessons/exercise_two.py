class User:
    def __init__(self,first_name, last_name, age, DOB, sex, contact) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.DOB = DOB
        self.sex = sex
        self.contact = contact
        self.login_attempts = 0
        
    def greet_user(self):
        print(f"Hello there! please tell us about yourself. Thank you.")
    
    def describe_user(self)-> None:
        print(f"Hey! my name is {self.first_name} {self.last_name} i am {str(self.age)} years old born on {self.DOB} i am a {self.sex}. My address is {self.contact}")
        
    # method to increments login attempts

    def increment_login_attempts(self):
        self.login_attempts += 1
       
    # method to reset login attempts
    def reset_login_attempts(self):
         self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, age, DOB, sex, contact, privileges) -> None:
        super().__init__(first_name, last_name, age, DOB, sex, contact)
        self.privileges = Privileges(privileges)

class Privileges:
    def __init__(self, privileges) -> None:
        self.privileges = privileges
    
    def show_privileges(self):
        print(f"The Admin has the following privileges: ")
        for privilege in self.privileges:
            print(f"-{privilege}")
        
user = User("Wisdom", "Ifiok", 20, "03/08/2005", "Male", "No 1 Harmony street eshiagurubea okundi boki")
# user.greet_user()
# user.describe_user()

# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()

# print(f"Login Attempts: {user.login_attempts}")
# user.reset_login_attempts()
# print(f"Login Attempts after reset: {user.login_attempts}")


admin_privileges = [
    "can add post", "can delete post", "can ban user"
]
admin = Admin("Marvelous", "Won", 24, "14/08/1999", "Male", "No 1 Harmony street eshiagurubea okundi boki", admin_privileges)

# admin.greet_user()
admin.privileges.show_privileges()
admin.describe_user()


print(" ")

