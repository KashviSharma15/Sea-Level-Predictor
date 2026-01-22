import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 5))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Line of best fit (all data)
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred = np.arange(df["Year"].min(), 2051)
    y_pred = res.intercept + res.slope * x_pred
    plt.plot(x_pred, y_pred, color="red")

    # Line of best fit (from year 2000)
    df_2000 = df[df["Year"] >= 2000]
    res_2000 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    x_pred_2000 = np.arange(2000, 2051)
    y_pred_2000 = res_2000.intercept + res_2000.slope * x_pred_2000
    plt.plot(x_pred_2000, y_pred_2000, color="green")

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save and return axis
    plt.savefig("sea_level_plot.png")
    return plt.gca()
