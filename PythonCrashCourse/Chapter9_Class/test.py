# -------------------
# writer: blateyang
# date: 2018/3/6
# -------------------

"""A test file for user module and other excersices"""
from collections import OrderedDict
from random import randint

import admin

# ex9-12
adm = admin.Admin('Blate', 'yang', 24)
adm.privileges.show_privileges()

# ex9-13 use OrderedDict
favorite_languages = OrderedDict()

favorite_languages['Bob'] = 'python'
favorite_languages['Blateyang'] = 'python'
favorite_languages['Zhuo'] = 'C++'
favorite_languages['Qin'] = 'Java'

for name,value in favorite_languages.items():
    print(name+' favorite languages is '+ value)


# ex9-14
class Die():
    """A class simulating roll die"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(str(randint(1, self.sides)), end=' ')

# test Die class
die1 = Die()
for i in range(10):
    die1.roll_die()
print()

die2 = Die(10)
for i in range(10):
    die2.roll_die()
print()

