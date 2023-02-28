from AbstractCard import AbstractCard
from UnoCard import UnoCard

class UnoCard2018(UnoCard):
    """Class to represent an UnoCard from 2018 and later."""
    
    # Inherit the suits from UnoCard; nothing changed there
    # Inherit the color ranks from UnoCard; nothing changed there
    # The wild rank names did change, though
    WILD_RANK_NAMES: tuple[str, ...] = ('', 'Draw 4', 'Shuffle Deck', 'Customizable')
    RANK_NAMES: tuple[str, ...] = UnoCard.COLOR_RANK_NAMES + WILD_RANK_NAMES
    # Inherit _BOTTOM_RANK and _TOP_COLOR_RANK
    _TOP_RANK: int = len(RANK_NAMES) - 1

    # Inherit _invariant().  Everything that changed is explicitly polymorphic ('self.')

    # __init__ is a special case.  Always override.
    def __init__(self, rank: str, suit: str):
        """Constructor."""
        # Pre:
        assert ((suit.title() in self.COLOR_SUITS and 
                   rank.title() in self.COLOR_RANK_NAMES) or 
               (suit.title() in self.WILD_SUIT and
                   rank.title() in self.WILD_RANK_NAMES))
        super().__init__(rank, suit)
        # Postcondition is exactly the one that's checked in AbstractCard.


    # Inherit suitName() from AbstractCard.
    # Inherit rankName() from AbstractCard.
    # Inherit __eq__() from AbstractCard.
    # Inherit __str__() from AbstractCard.

    @classmethod
    def makeDeck(cls) -> list[AbstractCard]:
        """Make a post-2018 Uno deck."""
        deck: list[AbstractCard] = []
        for suit in cls.SUITS:
            if suit in cls.COLOR_SUITS:
                for rank in cls.COLOR_RANK_NAMES:
                    deck.append(UnoCard2018(rank, suit))
                    if rank != '0':
                        deck.append(UnoCard2018(rank, suit))
            else: # suit == 'Wild'
                for rank in cls.WILD_RANK_NAMES:
                    if rank == 'Shuffle Deck':
                        deck.append(UnoCard2018(rank, suit)) # only one
                    elif rank == 'Customizable':
                        for i in range(3):
                            deck.append(UnoCard2018(rank, suit))
                    else:
                        for i in range(4):
                            deck.append(UnoCard2018(rank, suit))
        # Post:
        assert len(deck) == 112
        return deck
