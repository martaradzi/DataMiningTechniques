import pandas as pd
import glob
import numpy as np
import sys
import matplotlib.pyplot as plt
plt.style.use('ggplot')

from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from math import sqrt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import TimeSeriesSplit

if len(sys.argv) != 2:
    print("usage: python3 create_table.py <filename>")
    exit(1)

df = pd.read_csv(sys.argv[1])

# transform data to be stationary
raw_values = df.values
diff_values = difference(raw_values, 1)

print(raw_values)
print(diff_values)