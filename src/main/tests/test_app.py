# -*- coding: UTF-8 -*-
# Python3.7

# *******************************************************
#
#   brief       test_app.py
#   author      segulee@gmail.com
#
# *******************************************************

import unittest


class AppTestCase(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_something(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
