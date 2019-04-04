import pandas as pd
from ordered_set import OrderedSet
import glob

all_files = glob.glob('*.csv')

for filename in all_files:
        unique_dates = OrderedSet()
        df = pd.read_csv(filename)
        df['season'] = 0
        df['weekend'] = 0

        new = df['time'].str.split(" ", n = 1, expand = True)
        df['date'] = new[0]
        df['times'] = new[1]
        df.drop(columns = ['time'], inplace = True)

        # get the unique dates
        for date in df['date']:
                unique_dates.add(date)

        print(filename + ' ' + str(len(unique_dates)))
        # df.to_csv('new_data/' + filename)