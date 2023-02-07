# Program to do nothing, correctly.

def isLeapYear(year: int) -> bool:
    """Takes a YEAR in the Gregorian calendar and returns 
    a Boolean telling whether YEAR is a leap year."""
    # Pre:
    assert year > 1581, 'Year is too small'
    # Job of the precondition is to make sure the argument makes sense

    leap: bool = False # Correct 3/4 of the time
    if (year % 4) == 0: # Julian rule
        leap = True
    if (year % 100) == 0: # Gregorian century rule
        leap = False
    if (year % 400) == 0: # Gregorian 400-year rule
        leap = True
    # Post:
    assert leap == ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))
    # If the precondition is true and the code is right, the postcondition
    # should never be false

    return leap

def main(args: list[str]) -> int:
    currentyear: int = 2023

    year: int = int(input('Please enter a year (4 digits): '))

    print('The year', year, 'in the Gregorian calendar', end=' ')

    leap: bool = isLeapYear(year)
    if leap and (year < currentyear):
        print('was', end=' ')
    elif (not leap) and (year < currentyear):
        print('was NOT', end=' ')
    elif leap and (year == currentyear):
        print('is', end=' ')
    elif (not leap) and (year == currentyear):
        print('is NOT', end=' ')
    elif leap and (year > currentyear):
        print('will be', end=' ')
    elif (not leap) and (year > currentyear):
        print('will NOT be', end=' ')

    print('a leap year.')

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)