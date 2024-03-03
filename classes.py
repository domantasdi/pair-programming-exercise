"""
classes.py

Author: Domantas Didžiapetris
Date: 2024-03-03

Description:
    - This module hosts the classes necessary for the card game War.

Classes:
    - Card: a blueprint for the card object. Holds the ranks of the cards.
    - Deck: a blueprint for the deck object. The standard deck consists of 52 cards.
    - Player: a blueprint for the player object.
"""

import random

############################################################

SUITS = ["Diamonds", "Clubs", "Hearts", "Spades"]
VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

############################################################

class Card:
    """
    A blueprint for the card object.

    :param suit: the suit of a card.
    :param value: the rank (power) of a card.
    """
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self) -> str:
        return f"{self.value} of {self.suit}"

############################################################

class Deck:
    """Placeholder docstring 1"""

    def __init__(self):
        self.deck = []
        self.build_deck()
        # self.split_deck()


    def build_deck(self) -> list:
        """
        This method iterates over the suits and values and
        builds the deck from the
        """
        for suit in SUITS:
            for value in VALUES:
                self.deck.append(Card(suit, value))


    def shuffle_deck(self) -> list:
        """
        This method shuffles the built deck of cards in
        a random order.
        """
        random.shuffle(self.deck)


    def split_deck(self, no_of_players=2) -> list:
        """
        This function splits the deck between players.

        :param first_hand: cards from the first half of the deck.
        :param second_hand: cards from the second half of the deck.
        """
        first_hand = random.sample(self.deck, 26)
        second_hand = []
        for card in self.deck:
            if card not in first_hand:
                second_hand.append(card)

    def show_deck(self):
        for card in self.deck:
            print(card)



############################################################

# class Player:
#     """Placeholder docstring 1"""
#
#     def __init__(self):
#         pass
#     def get_name():
#         pass

############################################################
