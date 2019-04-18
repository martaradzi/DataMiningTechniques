import pandas as pd
import glob
import numpy as np
import sys
import matplotlib.pyplot as plt

all_files = glob.glob('summary/*_imputed.csv')
# all_files = glob.glob('summary/*01_imputed.csv')
out = pd.DataFrame()

if len(sys.argv) != 2:
    print("usage: python3 create_table.py <day-range>")
    exit(1)

rolling_range = int(sys.argv[1])

variables = ['circumplex.arousal', 'circumplex.valence', 'activity', 'screen', 'call', 'sms', 'appCat.builtin', 'appCat.communication', 'appCat.entertainment', 
    'appCat.finance', 'appCat.game', 'appCat.office','appCat.other', 'appCat.social', 'appCat.travel', 'appCat.unknown', 'appCat.utilities', 'appCat.weather']

for filename in all_files:
    df = pd.read_csv(filename)

    current_target = int(sys.argv[1])
    patient = int(filename[8:10])
    period = []
    target_mood = []

    for x in range(0, rolling_range-1):
        target_mood.append(None)
        period.append(None)

    # loop for target_moods to add to df
    for x in range(rolling_range-1, len(df)):
        target_mood.append(df.iloc[x][1])
        current_target += 1

    # need to shift the target moods up one
    target_mood.pop(0)
    target_mood.append(None)

    v1 = df['mood']
    v2 = df['circumplex.arousal']
    v3 = df['circumplex.valence']
    v4 = df['activity']
    v5 = df['screen']
    v6 = df['call']
    v7 = df['sms']
    v8 = df['appCat.builtin']
    v9 = df['appCat.communication']
    v10 = df['appCat.entertainment']
    v11 = df['appCat.office']
    v12 = df['appCat.other']
    v13 = df['appCat.social']
    v14 = df['appCat.travel']
    v15 = df['appCat.unknown']
    v16 = df['appCat.utilities']
    v17 = df['appCat.finance']
    v18 = df['appCat.game']
    v19 = df['appCat.weather']
    
    # one-hot day of week
    v20 = df['day_0']
    v21 = df['day_1']
    v22 = df['day_2']
    v23 = df['day_3']
    v24 = df['day_4']
    v25 = df['day_5']
    v26 = df['day_6']

    # one-hot patient number
    # v27 = []
    # for x in range(1, 33):
    #     if x == patient:
    #         patientno = df['p'+str(patient)]

    patientno = 'p' + str(patient)
    							
    data = { patientno:1, 'mood':v1, 'circumplex.arousal':v2, 'circumplex.valence':v3, 'activity':v4, 'screen':v5, 
        'call':v6, 'sms':v7, 'appCat.builtin':v8, 'appCat.communication':v9, 'appCat.entertainment':v10, 'appCat.office':v11, 
        'appCat.other':v12, 'appCat.social':v13, 'appCat.travel':v14, 'appCat.unknown':v15, 'appCat.utilities':v16, 
        'appCat.finance':v17, 'appCat.game':v18, 'appCat.weather':v19, 'mon':v20, 'tue':v21, 'wed':v22, 'thu':v23, 'fri':v24, 'sat':v25, 'sun':v26, 'target_mood':target_mood }
														
    temp = pd.DataFrame(data)
    to_drop = []
    
    for x in range(0,rolling_range-1):
        to_drop.append(x)

    temp.drop(temp.index[[len(df)-1]], inplace = True)
    temp.drop(temp.index[to_drop], inplace = True)
    
    # for variable in variables:
    #     if variable in temp.columns:
    #         meanVal = temp[variable].mean()
    #         stdVal = temp[variable].std()
    #         temp[variable] = (temp[variable] - meanVal) / stdVal

    variables_final = [patientno, 'mood', 'circumplex.arousal', 'circumplex.valence', 'activity', 'screen', 'call', 'sms', 
        'appCat.builtin', 'appCat.communication', 'appCat.entertainment', 'appCat.finance', 'appCat.game', 'appCat.office','appCat.other', 
        'appCat.social', 'appCat.travel', 'appCat.unknown', 'appCat.utilities', 'appCat.weather', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'target_mood']

    temp = temp[variables_final] # rearrange columns
    # temp.to_csv('patient_data/' + sys.argv[1] + '_p' + str(patient) + '.csv', index=False)
    out = pd.concat([out, temp], sort = False)

    # plt.subplot(2, 1, 1)
    # plt.plot(v1)
    # plt.subplot(2, 1, 2)
    # plt.plot(v5)
    # plt.show()

out.to_csv('LSTM_window_' + sys.argv[1] + '.csv', index = False)
# out.to_csv('tableX_' + sys.argv[1] + '.csv', index=False)

# corr = out.corr()
# plt.matshow(corr)
# plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical')
# plt.yticks(range(len(corr.columns)), corr.columns)
# plt.savefig('corr_' + sys.argv[1] + '.png')
# plt.show()
