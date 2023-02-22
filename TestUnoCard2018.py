# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test
from UnoCard2018 import UnoCard2018
from AbstractCard import AbstractCard

class TestUnoCard2018(unittest.TestCase):
    def test_str(self) -> None:
        # Make every color card and ensure that they all come out right
        for suit in UnoCard2018.COLOR_SUITS:
            with self.subTest(suit=suit):
                for rank in UnoCard2018.COLOR_RANK_NAMES:
                    with self.subTest(rank=rank):
                        card: UnoCard2018 = UnoCard2018(rank, suit)
                        self.assertEqual(str(card), suit + ' ' + rank)
                        if rank == '':
                            self.assertEqual(str(card), suit)
                        else:
                            self.assertEqual(str(card), suit + ' ' + rank)

        # Check the wild cards
        for rank in UnoCard2018.WILD_RANK_NAMES:
            with self.subTest(rank=rank):
                suit = 'Wild'
                card = UnoCard2018(rank, suit)
                if rank == '':
                    self.assertEqual(str(card), suit)
                else:
                    self.assertEqual(str(card), suit + ' ' + rank)

    def test_names(self) -> None:
        # Make every color card and ensure that they all come out right
        for suit in UnoCard2018.COLOR_SUITS:
            with self.subTest(suit=suit):
                for rank in UnoCard2018.COLOR_RANK_NAMES:
                    with self.subTest(rank=rank):
                        card: UnoCard2018 = UnoCard2018(rank, suit)
                        self.assertEqual(rank, card.rankName())
                        self.assertEqual(suit, card.suitName())

        # Make every wild card and ensure that they all come out right
        for suit in UnoCard2018.WILD_SUIT:
            with self.subTest(suit=suit):
                for rank in UnoCard2018.WILD_RANK_NAMES:
                    with self.subTest(rank=rank):
                        card = UnoCard2018(rank, suit)
                        self.assertEqual(rank, card.rankName())
                        self.assertEqual(suit, card.suitName())

    def test_eq(self) -> None:
        # Make every color card and ensure that they all come out right
        for suit1 in UnoCard2018.COLOR_SUITS:
            with self.subTest(suit1=suit1):
                for rank1 in UnoCard2018.COLOR_RANK_NAMES:
                    with self.subTest(rank1=rank1):
                        card1: UnoCard2018 = UnoCard2018(rank1, suit1)
                        # Check NotImplemented.  It should fall back to object.__eq__()
                        self.assertFalse(card1 == 'some other value')
                        # Now, check all the cards
                        # Color cards first...
                        for suit2 in UnoCard2018.COLOR_SUITS:
                            with self.subTest(suit2=suit2):
                                for rank2 in UnoCard2018.COLOR_RANK_NAMES:
                                    with self.subTest(rank2=rank2):
                                        card2: UnoCard2018 = UnoCard2018(rank2, suit2)
                                        self.assertFalse(card1 is card2) # Different objects
                                        self.assertEqual((card1 == card2), \
                                            (rank1 == rank2 and suit1 == suit2))
                        # Then wild cards
                        for suit2 in UnoCard2018.WILD_SUIT:
                            with self.subTest(suit2=suit2):
                                for rank2 in UnoCard2018.WILD_RANK_NAMES:
                                    with self.subTest(rank2=rank2):
                                        card2 = UnoCard2018(rank2, suit2)
                                        self.assertFalse(card1 is card2) # Different objects
                                        self.assertFalse(card1 == card2) # Color card never equals a wild card
        # GENERALIZE so it checks equality when the card on the left is a wild card


    @unittest.expectedFailure # Remove this and make test_makeDeck do its proper job
    def test_makeDeck(self) -> None:
        """Assumes the pre-2018 deck with 108 cards and only two kinds of wild card."""
        deck: list[AbstractCard] = UnoCard2018.makeDeck()
        self.assertEqual(len(deck), 112)
        # Finish figuring out if every card has the right number of instances
        # in the deck


if __name__ == '__main__':
    unittest.main()