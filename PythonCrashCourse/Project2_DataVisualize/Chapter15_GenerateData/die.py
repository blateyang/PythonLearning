# ----------------------
# Author: blateyang
# Date: 2018/3/13
# ----------------------

from random import randint


class Die():
    """A class representing die"""
    def __init__(self, num_sides=6):
        """num_sides of die is 6 in default"""
        self.num_sides = num_sides

    def roll(self):
        """return a random value between 1 and num_sides"""
        return randint(1, self.num_sides)

