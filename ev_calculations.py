from Hand import Hand
import itertools

def determine_best_hand(hand, board):
    # create list of all cards in the hand and on the board
    all_cards = hand + board
    # create a list of all possible 5-card combinations using the all_cards list
    combinations = itertools.combinations(all_cards, 5)
    # initialize variable for the best hand
    best_hand = None
    # iterate through the combinations and determine the best hand
    for combination in combinations:
        current_hand = Hand(combination)
        if best_hand is None or current_hand > best_hand:
            best_hand = current_hand
    return best_hand

def calculate_ev(hand, board, deck, num_iterations):
    win_count = 0
    tie_count = 0
    for i in range(num_iterations):
        deck.shuffle()
        # deal remaining cards
        remaining_cards = [card for card in deck.cards if card not in hand + board]
        remaining_cards = hand + board + remaining_cards[:5-len(board)]
        # determine the best hand for each player
        player_hand = determine_best_hand(hand, board)
        opponent_hand = determine_best_hand(opponent_hand, board)
        # compare hands and update win/tie counts
        if player_hand > opponent_hand:
            win_count += 1
        elif player_hand == opponent_hand:
            tie_count += 1
    # calculate and return EV
    ev = (win_count / num_iterations) - (tie_count / num_iterations / 2)
    return ev



def calculate_raise_amount(current_bet, stack_size, pot_size):
    # calculate the total amount needed to call
    total_needed_to_call = current_bet - pot_size
    # calculate the total amount available to raise
    total_available_to_raise = stack_size - total_needed_to_call
    # calculate the minimum raise amount
    min_raise_amount = current_bet * 2
    # if the total amount available to raise is less than the minimum raise amount, return the total amount available to raise
    if total_available_to_raise < min_raise_amount:
        return total_available_to_raise
    # otherwise, return the minimum raise amount
    else:
        return min_raise_amount