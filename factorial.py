# Program to calculate a factorial using the accumulator pattern.
import timeit
import math

def find_factorial(n: int) -> int:
    # Accumulator variable
    fact: int = 1 # Initial value is the identity element for multiplication

    # Loop
    for i in range(1, n+1): # int   O(n) * O(1) = O(n)
        # Accumulate the answer into the accumulator variable
        fact = fact * i  # O(1)
    return fact

def old_main() -> None:
    """Code from the CSC201 version of main()"""
    print('This program calculates a factorial.')
    # Read the number
    n: int = int(input('Please enter a positive integer: '))
    print(str(n) + '! =', end=' ')

    print(find_factorial(n))

def main(args: list[str]) -> int:
    #print(find_factorial(1000))
    sizes: list[int] = [1, 10, 100] # [10, 100, 1000]
    for size in sizes:
        cmd: str = 'find_factorial({0:d})'.format(size)
        print(timeit.timeit(stmt=cmd, globals=globals()))
    print()
    for size in sizes:
        cmd = 'math.factorial({0:d})'.format(size)
        print(timeit.timeit(stmt=cmd, globals=globals()))

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)