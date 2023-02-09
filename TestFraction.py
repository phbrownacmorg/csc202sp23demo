# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test
from Fraction import findGCD, Fraction


class TestFraction(unittest.TestCase):
    # All methods whose names start with "test"
    # will be treated as tests
    def test_gcd_0_0(self) -> None:
        # Violates the precondition
        with self.assertRaises(AssertionError) as cm:
            findGCD(0, 0)

    def test_gcd_10_7(self) -> None:
        self.assertEqual(findGCD(10, 7), 1)
        
    def test_gcd_14_11(self) -> None:
        self.assertEqual(findGCD(14, 11), 1)

    def test_gcd_23K_1(self) -> None:
        self.assertEqual(findGCD(23000, 1), 1)

    def test_gcd_1_23K(self) -> None:
        self.assertEqual(findGCD(1, 23000), 1)

    def test_gcd_9781_n1(self) -> None:
        self.assertEqual(findGCD(9781, -1), 1)

    def test_gcd_n1_9781(self) -> None:
        self.assertEqual(findGCD(-1, 9781), 1)

    def test_gcd_0_n1(self) -> None:
        self.assertEqual(findGCD(0, -1), 1)

    def test_gcd_20_42(self) -> None:
        self.assertEqual(findGCD(20, 42), 2)

    def test_gcd_42_20(self) -> None:
        self.assertEqual(findGCD(42, 20), 2)

    def test_gcd_8103_243(self) -> None:
        self.assertEqual(findGCD(8103, 243), 3)

    def test_gcd_36_8(self) -> None:
        self.assertEqual(findGCD(36, 8), 4)

    def test_gcd_10_10(self) -> None:
        self.assertEqual(findGCD(10, 10), 10)

    def test_gcd_20_100(self) -> None:
        self.assertEqual(findGCD(20, 100), 20)

    def test_gcd_100_20(self) -> None:
        self.assertEqual(findGCD(100, 20), 20)

    def test_gcd_243_8100(self) -> None:
        self.assertEqual(findGCD(243, 8100), 81)

    def test_gcd_n8100_n243(self) -> None:
        self.assertEqual(findGCD(-8100, -243), 81)

    def test_gcd_9781_0(self) -> None:
        self.assertEqual(findGCD(9781, 0), 9781)

    def test_gcd_0_9781(self) -> None:
        self.assertEqual(findGCD(0, 9781), 9781)

    def test_str_1_2(self) -> None:
        self.assertEqual('1/2', str(Fraction(1, 2)))

    def test_str_2_4(self) -> None:
        self.assertEqual('1/2', str(Fraction(2, 4)))

    def test_str_n2_n4(self) -> None:
        self.assertEqual('1/2', str(Fraction(-2, -4)))

    def test_str_2_n4(self) -> None:
        self.assertEqual('-1/2', str(Fraction(2, -4)))

    def test_str_n2_4(self) -> None:
        self.assertEqual('-1/2', str(Fraction(-2, 4)))

    def test_str_8_36(self) -> None:
        self.assertEqual('2/9', str(Fraction(8, 36)))

    def test_getters(self) -> None:
        frac: Fraction = Fraction(8, 36)
        self.assertEqual(frac.getNumr(), 2)
        self.assertEqual(frac.getDenom(), 9)

    def test_eq_half(self) -> None:
        self.assertTrue(Fraction(1, 2) == Fraction(3, 6))

    def test_eq_n2_9(self) -> None:
        self.assertTrue(Fraction(-8, 36) == Fraction(2, -9))

    def test_add_halves(self) -> None:
        # print(Fraction(1, 1), Fraction(1, 2), Fraction(512, 1024),
        #     Fraction(1, 2) + Fraction(512, 1024))
        self.assertTrue(Fraction(1, 1) == 
            Fraction(1, 2) + Fraction(512, 1024))


if __name__ == '__main__':
    unittest.main()