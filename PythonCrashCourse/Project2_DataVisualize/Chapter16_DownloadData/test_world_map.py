# ----------------------
# Author: blateyang
# Date: 2018/3/15
# ----------------------

import unittest
from world_map import get_country_code, get_dict_from_csv, get_dict_from_json


class MapTestCase(unittest.TestCase):
    """Test functions in world_map"""

    def test_get_country_code(self):
        country_code = get_country_code('Andorra')
        self.assertEqual(country_code, 'ad')

    def test_csv(self):
        country_dict = get_dict_from_csv('API_IP.JRN.ARTC.SC_DS2_en_csv_v2.csv', 2016)
        self.assertNotEqual(country_dict, {})

    def test_json(self):
        country_dict = get_dict_from_json('gdp.json', 2016)
        self.assertNotEqual(country_dict, {})

if __name__ == '__main__':
    unittest.main()
