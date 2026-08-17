from utils.data_loader import DataLoader
from utils.validator import DataValidator
from strategies.moving_average import MovingAverageStrategy
from backtester.backtester import Backtester
from backtester.performance import PerformanceAnalyzer


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

# ---------------------------------------------------
# ANALYZE PERFORMANCE
# ---------------------------------------------------

performance = PerformanceAnalyzer(
    results,
    initial_cash=10000
)

final_value = performance.get_final_value()
total_profit = performance.get_total_profit()
total_return = performance.get_total_return()
buy_hold_return = performance.get_buy_and_hold_return()
max_drawdown = performance.get_max_drawdown()

print("\nBACKTEST RESULTS")
print("----------------------------")

print("Final portfolio value:", round(final_value, 2))
print("Total profit:", round(total_profit, 2))
print("Strategy return:", round(total_return, 2), "%")
print("Buy and hold return:", round(buy_hold_return, 2), "%")
print("Maximum drawdown:", round(max_drawdown, 2), "%")

