import pandas as pd

from strategies.moving_average import MovingAverageStrategy

def test_moving_average_columns_are_created():
#checks that all of the moving-average strategy creates the columns we expect

    #we can now create a small artificial dataset
    data = pd.DataFrame({"Close": [100, 110, 120, 130, 140]})

    strategy = MovingAverageStrategy(data, short_window=2, long_window=3) #this will be our strategy 

    results = strategy.generate_signals() #this will generate our signals 

    #check that the required columns exist:
    assert "Short_MA" in results.columns
    assert "Long_MA" in results.columns
    assert "Signal" in results.columns


def test_moving_average_values_are_correct(): #checks that the moving averages are calculated correctly
    #we create a small data set where we know what the moving averages should be 
    data = pd.DataFrame({"Close": [100, 110, 120, 130, 140]}) 

    #create the strategy again with the results included
    strategy = MovingAverageStrategy(data, short_window=2, long_window=3)
    results = strategy.generate_signals()

    #the short moving average on the third row should be the following: (110 + 120) / 2 = 115
    assert results.loc[2, "Short_MA"] == 115 
    #results.loc[2, "Short_MA"] == 115 means: give me the value in row 2 of the Short_MA column
    #the assert, we use to verify that our expectation should give us 115

    #the long moving average on the third row should be: # (100 + 110 + 120) / 3 = 110
    assert results.loc[2, "Long_MA"] == 110

def test_buy_signal_is_generated():
#checks that the strategy generates a buy signal when the short moving average is above the long moving average.
    data = pd.DataFrame({"Close": [100, 110, 120, 130, 140]})
    strategy = MovingAverageStrategy(data, short_window=2, long_window=3)
    results = strategy.generate_signals()

    # at this point: Short MA = 115 and Long MA = 110, therefore Signal = 1 (since Short > Long)
    assert results.loc[2, "Signal"] == 1

