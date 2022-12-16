from player import Player
from opponent import Opponent
from board import Board
from deck import Deck


def calculate_pot_size():
    # code to calculate the current pot size
    pot_size = 0
    for player in [player, opponent]:
        pot_size += player.current_bet
    return pot_size

def get_current_bet():
    # code to get the current bet amount
    current_bet = max(player.current_bet, opponent.current_bet)
    return current_bet


def get_player_stack_size(player):
    # code to retrieve the current stack size of a player
    stack_size = player.stack_size
    return stack_size

def get_board_cards():
    # code to retrieve the current cards on the board
    cards = board.cards
    return cards

def get_deck_cards():
    # code to retrieve the current cards in the deck
    cards = deck.cards
    return cards

def update_player_stack_size(player, amount):
    # code to update the stack size of a player by a given amount
    player.stack_size += amount

def update_board_cards(cards):
    # code to add cards to the board
    board.cards += cards

def update_deck_cards(cards):
    # code to add cards to the deck
    deck.cards += cards
