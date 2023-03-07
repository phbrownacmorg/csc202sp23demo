# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test
from AbstractCard import AbstractCard
from Deck import Deck
from PlayingCard import PlayingCard
from UnoCard import UnoCard
import random

class TestDeck(unittest.TestCase):

    # setUp is run before every test
    def setUp(self) -> None:
        self.emptyDeck = Deck([])
        self.normalDeck = Deck(PlayingCard.makeDeck())
        random.seed(144000)

    # All methods whose names start with "test"
    # will be treated as tests
    def testLen(self) -> None:
        self.assertEqual(len(self.emptyDeck), 0)
        self.assertEqual(len(self.normalDeck), 52)
        deck = Deck(UnoCard.makeDeck())
        self.assertEqual(len(deck), 108) # Or it would be if UnoDeck.makeDeck() had been implemented
    
    def testContains(self) -> None:
        card: PlayingCard = PlayingCard('King', 'Spades')
        self.assertFalse(card in self.emptyDeck)
        self.assertTrue(card in self.normalDeck)
        # Exclude the king of spades from the deck
        self.assertFalse(card in Deck(PlayingCard.makeDeck()[:-1]))

    def testDeal(self) -> None:
        card: PlayingCard = PlayingCard('King', 'Spades')
        deck: Deck = self.normalDeck
        self.assertTrue(len(deck) == 52 and card in deck)
        self.assertEqual(deck.deal(), card)
        self.assertEqual(len(deck), 51)
        self.assertFalse(card in deck)

    # Polymorphism!
    def testStr(self) -> None:
        # Deck contains *both* PlayingCards and UnoCards
        cards: list[AbstractCard] = PlayingCard.makeDeck() + UnoCard.makeDeck()
        deck: Deck = Deck(cards)
        self.assertEqual(len(deck), 160)

        # Each card converts itself to a string correctly, depending on its type
        print(str(deck))
        for i in range(159, -1, -1): # Backwards through the deck
            card: AbstractCard = deck.deal()
            # Polymorphic, again
            self.assertEqual(str(card), str(cards[i]))

    def testPickCard(self) -> None:
        self.assertEqual(len(self.normalDeck), 52)
        card: AbstractCard = self.normalDeck.pickACard()
        self.assertEqual(len(self.normalDeck), 51) # Removed exactly 1 card
        self.assertFalse(card in self.normalDeck) # Card is no longer in deck
        print('\n', card)
        self.assertEqual(card, PlayingCard('7', 'Hearts')) # Not the King of Spades

if __name__ == '__main__':
    unittest.main()