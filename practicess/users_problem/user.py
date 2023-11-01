class User:
     def __init__(self, first_name, last_name, age, DOB, sex, contact) -> None:
          self.first_name = first_name
          self.last_name = last_name
          self.age = age
          self.DOB = DOB
          self.sex = sex
          self.contact = contact
          self.login_attempts = 0
     
     def greet_user(self):
          print(f"Hey there {self.first_name} {self.last_name}.")
          
     def describe_user(self):
          print(f"Hello my name is {self.first_name} {self.last_name} i am {str(self.age)} years old born on {self.DOB} i am a {self.sex}. My address is {self.contact}")
     
     # method to increment login_attempts
     
     def increment_login_attempts(self):
          self.login_attempts += 1
     
     def reset_login_attempts(self):
          self.login_attempts = 0