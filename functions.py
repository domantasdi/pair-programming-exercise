"""
functions.py

Author: Domantas Didžiapetris
Date: 2024-03-06

Description:
    - This module hosts the functions necessary for the card game War.

Functions:
    - TBD
"""


def draw_cards(table: object, player1: object, player2: object) -> tuple:
    """Draws two cards and adds them to the pile"""
    card1 = player1.get_card()
    card2 = player2.get_card()
    table.add_to_pile(card1, card2)
    return (card1, card2)


def draw_cards_face_down(table: object, player1: object, player2: object) -> tuple:
    """Draws two cards and adds them to the pile"""
    card1 = player1.get_card()
    card2 = player2.get_card()
    table.add_to_pile_face_down(card1, card2)
    return (card1, card2)


def compare_cards(
    table: object,
    first_players_hand: object,
    card1: object,
    second_players_hand: object,
    card2: object,
) -> None:
    """Compares cards and moves the pile to the player's hand."""
    if getattr(card1, "value") > getattr(card2, "value"):
        table.move_pile(first_players_hand)
    elif getattr(card1, "value") < getattr(card2, "value"):
        table.move_pile(second_players_hand)


def check_win_condition(
    first_players_hand: list,
    first_name: str,
    second_players_hand: list,
    second_name: str,
) -> str:
    """Checks who won the game."""
    if len(first_players_hand) == 0:
        print(f"{second_name} won!")
    elif len(second_players_hand) == 0:
        print(f"{first_name} won!")
