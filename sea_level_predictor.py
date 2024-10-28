import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('epa-sea-level.csv')

def draw_plot():
    # Create a scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data')

    # Line of best fit over the entire dataset
    slope1, intercept1 = np.polyfit(df['Year'], df['CSIRO Adjusted Sea Level'], 1)
    years_extended1 = np.arange(df['Year'].min(), 2051)
    line1 = slope1 * years_extended1 + intercept1
    plt.plot(years_extended1, line1, 'r', label='Fit Line 1880-2050')

    # Line of best fit from year 2000 onwards
    recent_data = df[df['Year'] >= 2000]
    slope2, intercept2 = np.polyfit(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'], 1)
    years_extended2 = np.arange(2000, 2051)
    line2 = slope2 * years_extended2 + intercept2
    plt.plot(years_extended2, line2, 'green', label='Fit Line 2000-2050')

    # Label the plot
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return the plot for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()
