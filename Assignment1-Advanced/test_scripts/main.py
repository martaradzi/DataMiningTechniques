import pandas as pd
from ordered_set import OrderedSet

unique_dates = OrderedSet()
df = pd.read_csv('AS14.01.csv')
df['day_number'] = 0

# get the unique dates
for date in df['date']:
    # do not include the empty rows in the ordered set
    # TODO: remove the empty rows
    if pd.notna(date):
        unique_dates.add(date)

for i, row in df.iterrows():
    if row.date in unique_dates:
        df.set_value(i, 'day_number', unique_dates.index(row.date))
        
    
print(df)
