from Card import Card
from Hand import Hand
from Deck import Deck
from ev_calculations import determine_best_hand, calculate_ev, calculate_raise_amount
from gto_strategy import calculate_gto_strategy, update_gto_strategy
from game_actions import fold, call, raise_, game_is_not_over

def run_game_loop():
    # initialize game state
    hand = [Card('Ace', 'hearts'), Card('King', 'diamonds')]
    board = []
    deck = Deck()
    gto_strategy = None

    # game loop
    while game_is_not_over:
        # get player action
        action = input('Enter action (fold, call, raise): ')
        # update game state
        hand, board, gto_strategy = update_gto_strategy(hand, board, action, deck)
        # execute GTO strategy
        if gto_strategy == 'fold':
            fold()
        elif gto_strategy == 'call':
            call()
        elif gto_strategy == 'raise':
            raise_amount = calculate_raise_amount()
            raise_(raise_amount)
