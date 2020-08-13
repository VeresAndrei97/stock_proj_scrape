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

url = 'https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch' # url to acces the stock page

class webscrapping:
    def __init__(self,opening_bid, actual_price,buy_bid,sell_bid,counter_buys,counter_sells,global_counter):
        self.opening_bid = opening_bid      # cu cat incepe ziua
        self.actual_price = actual_price    # pretul actual a stock ului
        self.buy_bid = buy_bid              # pretul cu care vom cumpara
        self.sell_bid = sell_bid            # pretul cu care vom vinde
        self.counter_buys = counter_buys    # contor pt numaru de buy uri facute
        self.counter_sells = counter_sells  # contor pt numaru de sell uri facute
        self.global_counter = global_counter#counter for all stock price that we found OLD or NEW

    def priceTracker(self):          # web-scrapping through that yahoo page from URL
        response = requests.get(url)
        today=date.today()
        soup = BeautifulSoup(response.text, 'lxml')
        price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        self.actual_price = float(price.replace(",",""))
        self.global_counter += self.global_counter
        return price

    def stock_buy(self):             # 0.2% fluctuatie negativa de la cat am cumparat initial.
        buy_bid = self.opening_bid - 0.2*self.actual_price/100.0
        if buy_bid == self.actual_price:
            print ("Now you should buy")
            self.counter_buys = counter_buys + 1

    def stock_sell(self):            # inapoi 0.2% fluctuatie Pozitiva de la cat am cumparat initial
        sell_bid = self.buy_bid + 0.2*self.actual_price/100 
        if sell_bid == self.actual_price:
            print ("Now you should sell")
            self.counter_sells += self.counter_sells

opening_bid_main = 0.0
suma_stock = 0.0 
pretz=webscrapping(opening_bid_main,0.0,0.0,0.0,0,0,0.0)
while True: 
    print(pretz.priceTracker())
    pretz.stock_buy()
    pretz.stock_sell()
   