class Deck:
  def __init__(self):
    self.cards = []
    for suit in ['hearts', 'diamonds', 'spades', 'clubs']:
            for rank in range(2, 11):
                self.cards.append(Card(str(rank), suit))
            for rank in ['Jack', 'Queen', 'King', 'Ace']:
                self.cards.append(Card(rank, suit))
