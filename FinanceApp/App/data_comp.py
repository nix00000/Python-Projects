import pandas as pd
import pandas_datareader.data as web
import datetime
import sqlite3
# import requests
# import csv
# from difflib import SequenceMatcher


class Data:
    def company(self,a):
        # SequenceMatcher(None, a, b).ratio()
        conn = sqlite3.connect('comp.db')
        c = conn.cursor()
        c.execute('SELECT * FROM companies WHERE name LIKE ? LIMIT 4',("%"+ a + "%",))
        data = c.fetchall()
        if data:
            return data
        else:
            return -1

    def companyFinal(self,a):
        # SequenceMatcher(None, a, b).ratio()
        conn = sqlite3.connect('comp.db')
        c = conn.cursor()
        c.execute('SELECT name FROM companies WHERE inds LIKE ?',("%"+ a + "%",))
        data = c.fetchone()
        if data:
            return data[0]
        else:
            return -1
    def getData(self,ind):
        start = datetime.datetime(2019, 1, 1)
        end = datetime.datetime(2021, 1, 1)

        try:
            datas = web.DataReader(ind, "yahoo", start, end)
        except:
            return -1

        return(datas)



