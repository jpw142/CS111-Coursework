#
# hand.py
#
# CS 111, Boston University
#

from card import *

class Hand:
    """ a class for objects that represent a single hand of cards """

    def __init__(self):
        """ constructor for Hand objects """
        self.cards = []

    def __repr__(self):
        """ returns a string representation of the called Hand object (self) """
        return str(self.cards)

    def add_card(self, card):
        """ add the specified Card object (card) to the list of cards
            for the called Hand object (self)
        """
        self.cards += [card]

    def num_cards(self):
        """ returns the number of cards in the called Hand (self) """
        return len(self.cards)

    def get_value(self):
        sum = 0
        for card in self.cards:
            sum += card.get_value()
        return sum

    def has_any(self, rank):
        for card in self.cards:
            if card.rank == rank:
                return True
        return false




