import unittest
from main import Card

class CardTest(unittest.TestCase):

    def test_suite_greater_than(self):
        self.assertGreater(Card("Ten", "Hearts"), Card("Two", "Hearts"))

    def test_suite_greater_than_equals(self):
        self.assertGreaterEqual(Card("Ten", "Hearts"), Card("Two", "Hearts"))

    def test_suite_less_than(self):
        self.assertLess(Card("Two", "Hearts"),  Card("Ten", "Hearts"))

    def test_suite_less_than_equals(self):
        self.assertLessEqual(Card("Two", "Hearts"),  Card("Ten", "Hearts"))

    def test_suite_equals(self):
        self.assertFalse(Card("Two", "Hearts") == Card("Ten", "Hearts"))

    def test_suite_not_equal(self):
        self.assertNotEqual(Card("Two", "Hearts"),  Card("Ten", "Hearts"))

    def test_ace_of_clubs_beats_king_of_diamonds(self):
        self.assertGreater(Card("Ace", "Clubs"),  Card("King", "Diamonds"))

    def test_hearts_beats_spades(self):
        self.assertGreater(Card("Two", "Hearts"),  Card("Two", "Spades"))



