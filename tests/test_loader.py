from utils.data_loader import DataLoader

def test_data_loader_returns_data():
#tests that the DataLoader succesfully loads the Apple CSV file. 

    #lets create the DataLoader using the CSV file:
    loader = DataLoader("data/apple.csv")

    #load the data 
    data = loader.load_data()

    #check that we received at least one row
    assert len(data)>0


def test_data_loader_contains_required_columns():
# checks that the loaded data contains the columns required by our backtesting framework
    
    #create the DataLoader 
    loader = DataLoader("data/apple.csv") #MIGHT NOT WORK, depends on the adress on my terminal !!

    #load the data 
    data = loader.load_data()

    required_columns = ["Date","Open","High","Low","Close","Volume"] #expected columns to have 

    for column in required_columns:
        assert column in data.columns


#when we run the tests within the terminal, we need to make sure that we get something like:  tests/test_loader.py ..
# the two dots means that both of the tests have passed