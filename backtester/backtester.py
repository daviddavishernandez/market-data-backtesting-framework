# this module will simulate the strategy day by day 
# the backtester wont create the signals, it will excecute them 
#logic: market data -> strategy creates signals -> backtester reads signals -> portfolio buys/sells -> portfolio value is recorded


from backtester.portfolio import Portfolio

class Backtester:
    def __init__(self, data, initial_cash=10000): #stores the strategy data and creates a portfolio
        self.data = data.copy()
        self.portfolio = Portfolio(initial_cash) # creates the portfolio that will execute the trades

    def run(self): #run the backtest one row at a time 
        portfolio_values = [] # this list will store the value of the portfolio for every day in the dataset

        #go through the market data one day at a time:
        for index,row in self.data.iterrows():

            #get the closing price for the current day
            price = row["Close"]

            #get the trading signal for the current day
            signal = row["Signal"]

            #if signal = 1 and we don't already own shares, buy as many shares as possible
            if signal == 1 and self.portfolio.shares == 0:
                self.portfolio.buy(price)

            #if signal = 0 and we own shares, sell all of them
            elif signal == 0 and self.portfolio.shares > 0:
                self.portfolio.sell(price)

            #calculate how much the portfolio is worth today
            total_value = self.portfolio.get_total_value(price)

            #store that value in the list that we created in the beginning 
            portfolio_values.append(total_value)

        # finally, we add the daily portfolio values to the DataFrame
        self.data["Portfolio_Value"] = portfolio_values
        return self.data 
    


            
        




