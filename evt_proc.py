# -*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime
from datetime import timedelta

HEADER = ['INFO', 'DATE', 'ORIG', 'ID', 'CAT', 'DESC']
ESSENCE = ['DATE', 'ID']

raw_data = pd.read_csv('static/rhythm.csv', names=HEADER, skiprows=1, encoding='utf-8')
df = pd.DataFrame(raw_data, columns=ESSENCE)
df = df.replace(['오전', '오후'], ['AM', 'PM'], regex=True)
df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%d %p %I:%M:%S')

#print(df.query('DATE > datetime.today().date()'))
today_rhythm = df[df['DATE'] > datetime.today().date() - timedelta(days=1)]

for i, row in today_rhythm.iterrows():
    print(row['DATE'], row['ID'])
