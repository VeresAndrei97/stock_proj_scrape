import numpy as np
#import quandl
import pandas as pd
#import tensorflow
import xgboost as xgb 
import matplotlib.pyplot as plt
from scipy import stats
from bs4 import BeautifulSoup
import requests
from datetime import date

k=0
actual_price = 0.0
vector_prices =[] 
#open_price = 0.0
#counter_price = 0

## Web-scrapping
def priceTracker():
    url = 'https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch'
    response = requests.get(url)
    today=date.today()
    soup = BeautifulSoup(response.text, 'lxml')
    #print(soup)
    #counter_price +=1
    price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    
    return price
    
#def Choice(price):
#actual_price = priceTracker()    
#vector_prices[0]= actual_price    
while True:
    actual_price = priceTracker() 
    

   # Choice(price)






## READING CSV FILE
df = pd.read_csv('tsla.csv')

stock_high = df['High']
stock_date = df['Date']
stock_low = df['Low']
stock_adj_close = df['Adj Close']


#print(df['High'])
#print(stock_adj_close)
plt.plot(stock_adj_close)
plt.show()


#LINEAR REGRESSION LAB-UTCN
#function [phi] = BLAfct(x, n)
#
#N=length(x);
#d = x{end} - x{1};
#b = d/(n-1);
#c=x{1}:b:x{end};

    #for k=1:N
     #   for j=1:n
      #      phi(k,j)= exp(-(x{k}-c(j)).^2/(b.^2));
       # end
    #end
#end