# Class to represent a fraction.

from typing import cast

def findGCD(a: int, b: int) -> int:
    """Find the GCD of two integers A and B.  Handles negative
    values correctly."""
    # Pre:
    assert a != 0 or b != 0
    m: int = a
    n: int = b    
    while n != 0:
        m, n = n, m % n
    gcd = abs(m)
    # Post:
    assert (a % gcd == 0) and (b % gcd == 0) and gcd > 0
    # and there is no integer > gcd for which this is so
    return gcd

class Fraction:
    """Class to represent a rational number a/b, b != 0.
    The fraction is always kept in lowest terms.  Fraction
    objects are immutable once created."""

    def _invariant(self) -> bool:
        """Class invariant.  Note that this enforces keeping the Fraction
        always in simplest terms."""
        return (self._denom > 0) and \
            (findGCD(self._numr, self._denom) == 1)

    # Constructor
    def __init__(self, a: int, b: int):
        """Construct a Fraction, in lowest terms."""
        # Pre:
        assert b != 0, "Zero denominator"
        # Reduce to lowest terms
        if b < 0: # No negative denominators
            a = -a
            b = -b
        gcd: int = findGCD(a, b)
        self._numr = a // gcd
        self._denom = b // gcd
        # Post: Class invariant holds
        assert self._invariant()
                
    # Query methods

    # Getter methods
    def getNumr(self) -> int:
        """Get the numerator."""
        # Pre:
        assert self._invariant()
        # Post: return value is the numerator
        return self._numr

    def getDenom(self) -> int:
        """Get the denominator."""
        # Pre:
        assert self._invariant()
        # Post: return value is the invariant
        return self._denom

    # Other query methods
    def __str__(self) -> str:
        """Represent the Fraction as a string in the form "a/b",
        where a is the numerator and b is the denominator."""
        # Pre:
        assert self._invariant()
        # Post: return value represents the fraction in the form "a/b"
        return '{0:d}/{1:d}'.format(self._numr, self._denom)

    def __eq__(self, other: object) -> bool:
        """Compare Fractions for equality.  Because Fractions
        are stored in lowest terms, it is enough just to compare
        numerators and denominators."""
        # Pre: other is a Fraction
        assert self._invariant() and isinstance(other, Fraction)
        otherFrac: Fraction = cast(Fraction, other)
        # Pre, second half.  This needs the cast to be done before being evaluated.
        assert otherFrac._invariant()
    
        # Post: return value is True iff self == other
        return (otherFrac._numr == self._numr) and \
                (otherFrac._denom == self._denom)

    def __add__(self, other: 'Fraction') -> 'Fraction':
        """Add two Fractions and return the result as a new Fraction object."""
        # Pre:
        assert self._invariant() and other._invariant()

        denom: int = self.getDenom() * other.getDenom()
        numerator: int = self.getNumr() * other.getDenom() + \
            other.getNumr() * self.getDenom()

        # Post: return value is self + other
        return Fraction(numerator, denom)
