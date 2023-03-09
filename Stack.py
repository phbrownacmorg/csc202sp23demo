from typing import Generic, TypeVar

T = TypeVar('T')

class Stack(Generic[T]):
    """Class to represent a stack.  The stack is implemented
    as a Python list.  The end of the list is the top of the
    stack."""

    def _invariant(self) -> bool:
        """Class invariant."""
        valid: bool = True
        for i in range(len(self._items)):
            valid = valid and (self._items[i] is not None)
        return valid

    def __init__(self):
        """Create an empty stack."""
        self._items: list[T] = []
        assert self._invariant()

    def empty(self) -> bool:
        """Tells whether the stack is empty."""
        return (len(self._items) == 0)
    
    def push(self, item: T) -> None:
        """Push an item onto the stack."""
        self._items.append(item)

    def pop(self) -> T:
        """Pop an item off the stack."""
        # Pre:
        assert not self.empty()
        return self._items.pop()
    
    # Optional operation
    def peek(self) -> T:
        """Peek at the top item, but do not remove it."""
        # Pre:
        assert not self.empty()
        return self._items[-1]

def matched_delimiters(s: str) -> bool:
    """Takes a string S, and returns True if the delimiters in S
    are balanced.  If the delimiters are not balanced, returns False."""
    OPENING_DELIMITERS: str = """([{"""
    NON_NESTING_DELIMITERS: str = """'"%$`"""
    CLOSING_DELIMITERS: str = """)]}"""

    stack: Stack[str] = Stack[str]()

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