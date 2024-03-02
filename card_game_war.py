"""
card_game_war.py

Author: Domantas Didžiapetris
Date: 2024-03-02

Description:
    This file contains the code for the card game "War" and its supporting functions, classes.
    
    Classes:
        - Card: a blueprint for the card object. Holds the ranks of the cards.
        - Deck: a blueprint for the deck object. The standard deck consists of 52 cards.
        - Player: a blueprint for the player object.

    Functions:
        - main: invokes the module

    Usage:
        '''
        To-Be-Discussed
        '''
"""


class Card:
    """
    A blueprint for a card object.
    :param rank: the rank (value) of a card.
    """

    rank = [
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
    ]

    # Do I really need this?
    def __init__(self, rank):
        self.rank = rank

    pass


class Deck:
    """Placeholder docstring 1"""

    deck = []
    # def __init__(self):
    pass


class Player:
    """Placeholder docstring 1"""

    # def __init__(self):
    # def get_name()
    pass


def main():
    """Placeholder docstring 1"""
    # player1 = Player._
    # player2 = Player.__
    pass


if __name__ == "__main__":
    main()
