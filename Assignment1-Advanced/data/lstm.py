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
# from math import sqrt
from sklearn.model_selection import train_test_split
# from sklearn.model_selection import TimeSeriesSplit

if len(sys.argv) != 2:
    print("usage: python3 create_table.py <filename>")
    exit(1)

df = pd.read_csv(sys.argv[1])
df.fillna(0, inplace=True)

# print(df.head())

target = np.array(df['target_mood'], dtype = float)
del df['target_mood']
del df['patientno']
del df['period']
data = np.array(df, dtype = float)

print(data[0])