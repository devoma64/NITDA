from user import User
from admin import Admin
from privilege import Privileges


admin_privileges = [
    "can add post", "can delete post", "can ban user"
]

admin = Admin("Marvelous", "won", 24, "14-08-1999", "male", "No 1 harmony street okundi boki", admin_privileges)

admin.describe_user()
admin.privilegs.show_privileges()