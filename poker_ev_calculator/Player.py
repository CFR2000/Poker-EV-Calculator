'''
This Player class has three attributes: name, stack_size, and in_hand. 
It also has a __init__ method that is called when a new Player object is created, 
and a __repr__ method that is used to create a string representation of the object.
'''

class Player:
    def __init__(self, name, stack_size):
        self.name = name
        self.stack_size = stack_size
        self.in_hand = True
        self.hand = []

    def __repr__(self):
        return f'Player(name={self.name}, stack_size={self.stack_size}, in_hand={self.in_hand}, hand={self.hand})'
