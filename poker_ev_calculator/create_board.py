from Card import Card

def create_board(flop=None, turn=None, river=None):
    # create empty board
    board = []
    # add flop cards to board
    if flop:
        board.extend(flop)
    # add turn card to board
    if turn:
        board.append(turn)
    # add river card to board
    if river:
        board.append(river)
    return board

# # example usage
# board = create_board([Card('Ace', 'hearts'), Card('King', 'diamonds'), Card('Queen', 'spades')], turn=Card('Jack', 'clubs'), river=Card('Ten', 'hearts'))
# print(board)  # [Card(rank='Ace', suit='hearts'), Card(rank='King', suit='diamonds'), Card(rank='Queen', suit='spades'), Card(rank='Jack', suit='clubs'), Card(rank='Ten', suit='hearts')]
