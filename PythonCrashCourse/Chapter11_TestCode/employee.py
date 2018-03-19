# -------------------------
# Author: blateyang
# Date: 2018/3/9
# ------------------------
"""Exercise 11-3"""

class Employee():
    """Record salary of employee"""
    def __init__(self, firs_name, last_name, salary):
        self.first_name = firs_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, raise_value=5000):
        """Raise salary"""
        self.salary += raise_value

