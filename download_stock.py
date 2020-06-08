# Basics
import pandas as pd
import pandas_datareader as pdr
from datetime import datetime

# Select the stocks to download
stock = ['AAPL']

# Select the dates 
date_start = datetime(2000, 1, 1)
date_end   = datetime(2019, 12, 31)

# Import data from Yahoo Finance
df = pdr.get_data_yahoo(symbols = stock, start = date_start, end = date_end)

# Delete annoying labels
df.columns = df.columns.get_level_values(1)
df.columns.name = None
df.index.name = None

# Rename columns
df.columns = ['Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']

# Reorder the columns
df = df[['Open', 'Low', 'Close', 'High', 'Volume']]

# Save the data
df.to_csv('data/{}_2000_2019.csv'.format(stock[0]))