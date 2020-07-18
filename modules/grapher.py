import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import matplotlib
from modules.xpaths import get_driver_colors, get_team_colors

from labellines import *

sns.set(style="whitegrid")


filepath = os.path.dirname(os.path.abspath(__file__)) + "/data/resources/driver_prices.xlsx"






def plot_prices(filepath):

    df = pd.read_excel(filepath)
    print(df)
    df.set_index('Timestamp', inplace=True)
    filled_markers = ('o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X', 'p', 'l', 'm', 'n', 'q', 'r')

    driver_colors = get_driver_colors()
    team_colors = get_team_colors()

    df = df.sort_values(df.last_valid_index(), axis=1, ascending=False)

    ax = plt.gca()



    for column in df:
        previous_driver = 0
        if column != 'Timestamp':
            extra_offset = False
            if df[column][-1] - previous_driver < 1:


            df.plot(kind='line', y=column, color=driver_colors[column], ax=ax)
            ax.annotate(xy=(df.index[-1], df[column][-1]), xytext=(z, 0), textcoords='offset points', va='center', s=f"{column}  {df[column][-1]}M")
            previous_driver = df[column][-1]












    plt.show()

plot_prices(filepath)