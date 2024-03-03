"""
card_game_war.py

Author: Domantas Didžiapetris
Date: 2024-03-02

Description:
    This file contains the code for the card game "War" and its supporting functions.

    Functions:
        - main: invokes the module

    Usage:
        '''
        To-Be-Discussed
        '''
"""
from classes import Deck, Card, Player


def main():
    """Placeholder docstring 1"""

    kalade = Deck()
    first_half_deck, second_half_deck = kalade.split_deck(2)
    player1 = Player('name1', first_half_deck)
    player2 = Player('name2', second_half_deck)
    kalade.show_deck()


if __name__ == "__main__":
    main()
