'''
1. Please write a program to fetch the historical prices and dates of gold and silver from these 2 URLs:

https://www.investing.com/commodities/gold-historical-data

https://www.investing.com/commodities/silver-historical-data

and store them locally (in a file or database, as you see fit).

(You can just extract the default data range in each case: no need to interact with the UI elements.)


'''


import requests,sys, pandas as pd

if len(sys.argv) <2:
    print 'Syntax: python fetchCommodityPrice.py gold'
    exit()


url = 'https://www.investing.com/commodities/'+sys.argv[1]+'-historical-data'

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'andrea.m1020@gmail.com'
}

response = requests.get(url, headers=headers)
df = pd.read_html(response.content,index_col=0,parse_dates=[0])[2]
df.to_csv(sys.argv[1].capitalize()+' Futures Historical Data.csv')

