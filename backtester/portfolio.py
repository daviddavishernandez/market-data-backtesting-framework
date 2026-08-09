"""
this module will keep track of the portfolio while the strategy is running
basically it will be able to answer: 
how much cash do i have, how many shares do i own, and what is my portfolio worth?

it will manage:
- starting cash
- buying shares
- selling shares
- number of shares owned
- current cash
- total portfolio value

the file will not tell us when to buy or sell (thats the startegy file), however it will excecute the decisions
(basically works hand to hand with the startegy module to be able to coordinate the actual positions on the stock) 

"""

class Portfolio: #keeps track of the trading portfolio 
    """
    this portfolio will store: 
        - current cash
        - number of shares owned
        - total portfolio value
    
    it will be able to:
        - bull/sell shares 
        - calculate the current total value 

    this class will not decide when to trade, it will only excecute trades when instructed.
    """
    def __init__(self, initial_cash = 10000): #the parameter initial cash (money available) will be a float 
        self.initial_cash = initial_cash #stores amount of money we started with 

        #current available cash. initially this will be the same value as the amount of cash that we begin with 
        self.cash = initial_cash

        #this is the number of shares that we currently own. initially, we own none. 
        self.shares = 0

    def buy(self,price): #uses available cash to buy as many whole shares as possible
        #parameter price is a float; price of one share at the moment of purchase

        #lets calculate how many shares we can afford 
        shares_to_buy = int(self.cash // price) # // means floor division

        #if we ant even afford one share, then we can't buy anything 
        if shares_to_buy == 0:
            return #this return will exit the method 

        #calculate the total cost of the purchase 
        total_cost = shares_to_buy * price

        #remove money used for our purchase from our cash 
        self.cash = self.cash - total_cost

        #add the purchased hares into our portfolio 
        self.shares = self.shares + shares_to_buy

    def sell(self,price): #sells all shares currently owned
        #price - float; price of one share at the moment of sale

        #if we dont own shares, we cant sell any 
        if self.shares == 0:
            return 

        #calculate how much money we receive from the sale
        money_received = self.shares * price

        #add the sale proceeds to our cash
        self.cash = self.cash + money_received

        #after selling everything, we have zero shares left
        self.shares = 0 #this is simplified to sell all of the shares completely, we will not consider if you went to only sell some shares.
        #this is tied up to the fact that our strategy is based off of 2 signals (1 or 0)
        #therefore, we will use this assumption and not use partial position,rebalance, buying/selling percentages, etc.

    def get_total_value(self, current_price): #calculates the current value of the whole portfolio
        # parameter c_p is a float - current market price of one share

        # calculate how much our shares are worth right now
        shares_value = self.shares * current_price 

        # therefore, our portfolio value is: cash + market value of owned shares   
        total_value = self.cash + shares_value

        return total_value # output of function will be a float - cash + current value of all shares owned









        





