from utils.data_loader import DataLoader
from utils.validator import DataValidator
from strategies.moving_average import MovingAverageStrategy
from backtester.backtester import Backtester


# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

loader = DataLoader("data/apple.csv")
market_data = loader.load_data()


# ---------------------------------------------------
# VALIDATE DATA
# ---------------------------------------------------

validator = DataValidator(market_data)
validator.validate()


# ---------------------------------------------------
# CREATE STRATEGY
# ---------------------------------------------------

strategy = MovingAverageStrategy(
    market_data,
    short_window=3,
    long_window=5
)

strategy_data = strategy.generate_signals()


# ---------------------------------------------------
# RUN BACKTEST
# ---------------------------------------------------

backtester = Backtester(
    strategy_data,
    initial_cash=10000
)

results = backtester.run()


# ---------------------------------------------------
# DISPLAY RESULTS
# ---------------------------------------------------

print(
    results[
        [
            "Date",
            "Close",
            "Signal",
            "Portfolio_Value"
        ]
    ]
)
