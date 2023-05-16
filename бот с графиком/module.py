#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import datetime
import time
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# In[2]:


companies = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Amazon': 'AMZN',
    'Facebook': 'FB',
    'Alphabet': 'GOOGL',
    'Tesla': 'TSLA',
    'Johnson & Johnson': 'JNJ',
    'Procter & Gamble': 'PG',
    'JPMorgan Chase': 'JPM',
    'Visa': 'V',
    'Walmart': 'WMT',
    'Coca-Cola': 'KO',
    'Intel': 'INTC',
    'AT&T': 'T',
    'Cisco Systems': 'CSCO',
    'Verizon Communications': 'VZ',
    'Pfizer': 'PFE',
    'ExxonMobil': 'XOM',
    'Chevron': 'CVX',
    'IBM': 'IBM'
}
token = '4TNC3MJ8OEM0GYWZ'


# In[3]:


def show(name):
    b_name = companies[name]
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={b_name}&apikey={token}'
    r = requests.get(url)
    data = r.json()
    date = []
    close = []
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    year_ago = (datetime.datetime.strptime(today, '%Y-%m-%d') - datetime.timedelta(days=365)).strftime('%Y-%m-%d')
    for k, v in zip(data['Weekly Time Series'].keys(), data['Weekly Time Series'].values()):
        if time.strptime(year_ago, "%Y-%m-%d") < time.strptime(k, "%Y-%m-%d"):
            date.append(k)
            close.append(float(v['4. close']))
    sns.set_style('darkgrid')
    fig, ax = plt.subplots(figsize = (10, 8))
    plt.plot(date[::-1], close)
    plt.xlabel('Дата')
    plt.ylabel('Цена, USD')
    plt.title(f'График изменения цены акций компании {name}')
    plt.xticks(rotation = 'vertical');
    plt.savefig('graph')


# In[4]:


show('Coca-Cola')


# In[ ]:




