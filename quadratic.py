# Program to do nothing, correctly.
import math

def read_coefficients() -> tuple[float, float, float]:
    # Read the quadratic system (a, b, and c)
    print('Solve a quadratic system of the form a * x**2 + b * x + c = 0')
    try:
        a: float = float(input('Please enter a value for a: '))
        b: float = float(input('Please enter a value for b: '))
        c: float = float(input('Please enter a value for c: '))
    # *Lots* of ways to foul up reading a floating-point value from
    # a string!  If-else won't cut it.

    # Catch the exception raised by float() function, and exit somewhat gracefully.
    except ValueError as e:
        print('PROBLEM: a, b, and c must all be floating-point numbers.')
        # e.args[0] is generally the error message that came with the exception.
        print(e.args[0].capitalize())
        a, b, c = math.nan, math.nan, math.nan
    return a, b, c

def find_determinant(a: float, b: float, c: float) -> float:
    # Find the determinant
    return math.pow(b, 2) - 4*a*c

def find_roots(a: float, b: float, c: float) -> tuple[float, float]:
    # Find the roots

    det: float = find_determinant(a, b, c)
    if det < 0:
        return math.nan, math.nan
    else: # For clarity.  Not *strictly* necessary, because of the "return" on 21.
        # Take the square root of the determinant
        # (Yes, this may crash if the determinant is negative.
        #  We'll see how to avoid that later in the course.)
        detroot: float = math.sqrt(det)

        # Test that
        #print(detroot)

        # Find the roots
        root1: float = (-b + detroot)/(2*a)
        root2: float = (-b - detroot)/(2*a)
        return root1, root2

def find_roots_except(a: float, b: float, c: float) -> tuple[float, float]:
    """Find the roots of the system a*x**2 + b*x + c = 0.  If there are no
    real roots, go ahead and raise the exception from math.sqrt()."""
    det: float = find_determinant(a, b, c)
    detroot: float = math.sqrt(det)
    root1: float = (-b + detroot)/(2*a)
    root2: float = (-b - detroot)/(2*a)
    return root1, root2

def main(args: list[str]) -> int:
    # Input
    a, b, c = read_coefficients() # float, float, float
    if not math.isnan(c):
        print('The system is', a, '* x**2 +', b, '* x +', c, '= 0')

        # Find the roots (Processing)
        root1, root2 = find_roots(a, b, c)

        if math.isnan(root1):
            print('The system has no real roots.')
        else:
            # Output
            print('The roots are:', root1, root2)

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)