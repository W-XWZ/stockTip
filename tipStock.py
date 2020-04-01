
import realtime_sina as sina
import tkinter as tk
from  tkinter import ttk
import time
import pandas as pd


def fx_out():
    fx_pd=pd.read_csv('W:\\python-work\\realtime_stock-master\\fx1.csv',sep=',',converters={'code':str})
    new = sina.fx(fx_pd['code'])
    new = pd.merge(new, fx_pd, how='inner', on=None)
    new['nchg'] = ((pd.to_numeric(new['price']) - pd.to_numeric(new['pre_close'])) * 10000).astype(int)
    return new[['name', 'price', 'nchg']]

print(fx_out())