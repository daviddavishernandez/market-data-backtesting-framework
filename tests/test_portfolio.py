from backtester.portfolio import Portfolio

# test 1: initial portfolio 

def test_initial_portfolio():
    #Checks that a new portfolio starts with the correctamount of cash and zero shares

    #create a portfolio with $10,000
    portfolio = Portfolio(initial_cash=10000)

    #check that the starting cash is correct
    assert portfolio.cash == 10000

    #check that we do not own any shares yet
    assert portfolio.shares == 0

#test 2: buying shares 

def test_buy_shares():
    #Checks that buying shares correctly updates the cash and the number of shares owned

    #create a portfolio with $10,000.
    portfolio = Portfolio(initial_cash=10000)

    # buy Apple shares at $250 per share
    portfolio.buy(250)

    # $10,000 / $250 = 40 shares
    assert portfolio.shares == 40

    # we spent all our available cash
    assert portfolio.cash == 0


#test 3: alculating the portfolio value 
def test_portfolio_value():
    #Checks that the portfolio calculates its total value correctly when the share price changes

    #create our starting portfolio
    portfolio = Portfolio(initial_cash=10000)

    # buy 40 shares at $250
    portfolio.buy(250)

    # apple now rises to $275
    # our 40 shares are now worth $11,000
    total_value = portfolio.get_total_value(275)

    #check that the calculated value is correct
    assert total_value == 11000


# test 4: selling shares 

def test_sell_shares():
#checks that selling shares correctly updates the available cash and number of shares

    # create our starting portfolio
    portfolio = Portfolio(initial_cash=10000)

    #buy 40 shares at $250
    portfolio.buy(250)

    #sell all 40 shares at $275
    portfolio.sell(275)

    #we should now have $11,000 in cash
    assert portfolio.cash == 11000

    #all shares have been sold
    assert portfolio.shares == 0