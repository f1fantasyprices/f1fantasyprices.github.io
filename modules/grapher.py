import matplotlib.pyplot as plt
import datetime
import numpy as np
import pandas as pd
import os



df = pd.read_excel( os.path.dirname(os.path.abspath(__file__)) + '/data/resources/driver_prices.xlsx')

print(df)