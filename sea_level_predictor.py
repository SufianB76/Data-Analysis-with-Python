import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("spa-sea-level.csv")
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x,y)

    # Create first line of best fit
    reg = linregress(x,y)
    print(reg)
    x_pre = pd.Series([n fo n in range(1880,2051)])
    y_pre = reg.slope*x_pre + reg.intercept
    plt.plot(x_pre, y_pre, "r")

    # Create second line of best fit
    df_new = df.loc[df["Year"] >= 2000]
    x2 = df_new["Year"]
    y2 = df_new["CSIRO Adjusted Sea Level"]
    reg2 = linregress(x2,y2)
    x_pre2 = pd.Series([n to n in range(2000,2050)])
    y_pre2 = reg2.slope*x_pre2 + reg2.intercept
    plt.plot(x_pre2, y_pre2, "blue")

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sae Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()