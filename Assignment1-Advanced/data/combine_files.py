import csv
import pandas as pd

variables= ['mood', 'circumplex.arousal', 'circumplex.valence', 'activity', 'screen', 'call', 'sms', 'appCat.builtin', 'appCat.communication', 'appCat.entertainment', 'appCat.finance', 'appCat.game', 'appCat.office','appCat.other', 'appCat.social', 'appCat.travel', 'appCat.unknown', 'appCat.utilities', 'appCat.weather', 'day_0', 'day_1', 'day_2', 'day_3', 'day_4', 'day_5', 'day_6']
patient = ['02','03','05','06','07','08','09','12','13','14','15','16','17','19','20','23','24','25','26','27','28','29','30','31','32','33']

f = "./summary/01_imputed.csv"

combined_csv = pd.read_csv(f)

for p in patient:
    filename = "./summary/" + p + "_imputed.csv"
    d = pd.read_csv(filename)
    combined_csv = pd.concat([combined_csv, d])

combined_csv.to_csv("./stats/combined_csv.csv", index=False, encoding='utf-8-sig')
