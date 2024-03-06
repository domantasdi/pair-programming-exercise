"""
classes.py

Author: Domantas Didžiapetris
Date: 2024-03-03

Description:
    - This module hosts the classes necessary for the card game War.

Classes:
    - Card: a blueprint for a card. Holds the ranks of the cards.
    - Deck: a blueprint for a deck. The standard deck consists of 52 cards.
    - Player: a blueprint for a player.
"""

import random

from consts import SUITS, VALUES


class Card:
    """
    A blueprint for the card.

    :param suit: the suit of a card.
    :param value: the rank (power) of a card.
    """

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self) -> str:
        return f"{self.value} of {self.suit}"


class Deck:
    """
    A blueprint for the deck of cards.

    :param deck: an empty deck.
    :param build_deck(): builds a deck upon initialization.
    :param shuffle_deck(): shuffles the deck in a random order.
    """

    def __init__(self):
        self.deck = []
        self.build_deck()
        self.shuffle_deck()
        # self.split_deck()

    def build_deck(self) -> list:
        """
        Iterates over the suits and values and
        builds the deck from suits and values.
        """
        for suit in SUITS:
            for value in VALUES:
                self.deck.append(Card(suit, value))

    def shuffle_deck(self) -> list:
        """
        Shuffles the built deck of cards in a random order.
        """
        random.shuffle(self.deck)

    def split_deck(self, no_of_players=2) -> list:
        """
        Splits the deck between players.

        :param first_hand: cards for the first player.
        :param second_hand: cards for the second player.
        """
        if no_of_players == 2:
            first_hand = self.deck[:26]
            second_hand = self.deck[26:]

        return first_hand, second_hand

    def show_deck(self):
        """
        Displays the cards in a human-readable format.
        """
        for card in self.deck:
            print(card)


class Player:
    """
    A blueprint for the player object.

    :param name: the name of the player.
    :param hand: the card hand the player has.
    :param pile: the pile of cards that were set aside.
    """

    def __init__(self, name: str, hand: list[Card]) -> None:
        self.name = name
        self.hand = hand

    def get_card(self):
        """Removes a card from the player's hand."""
        return self.hand.pop()

class Table:
    """
    A blueprint for the table object.

    :param name: the name of the player.
    :param hand: the card hand the player has.
    :param pile: the pile of cards that were set aside.
    """

    def __init__(self) -> None:
        self.pile = []

    def add_to_pile(self, cards: list):
        """Adds a card to a pile."""
        return self.pile.append(cards)
