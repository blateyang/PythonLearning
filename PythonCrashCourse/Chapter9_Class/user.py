# -------------------
# author: blateyang
# date: 2018/3/6
# -------------------
"""
A group of class related to user
"""


# ex9-3 & 9-5
class User():
    """Define a User class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print('The user profile:')
        print('\t name:'+self.first_name.title()+' '+self.last_name.title())
        print('\t age:'+str(self.age))
        print('\t login attempts:'+str(self.login_attempts))

    def greet_user(self):
        print('Hello,'+self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


if __name__ == '__main__':
    # test User class
    usr1 = User('Yang', 'Guangjun', 24)
    print(usr1.first_name, end=' ')
    print(usr1.last_name, end=' ')
    print(usr1.age)
    usr1.describe_user()
    usr1.greet_user()

    usr1.increment_login_attempts()
    print(usr1.login_attempts)
    usr1.increment_login_attempts()
    print(usr1.login_attempts)
    usr1.reset_login_attempts()
    print(usr1.login_attempts)
