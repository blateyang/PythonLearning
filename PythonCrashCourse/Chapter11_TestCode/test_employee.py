# -------------------------
# Author: blateyang
# Date: 2018/3/9
# ------------------------

import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
    """Test employee.py"""
    def setUp(self):
        """Create a Employee object shared by test function"""
        self.employee = Employee('blate', 'yang', 15000)

    def test_give_default_raise(self):
        """Test the default raise"""
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 20000)

    def test_give_custom_raise(self):
        """Test the custom raise"""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary, 25000)

if __name__ == '__main__':
    unittest.main()
