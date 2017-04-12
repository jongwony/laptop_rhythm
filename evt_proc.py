# -*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime
from datetime import timedelta

ESSENCE = ['EventID', 'TimeWritten']

class EventProc:
    def __init__(self):
        raw_data = pd.read_csv('static/logon_rhythm.csv', header=1, encoding='utf-8')
        self.df = pd.DataFrame(raw_data, columns=ESSENCE)
        self.df = self.df.replace(['오전', '오후'], ['AM', 'PM'], regex=True)
        self.df['TimeWritten'] = pd.to_datetime(self.df['TimeWritten'], format='%Y-%m-%d %p %I:%M:%S')

        # delta pin
        self.pin = None

        # { delta: ###, flag: active/deactive }
        self.result = dict()

    def today_rhythm(self):
        """
        today rhythm - each dataframe row to donut chart
        output: generator
        """
        now = datetime.today()
        now_date = now - datetime(now.year, now.month, now.day)
        today = now - now_date
        checkpoint = today

        # select query pin
        evt_today = self.df[['TimeWritten', 'EventID']]
        evt_today = evt_today[evt_today['TimeWritten'] > today]

        # loop reverse index in dataframe
        for _, element in evt_today.iloc[::-1].iterrows():
            # type: datetime.datetime
            self.pin = element['TimeWritten']
            # type: int
            evt_id = element['EventID']

            # Refresh
            if evt_id in [7001, 506]:
                self.result = self.calc_delta(self.pin, checkpoint, 'deactive')


            if evt_id in [7002, 507]:
                self.result = self.calc_delta(self.pin, checkpoint, 'active')

            checkpoint = self.pin
            yield self.result

        # current time
        yield self.calc_delta(now, checkpoint, 'active')

        # remaining time
        tommorrow = today + timedelta(days=1)
        yield self.calc_delta(tommorrow, now, 'remain')

    def calc_delta(self, after, before, flag):
        """
        Calculation delta time
        output: `self.result` dictionary
        """
        delta = after - before
        return {
            'delta': round(delta.total_seconds() / 60, 0),
            'flag': flag
        }
