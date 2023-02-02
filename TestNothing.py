# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test

class TestNothing(unittest.TestCase):
    # All methods whose names start with "test"
    # will be treated as tests
    def test_nothing(self) -> None:
        self.assertTrue(True)
        
if __name__ == '__main__':
    unittest.main()