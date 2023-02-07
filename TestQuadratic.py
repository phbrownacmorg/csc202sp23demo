# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test
import quadratic
import math

class TestQuadratic(unittest.TestCase):
    # All methods whose names start with "test"
    # will be treated as tests

    # No tests for read_coefficients(): keyboard input
    # No tests for main(): just output

    # Use self.assertAlmostEqual() to compare floating-point values
    # (To compare most things, use self.assertEqual().)
    def test_det_1_0_0(self) -> None: # b == c == 0
        self.assertAlmostEqual(quadratic.find_determinant(1, 0, 0), 0)

    def test_det_1_2_0(self) -> None: # b != 0, c == 0
        self.assertAlmostEqual(quadratic.find_determinant(1, 2, 0), 4)
        
    def test_det_1_10_0(self) -> None: # b != 0, c == 0
        self.assertAlmostEqual(quadratic.find_determinant(1, 10, 0), 100)

    def test_det_1_n5_0(self) -> None: # b != 0, c == 0
        self.assertAlmostEqual(quadratic.find_determinant(1, -5, 0), 25)

    def test_det_1_2_n2(self) -> None: # b != 0, c != 0
        self.assertAlmostEqual(quadratic.find_determinant(1, 2, -2), 12)

    def test_det_n2_2_n2(self) -> None: # a != 1, b != 0, c != 0
        self.assertAlmostEqual(quadratic.find_determinant(-2, 2, -2), -12)

    def test_roots_1_0_0(self) -> None:
        roots = quadratic.find_roots(1, 0, 0)
        self.assertEqual(len(roots), 2) # Comparing integers, use self.assertEqual()
        self.assertAlmostEqual(roots[0], 0)
        self.assertAlmostEqual(roots[1], 0)

    def test_roots_1_2_0(self) -> None:
        roots = quadratic.find_roots(1, 2, 0)
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], 0)
        self.assertAlmostEqual(roots[1], -2)

    def test_roots_1_10_0(self) -> None:
        roots = quadratic.find_roots(1, 10, 0)
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], 0)
        self.assertAlmostEqual(roots[1], -10)

    def test_roots_1_n5_0(self) -> None:
        roots = quadratic.find_roots(1, -5, 0)
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], 5)
        self.assertAlmostEqual(roots[1], 0)
    
    def test_roots_1_2_n2(self) -> None:
        roots = quadratic.find_roots(1, 2, -2)
        self.assertEqual(len(roots), 2)
        # You *can* calculate the number to compare to
        self.assertAlmostEqual(roots[0], (-2 + math.sqrt(12))/2)
        self.assertAlmostEqual(roots[1], (-2 - math.sqrt(12))/2)

    def test_roots_n2_2_n2(self) -> None:
        roots = quadratic.find_roots(-2, 2, -2)
        self.assertEqual(len(roots), 2)
        # The tuple is math.nan, math.nan.  
        # Need math.isnan(), since math.nan != anything
        self.assertTrue(math.isnan(roots[0]))
        self.assertTrue(math.isnan(roots[1]))

    def test_roots_xc_1_0_0(self) -> None:
        roots = quadratic.find_roots_except(1, 0, 0)
        self.assertEqual(len(roots), 2) # Comparing integers, use self.assertEqual()
        self.assertAlmostEqual(roots[0], 0)
        self.assertAlmostEqual(roots[1], 0)

    def test_roots_xc_1_2_0(self) -> None:
        roots = quadratic.find_roots_except(1, 2, 0)
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], 0)
        self.assertAlmostEqual(roots[1], -2)

    def test_roots_xc_1_10_0(self) -> None:
        roots = quadratic.find_roots_except(1, 10, 0)
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], 0)
        self.assertAlmostEqual(roots[1], -10)

    def test_roots_xc_1_n5_0(self) -> None:
        roots = quadratic.find_roots_except(1, -5, 0)
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], 5)
        self.assertAlmostEqual(roots[1], 0)
    
    def test_roots_xc_1_2_n2(self) -> None:
        roots = quadratic.find_roots_except(1, 2, -2)
        self.assertEqual(len(roots), 2)
        # You *can* calculate the number to compare to
        self.assertAlmostEqual(roots[0], (-2 + math.sqrt(12))/2)
        self.assertAlmostEqual(roots[1], (-2 - math.sqrt(12))/2)

    def test_roots_xc_n2_2_n2(self) -> None:
        with self.assertRaises(ValueError) as cm:
            roots = quadratic.find_roots_except(-2, 2, -2)
        # Make certain it's the *correct* ValueError
        exc: ValueError = cm.exception
        self.assertEqual(exc.args[0], "math domain error") # args[0] is the error message

if __name__ == '__main__':
    unittest.main()