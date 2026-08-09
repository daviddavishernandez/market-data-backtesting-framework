
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

"""

long term community for future references (relationships + inspiring + networking)
ai agents/trends - adjustment to every market
direct contact with other associations and unis 
no formal agreememnt w university - based off of full relation with ennova
focus on venture capital + startups 
networks: saudi arabia, germany, poland, saudi vc assos, lse entrepreneurs, london, princeton, yale, imperial, hsce (32 or 25 clubs)
us, europe, indonesia, asia, middle east, china, australia 
network navigation thru business and personally 

what they want:
join the network and contribution 
inspire and exchange project ideas with other associations 
they invite us to some workshops, and want us to invite other into our events 
they want some of our speakers if possible sometimes 




"""