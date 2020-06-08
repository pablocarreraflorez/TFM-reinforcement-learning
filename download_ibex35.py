# Basics
import pandas as pd
import pandas_datareader as pdr
from datetime import datetime

# Select the stocks to download
tables = pd.read_html('https://en.wikipedia.org/wiki/IBEX_35')
stocks = tables[1].Ticker.values.tolist()
stocks = [x + '.MC' for x in stocks]

# Select the dates 
date_start = datetime(2020, 1, 1)
date_end   = datetime(2020, 1, 2)

# Import data from Yahoo Finance
df = pdr.get_data_yahoo(symbols = stocks, start = date_start, end = date_end)

# Stack the stocks
df = df.stack(level='Symbols')

# Delete annoying labels
df.columns = df.columns.get_level_values(0)
df.columns.name = None
df.index.name = None

# Rename columns
df.columns = ['Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']

# Reorder the columns
df = df[['Open', 'Low', 'Close', 'High', 'Volume']]

# Clean columns
df = df.reset_index()
df = df.drop('Date', axis = 1)
df['Symbols'] = [x[:-3] for x in df['Symbols']]

# Save the data
df.to_csv('data/IBEX35.csv')

# print(df.to_latex(index=False, float_format="{:0.3f}".format))