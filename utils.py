# Basics
import numpy as np
import pandas as pd
import logging
import itertools

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

def create_logger(stream = True, file = True, file_name = 'logging.log'):
    '''
    Create a logger object for logging.

    Args: 
        stream: bool, flag indicating if we want a stream logger
        file: bool, flag indicating if we want to save the logs in a file
        file_name: string, name of the file in which we are saving the logs
    '''
    # Create the logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    if stream:
        # Set the format
        formatter_stream = logging.Formatter('%(asctime)s : %(levelname)s %(message)s')

        # Create a handler for showing the logs
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(formatter_stream)

        # Add the handlers to the logger
        logger.addHandler(stream_handler)
    
    if file:
        # Set the format
        formatter_file = logging.Formatter('%(asctime)s %(name)s %(lineno)d:%(levelname)s %(message)s')

        # Create a handler for saving the logs
        file_handler = logging.FileHandler(file_name, mode = 'w')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter_file)

        # Add the handlers to the logger
        logger.addHandler(file_handler)

    return logger

def plot_distributions(data, dict_labels = False, n_cols = 5, show = True):
    '''
    Plot the distribution of features in a dataset.
    
    Args:
        data: pd.DataFrame, dataframe containting the data
        n_cols: integer, number of cols of the plot
    
    Return:
        fig: plt.figure, figure object containing the plots
    '''
    # Define the layout of the plot
    n_rows = 1 + len(data.columns.tolist()) // n_cols

    # Instantiate the figure
    fig = plt.figure(figsize = (20, 5*n_rows))

    # Recursively add a subplot for each variable
    for i,var in enumerate(data.columns):

        # Add the subplot
        ax = fig.add_subplot(n_rows, n_cols, i + 1)
        
        # Plot feature distribution if numeric
        if data[var].dtype in ['int64','float64']:
            sns.distplot(data[var], bins = 20, kde = False)
            
        # Plot feature distribution if cateogorical
        else:
            sns.countplot(data[var])
            
            # Label the categories
            if dict_labels:
                ax.set_xticklabels(dict_labels[var].values(), rotation = 45)

        # Formatting
        ax.set_title(var + ' distribution')
        ax.set_xlabel(var)
        ax.set_ylabel('Frecuency')

    # Formatting    
    fig.tight_layout()

    # Show if necessary
    if show:
        plt.show()

    return fig