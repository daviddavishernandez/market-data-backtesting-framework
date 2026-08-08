
from abc import ABC, abstractmethod

class Strategy(ABC):
    """
    this will lbe the general class for all of the different trading strategies that emerge.

    every stratgey will:
    - recieve market data 
    - generate trading signals 
    - return the updated DataFrame 

    the class doesnt necessarily contain any trading strategy, its just defines comon structure and rules.
    """

    def __init__(self, data):
        self.data = data # historical market data containing prices and dates

    @abstractmethod
    def generate_signals(self):
        pass 

        """
        this function will basically create the trading signals for the strategy.
        every child class strategy will strictly create its own version thats why we use the abstractmethod. 
        """

"""

SIGNAL - a signal is basically an instruction created by a strategy
throughout this project i will be using: 

Signal = 1 -- Own the asset -- own/continue to own 
Signal = 0 -- Stay in cash -- do not own/sell/remain outside 

"""