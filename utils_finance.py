# Basics
import numpy as np
import pandas as pd
import logging
import itertools

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly

# Additional imports
import plotly.graph_objs as go

def plot_candlestick(data, tick = ''):
    '''
    Plot the candlestick chart of a stock.

    Arguments:
        data (pd.DataFrame): contains the historical data of prices for [Open, Low, High, Close]
        tick (str): tick of the stock for the title of the plot.
    '''
    # Create the data object
    data = [
        go.Candlestick(x     = data.index,
                       open  = data['Open'],
                       close = data['Close'],
                       low   = data['Low'],
                       high  = data['High']
                       )
    ]

    # Create the layout object
    layout = {
        'title' : {'text' : '{} - Daily'.format(tick), 'x': 0.5, 'y': 0.9, 'font' : { 'size' : 30 }},
        'xaxis' : go.layout.XAxis(title = go.layout.xaxis.Title( text = "Time" ), rangeslider = { 'visible' : False }),
        'yaxis' : go.layout.YAxis(title = go.layout.yaxis.Title( text = "Price per share in $")),
        'width' : 800,
        'height' : 400
    }

    # Make the figure
    fig = go.Figure(data = data, layout = layout)
    fig.show()

def compute_returns(data, log = False):
    '''
    Compute the returns of a stock's price time-series.

    Arguments:
        data (pd.DataFrame): contains the historical data of prices for [Open, Low, High, Close]
        log (bool): indicate if computing simple or logarithmic returns
    
    Returns: 
        returns (pd.Series): contains the historical value of returns
    '''
    # Select the closing prices
    series = data['Close']

    # Compute the returns
    if log:
        series_lag = series.shift(1, fill_value = 0)
        returns = np.log(series_lag / series)
    else:
        returns = series.pct_change()
        returns[0] = 1
    
    return returns

def plot_cummulative_returns(data, tick = '', log = False, show = True):
    '''
    Compute and plot the cummulative returns of a stock's price time-series.

    Args:
        data (pd.DataFrame): contains the historical data of prices for [Open, Low, High, Close]
        tick (str): tick of the stock for the title of the plot.
        log (bool): indicate if computing simple or logarithmic returns
        show (bool): indicate if showing the plot or just saving it

    Returns:
        ax (plt.figure): figure object containing the plots
    '''
    # Compute the returns
    returns = compute_returns(data, log = log)

    # Compute the cummulative product
    returns = (returns + 1).cumprod()

    # Plot the figure
    ax = sns.lineplot(x = returns.index, y = returns)
    
    # Formatting
    ax.set_title('{} - Daily Cummulative Returns'.format(tick), weight = 'bold')
    ax.set_xlabel('')
    ax.set_ylabel('Cummulative returns')

    # Show if necessary
    if show:
        plt.show()
    else:
        return ax
