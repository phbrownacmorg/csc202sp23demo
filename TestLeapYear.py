# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test
import leapyear

class TestLeapYear(unittest.TestCase):
    # All methods whose names start with "test"
    # will be treated as tests

    # Use self.assertTrue() and self.assertFalse() to check Boolean conditions
    def test_2023(self) -> None: # y % 4 == 3
        self.assertFalse(leapyear.isLeapYear(2023))

    def test_2022(self) -> None: # y % 4 == 2
        self.assertFalse(leapyear.isLeapYear(2022))

    def test_2021(self) -> None: # y % 4 == 1
        self.assertFalse(leapyear.isLeapYear(2021))

    def test_2020(self) -> None: # y % 4 == 0, y % 100 != 0 (== 20)
        self.assertTrue(leapyear.isLeapYear(2020))

    def test_2004(self) -> None: # y % 4 == 0, y % 100 == 4
        self.assertTrue(leapyear.isLeapYear(2004))

    def test_1996(self) -> None: # y % 4 == 0, y % 100 == 96
        self.assertTrue(leapyear.isLeapYear(1996))

    def test_2100(self) -> None: # y % 100 == 0, y % 400 == 100
        self.assertFalse(leapyear.isLeapYear(2100))

    def test_1900(self) -> None: # y % 100 == 0, y % 400 == 300
        self.assertFalse(leapyear.isLeapYear(1900))

    def test_1800(self) -> None: # y % 100 == 0, y % 400 == 200
        self.assertFalse(leapyear.isLeapYear(1800))

    def test_2000(self) -> None: # y % 400 == 0
        self.assertTrue(leapyear.isLeapYear(2000))


if __name__ == '__main__':
    unittest.main()