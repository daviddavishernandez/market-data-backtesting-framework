# this module will simulate the strategy day by day 
# the backtester wont create the signals, it will excecute them 
#logic: market data -> strategy creates signals -> backtester reads signals -> portfolio buys/sells -> portfolio value is recorded


from backtester.portfolio import Portfolio

class Backtester:
    def __init__(self, data, initial_cash=10000): #stores the strategy data and creates a portfolio
        self.data = data.copy()
        self.portfolio = Portfolio(initial_cash) # creates the portfolio that will execute the trades

    def run(self): #run the backtest one row at a time 
        #shifting the signals:
        #move every signal forward by one row
        #ex: original signal
        # Day 1 -> 0
        # Day 2 -> 1
        # Day 3 -> 1

        #execution signal:
        # Day 1 -> 0
        # Day 2 -> 0
        # Day 3 -> 1

        # Therefore, Day 2's signal is executed on Day 3.
        self.data["Execution_Signal"] = (self.data["Signal"].shift(1).fillna(0))
        #fillna(0) means that after shifting, the first row will be N/A or Nan because there was no previous trading day
        #shift(1) basically just shifts the signals so theyre excecuted the next day 

        portfolio_values = [] # this list will store the value of the portfolio for every day in the dataset

        #go through the market data one day at a time:
        for index,row in self.data.iterrows():

            #represents the price when the next trading day begins
            execution_price = row["Open"] 

            #signal created on the previous trading day
            execution_signal = row["Execution_Signal"]

            # current closing price to calculate worth of portfolio at the end of the day
            closing_price = row["Close"]

            #buy:
            if (execution_signal == 1 and self.portfolio.shares == 0):
                self.portfolio.buy(execution_price)

            #sell:
            elif (execution_signal == 0 and self.portfolio.shares > 0):
                self.portfolio.sell(execution_price)

            #calculate how much the portfolio is worth today
            total_value = self.portfolio.get_total_value(closing_price)

            #store that value in the list that we created in the beginning 
            portfolio_values.append(total_value)

        # finally, we add the daily portfolio values to the DataFrame
        self.data["Portfolio_Value"] = portfolio_values
        return self.data 
    


            
        




