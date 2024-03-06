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

from classes import Deck, Player, Table
from functions import check_for_a_win, check_higher_rank_card


def main():
    """Placeholder docstring 1"""

    deck = Deck()
    table = Table()

    first_players_hand, second_players_hand = deck.split_deck(2)

    player1 = Player("name1", first_players_hand)
    player2 = Player("name2", second_players_hand)

    card1 = player1.get_card()
    card2 = player2.get_card()

    table.add_to_pile([card1, card2])

    check_higher_rank_card(card1, card2)

    deck.show_deck()

    check_for_a_win("Jonas", player1, "Petras", player2)


if __name__ == "__main__":
    main()
