# ---------------
# Author: blateyang
# Date: 2018/3/6
# ----------------
"""A group of class related to admin"""
from user import User

class Privileges():
    """Define a Priveleges class"""

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('You are admin and have following privileges:')
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    """Define an Admin class which inherit from User class"""
    def __init__(self, first_name, last_name, age):
        # call  __init__() of base class
        super().__init__(first_name, last_name, age)
        # add new attribute, use Privileges construction fun to initialize
        self.privileges = Privileges()


if __name__ == "__main__":
    # test Admin class
    adm1 = Admin('Blate', 'yang', 24)
    adm1.describe_user()
    adm1.privileges.show_privileges()