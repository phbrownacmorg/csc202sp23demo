from typing import cast

class PlayingCard:
    """Class to represent a playing card of the usual (French) type.
    Objects of this type are immutable once created."""

    SUITS: tuple[str, ...] = ('Clubs', 'Diamonds', 'Hearts', 'Spades') # No particular order
    RANK_NAMES: tuple[str, ...] = ('', 
        'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
        'Jack', 'Queen', 'King')
    _BOTTOM_RANK: int = 1
    _TOP_RANK: int = len(RANK_NAMES) - 1
    _RANKS: tuple[int, ...] = tuple(range(_BOTTOM_RANK, _TOP_RANK+1))

    def _invariant(self) -> bool:
        return (0 <= self._suit < len(self.SUITS)) and \
            (self._BOTTOM_RANK <= self._rank <= self._TOP_RANK)

    def __init__(self, rank: str, suit: str):
        """Create a Playing Card of a given suit and rank."""
        # Pre:
        assert suit.capitalize() in self.SUITS and \
            rank.capitalize() in self.RANK_NAMES
        self._suit: int = self.SUITS.index(suit.capitalize())
        self._rank: int = self.RANK_NAMES.index(rank.capitalize())
        # Post:
        assert self._invariant()

    def suitName(self) -> str:
        """Given a PlayingCard, return the name of its suit."""
        return self.SUITS[self._suit]

    def rankName(self) -> str:
        """Given a PlayingCard, return its rank as a string."""
        return self.RANK_NAMES[self._rank]

    def __str__(self) -> str:
        """Return a string representation of this PlayingCard."""
        return self.rankName() + ' of ' + self.suitName()

    def __eq__(self, other: object) -> bool:
        """Return True iff the PlayingCards have the same rank and suit."""
        # Pre:
        assert self._invariant()

        if not isinstance(other, PlayingCard):
            return NotImplemented
        else:
            otherCard: PlayingCard = cast(PlayingCard, other)
            return (self._rank == otherCard._rank) and \
                (self._suit == otherCard._suit)
    