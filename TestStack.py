# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test
from Stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self) -> None:
        self._empty: Stack[int] = Stack[int]() # type: ignore

        self._1item: Stack[int] = Stack[int]() # type: ignore
        self._1item.push(5)

        self._3items: Stack[str] = Stack[str]() # type: ignore
        self._3items.push('42')
        self._3items.push('600')
        self._3items.push('7')
    
    # All methods whose names start with "test"
    # will be treated as tests
    def test_empty(self) -> None:
        self.assertTrue(self._empty.empty())
        self.assertFalse(self._1item.empty())
        self.assertFalse(self._3items.empty())

    def testPushEmpty(self) -> None:
        self._empty.push(314)
        self.assertFalse(self._empty.empty())
        self.assertEqual(self._empty.pop(), 314)
        self.assertTrue(self._empty.empty())

    def testPushNonEmpty(self) -> None:
        self.assertEqual(self._1item.peek(), 5)
        self._1item.push(12)
        self.assertEqual(self._1item.pop(), 12)
        self.assertEqual(self._1item.pop(), 5)
        self.assertTrue(self._1item.empty())

    def testPop(self) -> None:
        with self.assertRaises(AssertionError):
            self._empty.pop()
        self.assertEqual(self._1item.pop(), 5)
        self.assertTrue(self._1item.empty())
        self.assertEqual(self._3items.pop(), '7')
        self.assertEqual(self._3items.pop(), '600')
        self.assertEqual(self._3items.pop(), '42')
        self.assertTrue(self._3items.empty())

if __name__ == '__main__':
    unittest.main()