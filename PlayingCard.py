from AbstractCard import AbstractCard

class PlayingCard(AbstractCard):
    """Class to represent a playing card of the usual (French) type.
    Objects of this type are immutable once created."""

    SUITS: tuple[str, ...] = ('Clubs', 'Diamonds', 'Hearts', 'Spades') # No particular order
    RANK_NAMES: tuple[str, ...] = ('', 
        'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
        'Jack', 'Queen', 'King')
    _BOTTOM_RANK: int = 1
    _TOP_RANK: int = len(RANK_NAMES) - 1

    def __init__(self, rank: str, suit: str):
        """Create a Playing Card of a given suit and rank."""
        super().__init__(rank, suit)

    # Overrides __str__ from AbstractCard
    def __str__(self) -> str:
        """Return a string representation of this PlayingCard."""
        return self.rankName() + ' of ' + self.suitName()
    
    @classmethod
    def makeDeck(cls) -> list[AbstractCard]:
        """Make the whole deck of playing cards. (Jokers are not included.)"""
        # Pre: none
        deck: list[AbstractCard] = []
        for suit in cls.SUITS:
            for rank in cls.RANK_NAMES[cls._BOTTOM_RANK:]:
                deck.append(PlayingCard(rank, suit))
        # Post:
        assert len(deck) == len(cls.SUITS) * (cls._TOP_RANK - cls._BOTTOM_RANK + 1)
        return deck
