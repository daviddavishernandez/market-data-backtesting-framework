
class PerformanceAnalyzer:
    """
    calculates basic performance metrics for a completed backtest
    the analyzer studies the Portfolio_Value column and compares the strategy with buying and holding the asset
    """
    def __init__(self, results, initial_cash=10000):
        self.results = results
        self.initial_cash = initial_cash

    def get_final_value(self): #returns the final value of the portfolio
        final_value = self.results["Portfolio_Value"].iloc[-1] #iloc[-1] means "give me the last row"
        return final_value

    def get_total_profit(self):
        final_value = self.get_final_value()
        total_profit = final_value - self.initial_cash
        return total_profit

    def get_total_return(self): #calculates the total % return of the strategy 
        final_value = self.get_final_value()
        total_return = ((final_value - self.initial_cash)/ self.initial_cash) * 100
        return total_return

    def get_buy_and_hold_return(self): #calculates the return from buying the asset at the beginning and holding until the end
        # ex: what if we just bought Apple on Day 1 and held it until the end?

        first_price = self.results["Close"].iloc[0] #iloc[0] is the first value
        last_price = self.results["Close"].iloc[-1]

        buy_and_hold_return = ((last_price - first_price)/ first_price) * 100
        return buy_and_hold_return

    def get_max_drawdown(self): #gets largest percentage fall from a portfolio peak
        """
        ex: the portfolio rises from 10000 to 12000 and then it falls to 9000.
            the drawdown is measured from 12000 to 9000
        """
        portfolio_values = self.results["Portfolio_Value"]
        running_max = portfolio_values.cummax() #stores the highest portfolio value reached up to each point in time
        #cummax() keeps track of the highest value seen so far in the data

        drawdowns = (portfolio_values - running_max) / running_max #gets percentage fall from that previous peak

        max_drawdown = drawdowns.min() # the worst drawdown is the lowest value
        max_drawdown = max_drawdown * 100 #convert into percentage 

        return max_drawdown




