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
        return f"{self.value} – {self.suit}"

class Deck:
    """
    A blueprint for the deck of cards.

    Parameters:
        - deck: an empty deck;
    
    Methods:
        - build_deck: builds a deck upon initialization;
        - shuffle_deck: shuffles the deck in a random order;
        - split_deck: splits the deck between players;
        - show_deck: displays the cards in a human readable format.
    """

    def __init__(self) -> None:
        self.deck = []
        self.build_deck()
        self.shuffle_deck()

    def build_deck(self) -> list:
        """
        Iterates over the suits and values and
        builds the deck from suits and values.
        """
        for suit in SUITS:
            for value in VALUES:
                self.deck.append(Card(suit, value))

    def shuffle_deck(self) -> None:
        """
        Shuffles the built deck of cards in a random order.
        """
        random.shuffle(self.deck)

    def split_deck(self) -> list:
        """
        Splits the deck between players.

        :param first_hand: cards for the first player.
        :param second_hand: cards for the second player.
        """
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

    Parameters:
        - name: the name of the player.
        - hand: the card hand the player has.

    Methods:
        - get_card: removes a card from the player's hand.
    """

    def __init__(self, name: str, hand: list[Card]) -> None:
        self.name = name
        self.hand = hand

    def get_card(self) -> object:
        """Removes a card from the player's hand."""
        return self.hand.pop(0)

class Table:
    """
    A blueprint for the table object.

    Parameters:
        - players: the list of players at the table;

    Methods:
        - add_to_pile: adds a card to the table's pile of cards;
        - move_pile: moves the existing pile to a player's hand;
        - clear_pile: clears the pile after moving it
        - show_pile: displays the cards in the pile
    """

    def __init__(self, players: list[Player]) -> None:
        self.players = players
        self.pile = []

    def add_to_pile(self, card1: Card, card2: Card) -> None:
        """Adds a card to the pile."""
        self.pile.append(card1)
        self.pile.append(card2)
        print(f"{str(card1)} \t vs \t {str(card2)}")

    def add_to_pile_face_down(self, card1: Card, card2: Card) -> None:
        """Adds a card to the pile."""
        self.pile.append(card1)
        self.pile.append(card2)
        print("– \t\t vs \t –")

    def move_pile(self, players_hand: list[Card]) -> None:
        """Adds cards from the pile to the player's hand."""
        players_hand.extend(self.pile)
        self.pile.clear()

    def show_pile(self) -> list:
        """A helper method that displays the cards in the pile."""
        for card in self.pile:
            print(str(card))
