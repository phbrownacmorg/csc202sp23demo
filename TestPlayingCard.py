# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test
from PlayingCard import PlayingCard

class TestPlayingCard(unittest.TestCase):
    # All methods whose names start with "test"
    # will be treated as tests
    def test_str(self) -> None:
        # Make every card and ensure that they all come out right
        for suit in PlayingCard.SUITS:
            with self.subTest(suit=suit):
                for rank in PlayingCard.RANK_NAMES[PlayingCard._BOTTOM_RANK:]:
                    with self.subTest(rank=rank):
                        card: PlayingCard = PlayingCard(rank, suit)
                        self.assertEqual(str(card), rank + ' of ' + suit)
        
    def test_names(self) -> None:
        # Make every card and ensure that they all come out right
        for suit in PlayingCard.SUITS:
            with self.subTest(suit=suit):
                for rank in PlayingCard.RANK_NAMES[PlayingCard._BOTTOM_RANK:]:
                    with self.subTest(rank=rank):
                        card: PlayingCard = PlayingCard(rank, suit)
                        self.assertEqual(rank, card.rankName())
                        self.assertEqual(suit, card.suitName())

    def test_eq(self) -> None:
        # Make every card and ensure that they all come out right
        for suit1 in PlayingCard.SUITS:
            with self.subTest(suit1=suit1):
                for rank1 in PlayingCard.RANK_NAMES[PlayingCard._BOTTOM_RANK:]:
                    with self.subTest(rank1=rank1):
                        card1: PlayingCard = PlayingCard(rank1, suit1)
                        # Check NotImplemented.  It should fall back to object.__eq__()
                        self.assertFalse(card1 == 'some other value')
                        # Now, check all the cards
                        for suit2 in PlayingCard.SUITS:
                            with self.subTest(suit2=suit2):
                                for rank2 in PlayingCard.RANK_NAMES[PlayingCard._BOTTOM_RANK:]:
                                    with self.subTest(rank2=rank2):
                                        card2: PlayingCard = PlayingCard(rank2, suit2)
                                        self.assertFalse(card1 is card2) # Different objects
                                        self.assertEqual((card1 == card2), \
                                            (rank1 == rank2 and suit1 == suit2))

    def test_makeDeck(self) -> None:
        deck: list[PlayingCard] = PlayingCard.makeDeck()
        self.assertEqual(len(deck), 52)
        for suit in PlayingCard.SUITS:
            with self.subTest(suit=suit):
                for rank in PlayingCard.RANK_NAMES[PlayingCard._BOTTOM_RANK:]:
                    with self.subTest(rank=rank):
                        card: PlayingCard = PlayingCard(rank, suit)
                        self.assertTrue(card in deck)

if __name__ == '__main__':
    unittest.main()