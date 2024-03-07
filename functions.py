"""
functions.py

Author: Domantas Didžiapetris
Date: 2024-03-06

Description:
    - This module hosts the functions necessary for the card game War.

Functions:
    - TBD
"""

from classes import Table

#table = Table()

def check_for_a_win(first_name: str, first_hand: list, second_name: str, second_hand: list):
    """Checks which player won the game."""

    if len(first_hand) == 0:
        winner = second_name
    elif len(second_hand) == 0:
        winner = first_name

    return f"{winner} is the winner!"


#def check_higher_rank_card(card1: object, card2: object):
#    """Checks the card's rank."""
#    war = False
#
#    if card1["value"] > card2["value"]:
#        pass
