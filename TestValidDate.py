# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test
from valid_date import parseDate, isValidDate

class TestValidDate(unittest.TestCase):
    # All methods whose names start with "test"
    # will be treated as tests
    def test_parse2_7_2023(self) -> None:
        # Tuple, use assertEqual
        self.assertEqual(parseDate('2/7/2023'), (2, 7, 2023))
        
    def test_ZeroParts(self) -> None:
        with self.assertRaises(AssertionError) as cm:
            parseDate('')
        self.assertEqual(cm.exception.args[0], 'Wrong number of parts')

    def test_TwoParts(self) -> None:
        with self.assertRaises(AssertionError) as cm:
            parseDate('2/7')
        self.assertEqual(cm.exception.args[0], 'Wrong number of parts')

    def test_FourParts(self) -> None:
        with self.assertRaises(AssertionError) as cm:
            parseDate('2/7/2023/')
        self.assertEqual(cm.exception.args[0], 'Wrong number of parts')

    def test_nonIntMonth(self) -> None:
        with self.assertRaises(ValueError) as cm:
            parseDate('two/7/2023')
        self.assertEqual(cm.exception.args[0], 
                        "invalid literal for int() with base 10: 'two'")

    def test_nonIntMonth(self) -> None:
        with self.assertRaises(ValueError) as cm:
            parseDate('2/7th/2023')
        self.assertEqual(cm.exception.args[0], 
                        "invalid literal for int() with base 10: '7th'")

    def test_nonIntYear(self) -> None:
        with self.assertRaises(ValueError) as cm:
            parseDate('2/7/foo')
        self.assertEqual(cm.exception.args[0], 
                        "invalid literal for int() with base 10: 'foo'")
    
    def test_validDate_2_7_2023(self) -> None:
        self.assertTrue(isValidDate('2/7/2023'))

    # Month (edge cases)
    def test_validDate_0_7_2023(self) -> None:
        self.assertFalse(isValidDate('0/7/2023'))

    def test_validDate_13_7_2023(self) -> None:
        self.assertFalse(isValidDate('13/7/2023'))

    def test_validDate_1_7_2023(self) -> None:
        self.assertTrue(isValidDate('1/7/2023'))

    def test_validDate_12_7_2023(self) -> None:
        self.assertTrue(isValidDate('12/7/2023'))

    # Year (edge cases)
    def test_validDate_2_7_1581(self) -> None:
        self.assertFalse(isValidDate('2/7/1581'))

    def test_validDate_2_7_1582(self) -> None:
        self.assertTrue(isValidDate('2/7/1582'))

    # Day (edge cases)
    def test_validDate_2_0_2023(self) -> None:
        self.assertFalse(isValidDate('2/0/2023'))

    def test_validDate_2_1_2023(self) -> None:
        self.assertTrue(isValidDate('2/1/2023'))

    def test_validDate_1_32_2023(self) -> None:
        self.assertFalse(isValidDate('1/32/2023'))

    def test_validDate_1_31_2023(self) -> None:
        self.assertTrue(isValidDate('1/31/2023'))

    # 30-day month
    def test_validDate_4_31_2023(self) -> None:
        self.assertFalse(isValidDate('4/31/2023'))

    def test_validDate_4_30_2023(self) -> None:
        self.assertTrue(isValidDate('4/30/2023'))

    # February, non-leap
    def test_validDate_2_29_2023(self) -> None:
        self.assertFalse(isValidDate('2/29/2023'))

    def test_validDate_2_28_2023(self) -> None:
        self.assertTrue(isValidDate('2/28/2023'))

    # February, leap
    def test_validDate_2_30_2020(self) -> None:
        self.assertFalse(isValidDate('2/30/2020'))

    def test_validDate_2_29_2020(self) -> None:
        self.assertTrue(isValidDate('2/29/2020'))

if __name__ == '__main__':
    unittest.main()