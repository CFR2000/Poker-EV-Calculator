from Card import Card
from Hand import Hand
from Deck import Deck
from Player import Player
from ev_calculations import determine_best_hand, calculate_ev, calculate_raise_amount
from gto_strategy import calculate_gto_strategy, update_gto_strategy
from player_actions import fold, call, raise_, game_is_not_over
from game_state import calculate_pot_size, get_current_bet

from player_actions import fold, call, raise_

def run_game_loop(player, opponent):
    # initialize game state
    player = Player('Alice', 100)
    opponent = Player('Bob', 100)
    hand = player.hand
    board = []
    deck = Deck()
    gto_strategy = None

    # game loop
    while game_is_not_over():
        # get player action
        action = input('Enter action (fold, call, raise): ')
        # update game state
        hand, board, gto_strategy = update_gto_strategy(hand, board, action, deck)
        # execute GTO strategy
        if gto_strategy == 'fold':
            fold(player, opponent, calculate_pot_size())
        elif gto_strategy == 'call':
            call(player, get_current_bet(), calculate_pot_size())
        elif gto_strategy == 'raise':
            raise_amount = calculate_raise_amountmak
            raise_(player, raise_amount, calculate_pot_size())
