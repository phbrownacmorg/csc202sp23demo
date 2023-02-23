# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test
from UnoCard import UnoCard
from AbstractCard import AbstractCard

# test_makeDeck assumes the pre-2018 deck with 108 cards and
# only two types of wild card.  The other tests do not care.
class TestUnoCard(unittest.TestCase):
    def test_str(self) -> None:
        # Make every card and ensure that they all come out right
        for suit in UnoCard.SUITS:
            with self.subTest(suit=suit):
                rank_list: tuple[str,...] = UnoCard.COLOR_RANK_NAMES
                if suit in UnoCard.WILD_SUIT:
                    rank_list = UnoCard.WILD_RANK_NAMES
                for rank in rank_list:
                    with self.subTest(rank=rank):
                        card: UnoCard = UnoCard(rank, suit)
                        self.assertEqual(str(card), (suit + ' ' + rank).strip())

    def test_names(self) -> None:
        # Make every card and ensure that they all come out right
        for suit in UnoCard.SUITS:
            with self.subTest(suit=suit):
                rank_list: tuple[str,...] = UnoCard.COLOR_RANK_NAMES
                if suit in UnoCard.WILD_SUIT:
                    rank_list = UnoCard.WILD_RANK_NAMES
                for rank in rank_list:
                    with self.subTest(rank=rank):
                        card: UnoCard = UnoCard(rank, suit)
                        self.assertEqual(rank, card.rankName())
                        self.assertEqual(suit, card.suitName())

    def test_eq(self) -> None:
        # Make every card for the left side
        for suit1 in UnoCard.SUITS:
            with self.subTest(suit1=suit1):
                rank1_list = UnoCard.COLOR_RANK_NAMES
                if suit1 in UnoCard.WILD_SUIT:
                    rank1_list = UnoCard.WILD_RANK_NAMES
                for rank1 in rank1_list:
                    with self.subTest(rank1=rank1):
                        card1: UnoCard = UnoCard(rank1, suit1)
                        # Check NotImplemented.  It should fall back to object.__eq__()
                        self.assertFalse(card1 == 'some other value')
                        # Now, check all the cards on the right side
                        for suit2 in UnoCard.SUITS:
                            with self.subTest(suit2=suit2):
                                rank2_list = UnoCard.COLOR_RANK_NAMES
                                if suit2 in UnoCard.WILD_SUIT:
                                    rank2_list = UnoCard.WILD_RANK_NAMES
                                for rank2 in rank2_list:
                                    with self.subTest(rank2=rank2):
                                        card2: UnoCard = UnoCard(rank2, suit2)
                                        self.assertFalse(card1 is card2) # Different objects
                                        self.assertEqual((card1 == card2), \
                                            (rank1 == rank2 and suit1 == suit2))

    # @unittest.expectedFailure # Remove this and make test_makeDeck do its proper job
    def test_makeDeck(self) -> None:
        """Assumes the pre-2018 deck with 108 cards and only two kinds of wild card."""
        deck: list[AbstractCard] = UnoCard.makeDeck()
        self.assertEqual(len(deck), 108)
        # Finish figuring out if every card has the right number of instances
        # in the deck
        counts: list[int] = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, # Color ranks, numbers
                             2, 2, 2,                      # Color ranks, non-numbers
                             4, 4]                         # Wild cards
        for suit in UnoCard.SUITS:
            with self.subTest(suit=suit):
                rank_list: tuple[str,...] = UnoCard.COLOR_RANK_NAMES
                if suit in UnoCard.WILD_SUIT:
                    rank_list = UnoCard.WILD_RANK_NAMES
                for rank in rank_list:
                    with self.subTest(rank=rank):
                        card: UnoCard = UnoCard(rank, suit)
                        self.assertEqual(deck.count(card), counts[card._rank])

if __name__ == '__main__':
    unittest.main()