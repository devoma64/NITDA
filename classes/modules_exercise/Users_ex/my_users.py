from users import User
from admin import Admin
from privileges import Privileges


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