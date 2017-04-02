# -*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime
from datetime import timedelta

ESSENCE = ['EventID', 'TimeWritten']

class EventParam:
    def __init__(self):
        raw_data = pd.read_csv('static/rhythm.csv', header=1, encoding='utf-8')
        self.df = pd.DataFrame(raw_data, columns=ESSENCE)
        self.df = self.df.replace(['오전', '오후'], ['AM', 'PM'], regex=True)
        self.df['TimeWritten'] = pd.to_datetime(self.df['TimeWritten'], format='%Y-%m-%d %p %I:%M:%S')

    def today_rhythm(self):
        #print(df.query('DATE > datetime.today().date()'))
        return self.df[self.df['TimeWritten'] > datetime.today().date()]

    def today_print(self):
        for i, row in self.today_rhythm().iterrows():
            print(row['TimeWritten'], row['EventID'])

a = EventParam()
a.today_print()