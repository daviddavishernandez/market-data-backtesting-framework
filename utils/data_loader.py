

import pandas as pd #just as a nickname to be able to use the shortcut 'pd' in our code

class DataLoader:
    #the purpose of this class is to be able to load historical market data from a CSV file
    """the objectives of this class (with its functions): 
    - read the csv file 
    - convert the date column into actual real dates for python to recognize 
    - sort all of the data cronologically to have everything organized 
    - return a clear dataframe 
    """

    def __init__(self, file_path): 
        #file path will be a string telling us the location of the csv file
        self.file_path = file_path #whole class can use it.

    def load_data(self):
        #reads the csv file and returns a pandas DataFrame (like a table)
        data = pd.read_csv(self.file_path)
        data["Date"] = pd.to_datetime(data["Date"])

        data = data.sort_values("Date") #sorts from oldest to newest
        data = data.reset_index(drop=True) #reset the row numbers after being altered

        return data #should give us the finished dataframe  


