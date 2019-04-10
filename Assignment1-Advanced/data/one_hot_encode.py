import pandas as pd
from ordered_set import OrderedSet
import glob
import numpy as np

all_files = glob.glob('*.csv')

for filename in all_files:
        unique_dates = OrderedSet()
        df = pd.read_csv(filename)

        df['time'] = pd.to_datetime(df['time'])
        df['dayofweek'] = df['time'].dt.dayofweek

        one_hot = pd.get_dummies(df['dayofweek'], prefix = 'day')
        df = df.drop('dayofweek', axis=1)
        df = df.join(one_hot)

        df.to_csv(filename)