import bs4
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from time import sleep
import sqlite3
from sqlite3 import Error
import time

url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch'
database = r"/usr/src/app/StockData.db"
conn = sqlite3.connect(database)
    

def add_price(conn, price):
    sql = ''' INSERT INTO AAPLData(time,price)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, price)

def startwebscraping():
    try:
        page = urlopen(url)
    except:
        print('Error opening the URL')

    soup = BeautifulSoup(page,'html.parser')

    soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})

    while True: 
        price_value = float(soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text)
        price = (int(time.time()), price_value)
        add_price(conn, price)
        print("Added: " + str(int(time.time())) + " and " + str(price_value))
        sleep(1)

if __name__ == '__main__':
    startwebscraping()