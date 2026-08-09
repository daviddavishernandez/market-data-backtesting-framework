from utils.data_loader import DataLoader
from utils.validator import DataValidator
from strategies.moving_average import MovingAverageStrategy


# Load the market data
loader = DataLoader("data/apple.csv")
market_data = loader.load_data()


# Validate the market data
validator = DataValidator(market_data)
validator.validate()


# Create the strategy
strategy = MovingAverageStrategy(
    market_data,
    short_window=3,
    long_window=5
)


# Generate signals
strategy_data = strategy.generate_signals()


print("Market data loaded and validated successfully.")

print(
    strategy_data[
        ["Date", "Close", "Short_MA", "Long_MA", "Signal"]
    ]
)