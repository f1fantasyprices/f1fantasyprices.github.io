import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import matplotlib
from script.modules.xpaths import get_driver_colors, get_team_colors, get_abrreviated_names
from matplotlib.dates import DateFormatter


sns.set(style="whitegrid")
wdir = os.path.dirname(os.path.abspath(__file__))

filepath_team = os.path.dirname(os.path.abspath(__file__)) + "/data/resources/constructor_prices.xlsx"
filepath = os.path.dirname(os.path.abspath(__file__)) + "/data/resources/driver_prices.xlsx"






def plot_prices(filepath, drivers=True):

    df = pd.read_excel(filepath)
    #print(df)

    df['Timestamp'] = matplotlib.dates.date2num(df['Timestamp'])
    df.set_index('Timestamp', inplace=True)



    driver_colors = get_driver_colors()
    team_colors = get_team_colors()
    abb = get_abrreviated_names()

    fig, ax = plt.subplots(nrows=1, ncols=1)
    #ax = plt.gca()
    date_form = DateFormatter("%m-%d %HH")
    ax.xaxis.set_major_formatter(date_form)

    #size parameters




    if drivers:

        df = df[["V. Bottas",
                 "L. Hamilton",
                 "S. Vettel",
                 "C. Leclerc",
                 "C. Sainz",
                 "L. Norris",
                 "D. Ricciardo",
                 "E. Ocon",
                 "R. Grosjean",
                 "K. Magnussen",
                 "N. Latifi",
                 "G. Russell",
                 "M. Verstappen",
                 "A. Albon",
                 "A. Giovinazzi",
                 "K. Räikkönen",
                 "D. Kvyat",
                 "P. Gasly",
                 "S. Perez",
                 "L. Stroll"
                 ]]

        z = 0
        for column in df:

            if z % 2 == 0:
                df.plot(kind='line',  y=column, color=driver_colors[column], ax=ax)
                z += 1
            else:
                df.plot(kind='line',  y=column, color=driver_colors[column], ax=ax, linestyle="--")
                z += 1
        plt.gca().legend_.remove()
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

        ax.set_title("Driver Prices", fontsize=22)
        ax.set_ylabel("Price ($ Millions)", fontsize=18)
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        fig.set_figheight(8)
        fig.set_figwidth(14)
        fig.savefig(wdir + '/data/resources/driver_prices.png')
        print("New driver graph created")


    else:
        for column in df:
            df.plot(kind='line', y=column, color=team_colors[column], ax=ax)

        plt.gca().legend_.remove()
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

        ax.set_title("Constructor Prices", fontsize=22)
        ax.set_ylabel("Price ($ Millions)", fontsize=18)
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        fig.set_figheight(8)
        fig.set_figwidth(14)
        fig.savefig(wdir + '/data/resources/constructor_prices.png')
        print("New constructor graph created")



