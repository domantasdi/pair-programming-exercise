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
        self.shuffle_deck()
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

        :param first_hand: cards for the first player.
        :param second_hand: cards for the second player.
        """
        if no_of_players == 2:
            first_hand = self.deck[:26]
            second_hand = self.deck[26:]


        return first_hand, second_hand


    def show_deck(self):
        """
        This method displays the cards in a human-readable format.
        """
        for card in self.deck:
            print(card)


############################################################

class Player:
    """Placeholder docstring 1"""
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand


    def get_name():
        pass

############################################################
