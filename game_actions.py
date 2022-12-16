def game_is_not_over():
    # check if there are enough cards in the deck for the game to continue
    if len(deck) < 2:
        return False
    # check if there is at least one player with a stack size greater than 0
    if player.stack_size > 0 and opponent.stack_size > 0:
        return True
    else:
        return False



'''
This function contains code to update the game state to reflect the fold action. 
It sets the player.in_hand variable to False, indicating that the player has folded. 
It then calculates the pot size and updates the stack sizes of the player and opponent accordingly.
'''


def fold():
    # code to execute a fold action
    # update game state to reflect the fold action
    player.in_hand = False
    # update player and opponent stack sizes
    pot_size = calculate_pot_size()
    player.stack_size -= pot_size / 2
    opponent.stack_size += pot_size / 2