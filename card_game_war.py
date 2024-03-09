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

import time
from classes import Deck, Player, Table
from functions import (
    draw_cards,
    draw_cards_face_down,
    compare_cards,
    check_win_condition,
)


def main():
    """Main function that runs the game."""

    deck = Deck()

    first_players_hand, second_players_hand = deck.split_deck(2)

    player1 = Player("Tom", first_players_hand)
    player2 = Player("Jerry", second_players_hand)

    table = Table([player1, player2])

    while len(first_players_hand) != 0 or len(second_players_hand) != 0:
        time.sleep(0.001)

        try:
            card1, card2 = draw_cards(table, player1, player2)
        except IndexError:
            break

        while getattr(card2, "value") == getattr(card1, "value"):
            print("War!")
            for _ in range(1, 2):
                try:
                    card1, card2 = draw_cards_face_down(table, player1, player2)
                except IndexError:
                    break
            try:
                card1, card2 = draw_cards(table, player1, player2)
            except IndexError:
                break
            compare_cards(table, first_players_hand, card1, second_players_hand, card2)
        compare_cards(table, first_players_hand, card1, second_players_hand, card2)

        check_win_condition(first_players_hand, player1.name, second_players_hand, player2.name)


if __name__ == "__main__":
    main()
