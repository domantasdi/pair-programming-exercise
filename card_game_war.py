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
from functions import draw_cards, compare_cards


def main():
    """Placeholder docstring 1"""

    deck = Deck()

    first_players_hand, second_players_hand = deck.split_deck(2)

    player1 = Player("name1", first_players_hand)
    player2 = Player("name2", second_players_hand)

    table = Table([player1, player2])

    while len(first_players_hand) != 0 or len(second_players_hand) != 0:
        
        card1, card2 = draw_cards(table, player1, player2)
        
        while getattr(card2, "value") == getattr(card1, "value"):
            print(f"War!")
            for _ in range(1,3):
                card1, card2 = draw_cards(table, player1, player2)
            compare_cards(table, first_players_hand, card1, second_players_hand, card2)
        else:
            compare_cards(table, first_players_hand, card1, second_players_hand, card2)
        
        #table.compare_cards(card1, card2)
        #table.show_pile()




if __name__ == "__main__":
    main()
