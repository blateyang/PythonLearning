# -------------------------
# Author: blateyang
# Date: 2018/3/9
# ------------------------

"""Test code by using unittest module"""
import unittest
from city_functions import city_functions


class CityTestCase(unittest.TestCase):
    """Test city_functions.py"""
    def test_city_country(self):
        """Test city_functions with 2 args"""
        combined_name = city_functions('santiago', 'chile')
        self.assertEqual(combined_name, 'Santiago, Chile')

    def test_population(self):
        """Test city_functions with 3 args"""
        combined_name = city_functions('santiago', 'chile', population=500000)
        self.assertEqual(combined_name, 'Santiago, Chile - population 500000')

if __name__ == '__main__':  # this need to be added, otherwise test can't run
    unittest.main()
