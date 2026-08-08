# the responsibility of this module is to see whether the market data is valid before the backtest uses it

# the class made before named 'DataLoader' only reads the file
# now we create another one called 'DataValidator' that checks whether the data makes sense 
"""
things that this class will check: 
- are all required columns present 
- any missing values?
- duplicate dates 
- any prices negative? we would need to modify these 
- is the HIGH price actually the highest among the other daily prices? 
- is the LOW price actually lower that the other daily prices? 

"""

class DataValidator: 
    def __init__(self, data):
        # data - pd.DataFrame or pandas.DataFrame which is the historical market data loaded from the csv file
        self.data = data 

    def validate(self):
        # runs every validation check
        # if a problem is found, raise ValueError
        # if no problem is found, returns True

        #to do this, we will have to incorporate all of the following functions: 

        self._check_required_columns()
        self._check_missing_values()
        self._check_duplicate_dates()
        self._check_negative_values()
        self._check_high_prices()
        self._check_low_prices()

        return True

    #lets define all of the previous functions

    def _check_required_columns(self):
        # checks that the dataframe contains every column that we need

        required_columns = ["Date", "Open", "High", "Low", "Close", "Volume"]

        for column in required_columns: 
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    
    def _check_missing_values(self):
        #checks if any cell contains a missing value from the data 

        if self.data.isnull().values.any(): #if any value in the whole DataFrame is missing, stop the program
            raise ValueError("The market data contains missing values")
        
        # self.data.isnull() -- this checks every cell and produces true where a value is missing
        # .values.any() -- basically asks is there at least one missing value anywhere?
        # .any() checks whether at least one result is True -- really important FOR ALL THE FOLLOWING FUNCTIONS! 

    def _check_duplicate_dates(self):
        #checks whether the same date appears more than once
        if self.data["Date"].duplicated().any():
            raise ValueError("The market data contains duplicate dates")

    def _check_negative_values(self):
        #checks that prices and trading volume are not negative.
        numeric_columns = ["Open", "High", "Low", "Close", "Volume"]

        for column in numeric_columns:
            if (self.data[column] < 0).any():
                raise ValueError(f"The column '{column}' contains negative values.")

    def _check_high_prices(self):
        #checks that the High price is not below Open, Low, or Close
        invalid_high = ((self.data["High"] < self.data["Open"])
            | (self.data["High"] < self.data["Low"])
            | (self.data["High"] < self.data["Close"]))

        if invalid_high.any():
            raise ValueError("At least one High price is inconsistent")

    def _check_low_prices(self):
        # checks that the Low price is not above Open, High, or Close 
        invalid_low = ((self.data["Low"] > self.data["Open"])
            | (self.data["Low"] > self.data["High"])
            | (self.data["Low"] > self.data["Close"]))

        if invalid_low.any():
            raise ValueError("At least one Low price is inconsistent.")

        