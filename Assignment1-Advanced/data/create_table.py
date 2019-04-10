import pandas as pd
import glob
import numpy as np
import sys

all_files = glob.glob('summary/*01_imputed.csv')

if len(sys.argv) != 2:
    print("usage: python3 create_table.py <day-range>")
    exit(1)

rolling_range = int(sys.argv[1])
current_target = int(sys.argv[1])

column_names = ['mood', 'circumplex.arousal', 'circumplex.valence', 'activity', 'screen', 'call', 'sms', 'appCat.builtin', 'appCat.communication', 'appCat.entertainment', 'appCat.office','appCat.other', 'appCat.social', 'appCat.travel', 'appCat.unknown', 'appCat.utilities', 'target_mood']

for filename in all_files:
    df = pd.read_csv(filename)
    df['time'] = pd.to_datetime(df['time'])

    patient_number = filename[8:10]
    patient = 'Patient' + patient_number
    period = []
    target_mood = []

    for x in range(0, rolling_range-1):
        target_mood.append(None)
        period.append(None)

    # loop for target_moods and time-periods to add to df
    for x in range(rolling_range-1, len(df)):
        target_mood.append(df.iloc[x][1])
        period.append('t = ' + str(current_target-rolling_range) + '-' + str(current_target))
        current_target += 1

    target_mood.pop(0)
    target_mood.append(None)

    v1 = df['mood'].rolling(rolling_range).mean()
    v2 = df['circumplex.arousal'].rolling(rolling_range).mean()
    v3 = df['circumplex.valence'].rolling(rolling_range).mean()
    v4 = df['activity'].rolling(rolling_range).mean()
    v5 = df['screen'].rolling(rolling_range).sum()
    v6 = df['call'].rolling(rolling_range).sum()
    v7 = df['sms'].rolling(rolling_range).sum()
    v8 = df['appCat.builtin'].rolling(rolling_range).sum()
    v9 = df['appCat.communication'].rolling(rolling_range).sum()
    v10 = df['appCat.entertainment'].rolling(rolling_range).sum()
    v11 = df['appCat.office'].rolling(rolling_range).sum()
    v12 = df['appCat.other'].rolling(rolling_range).sum()
    v13 = df['appCat.social'].rolling(rolling_range).sum()
    v14 = df['appCat.travel'].rolling(rolling_range).sum()
    v15 = df['appCat.unknown'].rolling(rolling_range).sum()
    v16 = df['appCat.utilities'].rolling(rolling_range).sum()

    data = {'patientno':patient, 'period': period, 'mood':v1, 'circumplex.arousal':v2, 'circumplex.valence':v3, 'activity':v4, 'screen':v5, 
        'call':v6, 'sms':v7, 'appCat.builtin':v8, 'appCat.communication':v9, 'appCat.entertainment':v10, 'appCat.office':v11, 
        'appCat.other':v12, 'appCat.social':v13, 'appCat.travel':v14, 'appCat.unknown':v15, 'appCat.utilities':v16, 'target_mood':target_mood}
														
    out = pd.DataFrame(data)

    to_drop = []
    for x in range(0,rolling_range-1):
        to_drop.append(x)

    out.drop(out.index[[len(df)-1]], inplace=True)
    out.drop(out.index[to_drop], inplace=True)

    print(out)
