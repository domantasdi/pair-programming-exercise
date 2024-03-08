"""
functions.py

Author: Domantas Didžiapetris
Date: 2024-03-06

Description:
    - This module hosts the functions necessary for the card game War.

Functions:
    - TBD
"""


def draw_cards(table: object, player1: object, player2: object):
    card1 = player1.get_card()
    card2 = player2.get_card()
    table.add_to_pile(card1, card2)
    return (card1, card2)

def compare_cards(table: object, first_players_hand: object, card1: object, second_players_hand: object, card2: object):
    if getattr(card1, "value") > getattr(card2, "value"):
        table.move_pile(first_players_hand)
    elif getattr(card1, "value") < getattr(card2, "value"):
        table.move_pile(second_players_hand)


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
