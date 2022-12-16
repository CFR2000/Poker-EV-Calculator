# *Poker EV Calculation*
This project is focused on building a tool to calculate the expected value (EV) of poker hands in the popular card game Texas Holdem. The tool will allow players to make more informed decisions by analyzing the EV of different hand scenarios and betting strategies.

### *Structured Organisation of Poker EV Calculator*
The project is organized into the following files and directories:

1. ev_calculator.py: contains the EVCalculator class, which is responsible for calculating the EV of a hand scenario.
2. Card.py: contains the Card class, which represents a playing card.
3. Hand.py: contains the Hand class, which represents a poker hand.
4. Deck.py: contains the Deck class, which represents a deck of playing cards.
5. game_loop.py: contains the run_game_loop function, which is the main game loop for the poker EV calculation program.
6. game_state.py: contains functions to update the game state and execute game actions (e.g. fold, call, raise).
7. gto_strategy.py: contains the calculate_gto_strategy function, which calculates the game theory optimal (GTO) strategy for a given hand and game state.
8. Player.py: contains the Player class, which represents a poker player.
9. Opponent.py: contains the Opponent class, which represents an opponent in the game.

## *Getting Started*
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

#### *Prerequisites*
- Python 3.7 or higher
- A poker software or platform to integrate the EV calculator

#### *Installing*
To install the EV calculator, follow these steps:

1. Clone the repository to your local machine: 
'''git clone https://github.com/user/poker-ev-calculator.git'''

2. Navigate to the project directory: 
'''cd poker-ev-calculator'''

3. Install the required dependencies: 
'''pip install -r requirements.txt'''

### *Usage*
To use the EV calculator, follow these steps:

1. Import the 'ev_calculator' module into your poker software or platform:
from ev_calculator import ev_calculator

2. Use the calculate_ev function to calculate the EV of a hand scenario:

'''hand = [Card('Ace', 'hearts'), Card('King', 'diamonds')]
board = [Card('Queen', 'hearts'), Card('Jack', 'hearts'), Card('Ten', 'hearts')]
stack_size = 1000
opponent_stack_sizes = [500, 1000, 2000]
bet_sizes = [100, 200, 300]
ev = ev_calculator.calculate_ev(hand, board, stack_size, opponent_stack_sizes, bet_sizes)
print(ev)'''


### *Contributing*
We welcome contributions to this project. If you have an idea for a feature or improvement, please open an issue to discuss it before submitting a pull request.
