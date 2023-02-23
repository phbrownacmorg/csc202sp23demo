# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test
from UnoCard2018 import UnoCard2018
from AbstractCard import AbstractCard

class TestUnoCard2018(unittest.TestCase):
    def test_str(self) -> None:
        # Make every card and ensure that they all come out right
        for suit in UnoCard2018.SUITS:
            with self.subTest(suit=suit):
                rank_list: tuple[str,...] = UnoCard2018.COLOR_RANK_NAMES
                if suit in UnoCard2018.WILD_SUIT:
                    rank_list = UnoCard2018.WILD_RANK_NAMES
                for rank in rank_list:
                    with self.subTest(rank=rank):
                        card: UnoCard2018 = UnoCard2018(rank, suit)
                        self.assertEqual(str(card), (suit + ' ' + rank).strip())

    def test_names(self) -> None:
        # Make every card and ensure that they all come out right
        for suit in UnoCard2018.SUITS:
            with self.subTest(suit=suit):
                rank_list: tuple[str,...] = UnoCard2018.COLOR_RANK_NAMES
                if suit in UnoCard2018.WILD_SUIT:
                    rank_list = UnoCard2018.WILD_RANK_NAMES
                for rank in rank_list:
                    with self.subTest(rank=rank):
                        card: UnoCard2018 = UnoCard2018(rank, suit)
                        self.assertEqual(rank, card.rankName())
                        self.assertEqual(suit, card.suitName())
 
    def test_eq(self) -> None:
        # Make every card for the left side
        for suit1 in UnoCard2018.SUITS:
            with self.subTest(suit1=suit1):
                rank1_list = UnoCard2018.COLOR_RANK_NAMES
                if suit1 in UnoCard2018.WILD_SUIT:
                    rank1_list = UnoCard2018.WILD_RANK_NAMES
                for rank1 in rank1_list:
                    with self.subTest(rank1=rank1):
                        card1: UnoCard2018 = UnoCard2018(rank1, suit1)
                        # Check NotImplemented.  It should fall back to object.__eq__()
                        self.assertFalse(card1 == 'some other value')
                        # Now, check all the cards on the right side
                        for suit2 in UnoCard2018.SUITS:
                            with self.subTest(suit2=suit2):
                                rank2_list = UnoCard2018.COLOR_RANK_NAMES
                                if suit2 in UnoCard2018.WILD_SUIT:
                                    rank2_list = UnoCard2018.WILD_RANK_NAMES
                                for rank2 in rank2_list:
                                    with self.subTest(rank2=rank2):
                                        card2: UnoCard2018 = UnoCard2018(rank2, suit2)
                                        self.assertFalse(card1 is card2) # Different objects
                                        self.assertEqual((card1 == card2), \
                                            (rank1 == rank2 and suit1 == suit2))

    def test_makeDeck(self) -> None:
        """Assumes the pre-2018 deck with 108 cards and only two kinds of wild card."""
        deck: list[AbstractCard] = UnoCard2018.makeDeck()
        self.assertEqual(len(deck), 112)
        # Finish figuring out if every card has the right number of instances
        # in the deck
        counts: list[int] = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, # Color ranks, numbers
                             2, 2, 2,                      # Color ranks, non-numbers
                             4, 4, 1, 3]                         # Wild cards
        for suit in UnoCard2018.SUITS:
            with self.subTest(suit=suit):
                rank_list: tuple[str,...] = UnoCard2018.COLOR_RANK_NAMES
                if suit in UnoCard2018.WILD_SUIT:
                    rank_list = UnoCard2018.WILD_RANK_NAMES
                for rank in rank_list:
                    with self.subTest(rank=rank):
                        card: UnoCard2018 = UnoCard2018(rank, suit)
                        self.assertEqual(deck.count(card), counts[card._rank])

if __name__ == '__main__':
    unittest.main()