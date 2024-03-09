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

import sys
from classes import Deck, Player, Table
from functions import (
    draw_cards,
    draw_cards_face_down,
    compare_cards,
    check_win_condition,
)


def main():
    """Main function that runs the game."""

    # Here I initialize the deck as an object
    deck = Deck()

    # Here I split the deck into two hands, for two players
    first_players_hand, second_players_hand = deck.split_deck(2)

    # Here I initialize the two players

    p1_name = str(sys.argv[1])
    p2_name = str(sys.argv[2])

    player1 = Player(p1_name, first_players_hand)
    player2 = Player(p2_name, second_players_hand)

    # Here I initialize the table
    table = Table([player1, player2])

    # Here I run a loop, as long as one of the players' doesn't have any cards
    while True:
        # Here I add a sleep timer so the program doesn't run too fast
        if check_win_condition(first_players_hand, player1.name, second_players_hand, player2.name):
            break

        # Here I try to draw two cards, except there are no more cards
        try:
            card1, card2 = draw_cards(table, player1, player2)
        except IndexError:
            break

        while getattr(card2, "value") == getattr(card1, "value"):
            print("War!")
            try:
                for _ in range(1, 2):
                    card1, card2 = draw_cards_face_down(table, player1, player2)
                    break
                card1, card2 = draw_cards(table, player1, player2)
            except IndexError:
                break
        compare_cards(table, first_players_hand, card1, second_players_hand, card2)



if __name__ == "__main__":
    main()
