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

    def __init__(self):                  # type: ignore
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