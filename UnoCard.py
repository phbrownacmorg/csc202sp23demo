from AbstractCard import AbstractCard

class UnoCard(AbstractCard):
    """Class to represent an Uno card.  This class assumes the pre-2018 deck,
    with 108 cards and only two kinds of wild cards."""

    COLOR_SUITS: tuple[str,...] = ('Red', 'Yellow', 'Green', 'Blue')
    WILD_SUIT: tuple[str] = ( 'Wild' ,) # Comma at the end tells Python this is a tuple
    SUITS: tuple[str,...] = COLOR_SUITS + WILD_SUIT

    COLOR_RANK_NAMES: tuple[str, ...] = ('0', '1', '2', '3', '4', 
                                         '5', '6', '7', '8', '9', 
                                         'Skip', 'Reverse', 'Draw 2')
    WILD_RANK_NAMES: tuple[str, ...] = ('', 'Draw 4')
    RANK_NAMES: tuple[str, ...] = COLOR_RANK_NAMES + WILD_RANK_NAMES
    _TOP_COLOR_RANK: int = len(COLOR_RANK_NAMES) - 1
    _TOP_RANK: int = len(RANK_NAMES) - 1

    # Overrides AbstractCard._invariant()
    def _invariant(self) -> bool:
        """Class invariant."""
        # This UnoCard is a valid color card
        colorOK: bool = ((self._BOTTOM_RANK <= self._rank <= self._TOP_COLOR_RANK)
            and (self._suit < len(self.COLOR_SUITS)))

        # This UnoCard is a valid wild card
        wildOK: bool = ((self._TOP_COLOR_RANK < self._rank <= self._TOP_RANK)
            and (len(self.COLOR_SUITS) <= self._suit < len(self.SUITS)))

        return ((colorOK and (not wildOK)) or (wildOK and (not colorOK)))

    def __init__(self, rank: str, suit: str):
        """Constructor"""
        # Pre:
        assert ((suit.title() in self.COLOR_SUITS and 
                   rank.title() in self.COLOR_RANK_NAMES) or 
               (suit.title() in self.WILD_SUIT and
                   rank.title() in self.WILD_RANK_NAMES))
        super().__init__(rank, suit)
        # Postcondition is exactly the one that's checked in AbstractCard.

    @classmethod
    def makeDeck(cls) -> list[AbstractCard]:
        """Make an Uno deck."""
        deck: list[AbstractCard] = []
        for suit in UnoCard.SUITS:
            if suit in UnoCard.COLOR_SUITS:
                for rank in UnoCard.COLOR_RANK_NAMES:
                    deck.append(UnoCard(rank, suit))
                    if rank != '0':
                        deck.append(UnoCard(rank, suit))
            else:
                for rank in UnoCard.WILD_RANK_NAMES:
                    for i in range(4):
                        deck.append(UnoCard(rank, suit))
        # Post:
        assert len(deck) == 108
        return deck
