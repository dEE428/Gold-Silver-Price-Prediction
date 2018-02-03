

import pandas as pd, sys
from dateutil.parser import parse

if len(sys.argv) <4:
    print 'Syntax: python getCommodityPrice.py 2017-05-01 2017-05-03 gold'
    exit()

gold = pd.read_csv(sys.argv[3].capitalize()+' Futures Historical Data.csv',parse_dates=[0],index_col=0, thousands=',')


assert min(( parse(sys.argv[1]) -pd.to_datetime(gold.index[-1])).total_seconds(), -(parse(sys.argv[2])-gold.index[0]).total_seconds(), (parse(sys.argv[2])-parse(sys.argv[1])).total_seconds()) >=0, 'Error: re-check the range interval in input or download a commodity file with an appropriate date range'

print sys.argv[3], gold[sys.argv[2]:sys.argv[1]].Price.mean(),gold[sys.argv[2]:sys.argv[1]].Price.var(skipna=True)
