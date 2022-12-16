class Opponent:
    def __init__(self, name, stack_size, hand=None, current_bet=0, in_hand=True):
        self.name = name
        self.stack_size = stack_size
        self.hand = hand
        self.current_bet = current_bet
        self.in_hand = in_hand
