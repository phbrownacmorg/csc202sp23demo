# Program to do nothing, correctly.

from Stack import Stack

def matched_delimiters(s: str) -> bool:
    """Takes a string S, and returns True if the delimiters in S
    are balanced.  If the delimiters are not balanced, returns False."""
    OPENING_DELIMITERS: str = """([{"""
    NON_NESTING_DELIMITERS: str = """'"%$`"""
    CLOSING_DELIMITERS: str = """)]}"""

    stack: Stack[str] = Stack[str]() # type: ignore

    balanced: bool = True
    for c in s:
        if c in OPENING_DELIMITERS:
            stack.push(c)
        elif c in CLOSING_DELIMITERS:
            if stack.empty():
                balanced = False
            else:
                opening: str = stack.pop()
                if OPENING_DELIMITERS.index(opening) != CLOSING_DELIMITERS.index(c):
                    # Mismatch
                    balanced = False
        elif c in NON_NESTING_DELIMITERS:
            if not stack.empty() and stack.peek() == c:
                stack.pop() # Get rid of the opening delimiter
            else:
                stack.push(c)
    if not stack.empty():  # Oops, leftovers
        balanced = False

    return balanced


def main(args: list[str]) -> int:
    # Obvious false cases
    assert not (matched_delimiters('('))
    assert not (matched_delimiters('['))
    assert not (matched_delimiters('{'))
    assert not (matched_delimiters(')'))
    assert not (matched_delimiters(']'))
    assert not (matched_delimiters('}'))
    assert not (matched_delimiters("'"))
    assert not (matched_delimiters('"'))
    assert not (matched_delimiters('`'))
    assert not (matched_delimiters('%'))
    assert not (matched_delimiters('$'))

    # Obvious true cases
    assert (matched_delimiters(''))
    assert (matched_delimiters('()'))
    assert (matched_delimiters('[]'))
    assert (matched_delimiters('{}'))
    assert (matched_delimiters('""'))
    assert (matched_delimiters("''"))
    assert (matched_delimiters('``'))
    assert (matched_delimiters('$$'))
    assert (matched_delimiters('%%'))

    # Nesting
    assert (matched_delimiters('(()()()())'))
    assert (matched_delimiters('(((())))'))
    assert (matched_delimiters('(()((())()))'))
    assert not (matched_delimiters('((((((())'))
    assert not (matched_delimiters('()))'))
    assert not (matched_delimiters('(()()(()'))

    # If we get this far, everything worked
    print('Tests completed successfully')

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)