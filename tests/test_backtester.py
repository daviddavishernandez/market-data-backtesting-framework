# goal - Verify that our backtester uses yesterday's signal to trade at today's opening price, without using future information

import pandas as pd
from backtester.backtester import Backtester

def test_signals_are_executed_next_day():
# Checks that today's trading signal is executed on the following trading day.

    # Create four days of artificial market data.
    data = pd.DataFrame({"Open": [100, 110, 130, 150],
        "Close": [100, 120, 140, 160],"Signal": [1, 1, 0, 0]})

    #create and run the backtester
    backtester = Backtester(data, initial_cash=1000)
    results = backtester.run()

    #monday's buy signal must NOT execute on Monday
    assert results.loc[0, "Execution_Signal"] == 0

    #monday's buy signal executes on Tuesday
    assert results.loc[1, "Execution_Signal"] == 1

    #wednesday's sell signal executes on Thursday
    assert results.loc[3, "Execution_Signal"] == 0


def test_buy_at_next_day_open():
# Checks that the backtester buys shares using the next trading day's opening price.

    data = pd.DataFrame({"Open": [100, 110],"Close": [100, 120],"Signal": [1, 1]})

    #start with $1,000
    backtester = Backtester(data, initial_cash=1000)
    results = backtester.run()

    # no shares should be purchased on the first day
    assert results.loc[0, "Portfolio_Value"] == 1000

    # on the second day:
    # buy 9 shares at $110 = $990 spent.
    # remaining cash = $10.
    # at the close:
    # 9 shares * $120 + $10 = $1,090.
    assert results.loc[1, "Portfolio_Value"] == 1090

    #confirm that we own exactly 9 shares
    assert backtester.portfolio.shares == 9

    #confirm that we have $10 remaining
    assert backtester.portfolio.cash == 10


def test_sell_at_next_day_open():
# Checks that the backtester sells shares usingthe opening price of the following trading day.

    data = pd.DataFrame({"Open": [100, 110, 130, 150],"Close": [100, 120, 140, 160],"Signal": [1, 1, 0, 0]})

    #start with $1,000
    backtester = Backtester(data, initial_cash=1000)
    results = backtester.run()

    #monday: no trade
    assert results.loc[0, "Portfolio_Value"] == 1000

    #tuesday: buy 9 shares at $110.
    #end of day value = $1,090.
    assert results.loc[1, "Portfolio_Value"] == 1090

    # wednesday: keep holding 9 shares
    # end of day value = 9 * $140 + $10 = $1,270
    assert results.loc[2, "Portfolio_Value"] == 1270

    # thursday: sell 9 shares at the opening price of $150
    # final cash = 9 * $150 + $10 = $1,360
    assert results.loc[3, "Portfolio_Value"] == 1360

    # after selling, we should own no shares
    assert backtester.portfolio.shares == 0

    # all our money should now be held as cash
    assert backtester.portfolio.cash == 1360