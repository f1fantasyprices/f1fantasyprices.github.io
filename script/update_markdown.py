import os
import pandas as pd
from script.modules.helpers import markdown_table
import datetime

wdir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(wdir)

ddf = "/data/resources/driver_prices.xlsx"
cdf = "/data/resources/constructor_prices.xlsx"


## This script updates the webpage with new graphs and driver price tables

mytext = f"""

![driver_prices](./script/modules/data/resources/driver_prices.png)

{markdown_table(ddf, drivers=True)}

![constructor](./script/modules/data/resources/constructor_prices.png)

{markdown_table(cdf, drivers = False)}

Last updated at {datetime.datetime.now()}

"""




f = open(root_dir + '\index.md', 'w')

f.write(mytext)
f.close()
