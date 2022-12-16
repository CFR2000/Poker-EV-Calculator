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