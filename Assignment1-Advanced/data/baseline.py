import pandas as pd
import glob
import numpy as np
import sys
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from math import sqrt

scaler = MinMaxScaler(feature_range=(-1, 1))

all_files = glob.glob('summary/*_imputed.csv')
# all_files = glob.glob('summary/*01_imputed.csv')
out = pd.DataFrame()

if len(sys.argv) != 2:
    print("usage: python3 create_table.py <day-range>")
    exit(1)

rolling_range = int(sys.argv[1])

for filename in all_files:
    df = pd.read_csv(filename)
    current_target = int(sys.argv[1])
    patient = int(filename[8:10])
    target_mood = []

    target_mood.append(None)

    # loop for target_moods to add to df
    for x in range(rolling_range-1, len(df)):
        target_mood.append(df.iloc[x][1])
        current_target += 1

    # need to shift the target moods down one
    target_mood.pop()

    v1 = df['mood']					
    data = { 'mood':v1, 'target_mood':target_mood }
														
    temp = pd.DataFrame(data)
    to_drop = []
    
    for x in range(0,rolling_range-1):
        to_drop.append(x)

    temp.drop(temp.index[[len(df)-1]], inplace = True)
    temp.drop(temp.index[to_drop], inplace = True)
    temp.drop(temp.index[(0)], inplace = True)
    variables_final = ['mood', 'target_mood']
    temp = temp[variables_final] # rearrange columns

    out = pd.concat([out, temp], sort = False)

scaled = scaler.fit_transform(np.array(out, dtype = float))
out = pd.DataFrame(scaled)
out.columns = variables_final

out.to_csv('lstm_benchmark.csv', index = False)

x_test = out['mood']	
y_test = out['target_mood']

rmse = sqrt(mean_squared_error(x_test, y_test))
print('lstm')
print(sqrt(x_test.mean()))
print(sqrt(y_test.mean()))
print(rmse)
print()

print('random forest')
rmape = sqrt(mean_absolute_error(x_test, y_test))
print(rmape)
