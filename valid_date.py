# Program to do nothing, correctly.

from leapyear import isLeapYear

def parseDate(instring:str) -> tuple[int, int, int]:
    """Takes a string INSTRING, split it into month, day, and year,
    and return those three as integers."""
    # Pre: none (just that instring is in fact a string)
    parts: list[str] = instring.split('/')
    assert len(parts) == 3, 'Wrong number of parts'
    month: int = int(parts[0])
    day: int = int(parts[1])
    year: int = int(parts[2])
    # Post: month, day, and year are all integers
    return month, day, year

def isValidDate(instring: str) -> bool:
    """Takes a string INSTRING and determines whether it is a valid date
    in m/d/yyyy format."""
    # Pre: none (just that instring is in fact a string)
    valid: bool = True

    try:
        month, day, year = parseDate(instring)
    except AssertionError: # Wrong number of parts
        valid = False
    except ValueError: # One of the parts wasn't an integer
        valid = False
    else:
        if (month < 1 or month > 12): # Valid month
            valid = False
        if (year < 1582): # Valid year
            valid = False
        if (day < 1 or day > 31): # Valid day (any month)
            valid = False
        # 30-day months
        if month in [9, 4, 6, 11] and day > 30:
            valid = False
        # February
        if month == 2 and day > 29:
            valid = False
        if month == 2 and day > 28 and not isLeapYear(year):
            valid = False

    # Post: valid == True iff instring is a valid date in m/d/yyyy format
    return valid

def main(args: list[str]) -> int:
    """Reads a date in m/d/yyyy format and determine whether
    it is a valid date."""
    datestring: str = input('Please enter a date in m/d/yyyy format: ')
    print("'{0}' is".format(datestring), end=' ')

    if not isValidDate(datestring):
        print('NOT', end=' ')
    print('a valid date.')

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)