# -------------------
# Author: blateyang
# Date: 2018/3/16
# -------------------

"""Test python_repos.py"""

import unittest
from python_repos import get_json, get_api_request_limit


class ReposTestCase(unittest.TestCase):
    """Test some functions of python_repos.py"""
    def test_get_items(self):
        url = 'https://api.github.com/search/repositories?q=language:Python&sort=stars'
        results = get_json(url)
        self.assertEqual(results[0], 200)
        self.assertEqual(len(results[1]['items']), 30)

if __name__ == '__main__':
    unittest.main()