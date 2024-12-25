import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
     #column "NOAA Adjusted Sea Level" does not have data
    df = df.drop(columns='NOAA Adjusted Sea Level')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,6))
    ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    result = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    y_intercept = result.intercept
    slope = result.slope
    x = np.arange(1880, 2051, 1)
    
    ax.plot(x, y_intercept + slope * x, 
        color='red', label='Regression line from year 1880')

    # Create second line of best fit
    df_2000 = df.loc[df['Year'] >= 2000]
    result_2000 = linregress(x=df_2000['Year'], y=df_2000['CSIRO Adjusted Sea Level'])
    y_intercept_2000 = result_2000.intercept
    slope_2000 = result_2000.slope
    x_2000 = np.arange(2000, 2051, 1)

    ax.plot(x_2000, y_intercept_2000 + slope_2000 * x_2000, 
        color='green', label='Regression line from year 2000')
    
    # Add labels and title
    ax.legend()
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()