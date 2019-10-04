'''
Do some research on other popular python packages and what the are used for. Feel free to import them
and play around a little.

'''

# work on them!

import requests
import numpy
import pandas as pd

print("Requests:", requests.__version__)
print("Numpy:", numpy.__version__)
print("Pandas:", pd.__version__)

pd.set_option('display.max_colums', 100)
pd.set_option('display.max_rows', 5000)

pd.read_excel("aging_example.xlsx")

