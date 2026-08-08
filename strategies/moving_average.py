# import the Strategy parent class from the other module 
from strategies.strategy import Strategy

class MovingAverageStrategy(Strategy):
    # moving average - calculates the average price over a selected number of recent days
    # do average of a specific set of days, when more days appear, the oldest days get ignored from the calculation maintaining the specific set always the same. 
    # ex: the first set is - (day 1 + day 2 + day 3)/3 then the next time its - (day 2 + day 3 + day 4)/3
    # day 1 is deleted and day 4 is incorporated

    """
    trading strategy based on two moving averages

    the strategy compares:
        - a short moving average
        - a long moving average

    If the short moving average is above the long moving average,
    the strategy creates a Signal of 1

    If the short moving average is below or equal to the long moving
    average, the strategy creates a Signal of 0
    """

    def __init__(self, data, short_window = 3, long_window = 5): #when we use larger data sets we can change these values 
        """
        stores the market data and the moving-average periods

        here is a rundown of the purpose of the three parameters:
        - data : pandas.DataFrame
            historical market data

        -- short_window : int
            number of recent days used for the short moving average

        - long_window : int
            number of recent days used for the long moving average

        """

        #now, we can call the constructor of the Strategy parent class using a "super"
        #this stores the market data inside self.data

        super().__init__(data)

        #store the selected moving-average periods 
        self.short_window = short_window #this will be the num of set values that the average calc will take into consideration
        self.long_window = long_window


    def generate_signals(self): #calculates the moving averages and creates different trading signals 
        #this will return a pandas.DataFrame that contains a copy of the original market data with the following:
        #Short_MA
        #Long_MA
        #Signal
        
        strategy_data = self.data.copy() # we need to create a copy so that we do not directly modify the original DataFrame 

        # now, we calculate the short moving average using closing prices
        strategy_data["Short_MA"] = (strategy_data["Close"].rolling(window=self.short_window).mean())

        #rolling = taking the closing prices in groups of 3 consecutive rows and calculate their average

        # same for the long moving average
        strategy_data["Long_MA"] = (strategy_data["Close"].rolling(window=self.long_window).mean())

        #now, lets create the "Signal" column with a default value of 0
        strategy_data["Signal"] = 0 # this creates a full column of 0s

        # IDEA - change the signal to 1 whenever the short moving average is greater than the long moving average
        # short moving avg > long moving average -- signal is now 1 

        strategy_data.loc[strategy_data["Short_MA"] > strategy_data["Long_MA"], "Signal"] = 1

        # this means find every row where Short_MA is greater than Long_MA, and place 1 in the Signal column

        # the general format for loc is - data.loc[condition, column] = value
        # therefore: 
        """
        DataFrame: strategy_data
        condition: Short_MA > Long_MA
        column to change: Signal
        new value: 1
        """
        return strategy_data