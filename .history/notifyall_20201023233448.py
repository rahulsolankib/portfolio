# print('Yes Rahul! I have notified all peoples')
import schedule
import time
import yfinance as yf
import numpy as np 
from statistics import mean 
from pandas_datareader import data

import pandas as pd
import math
from datetime import date, timedelta
import requests

from twilio.rest import Client 
account_sid = 'AC99c04c65707246fda97538520277b450' 
auth_token = '190674744f34baa4078fb2325dcbb6fc' 


def job():
    print("I'm working...")
    tickers = yf.Tickers('msft aapl goog amzn wba noc ba lmt mcd intc nav ibm txn ma ge axp pep ko jnj tm hmc msbhy sne xom cvx vlo f bac')
    label = ['msft aapl goog amzn wba noc ba lmt mcd intc nav ibm txn ma ge axp pep ko jnj tm hmc msbhy sne xom cvx vlo f bac']
    today = date.today() 
    days_before = (date.today()-timedelta(days=90)).isoformat()
    df = tickers.history(start = days_before, end = today)
    stock_open = np.array(df['Open']).T.tolist()
    stock_close = np.array(df['Close']).T
    X1 = []
    movements = [[0 for i in range(len(stock_close[0]))] for j in range(len(stock_close))]
    for i in range(len(stock_close)):
        for j in range(len(stock_close[0])):
            movements[i][j]  = (stock_close[i][j] - stock_open[i][j])/stock_open[i][j]
        X1.append(sum(movements[i]))
    m = [0 for i in range(len(stock_close))]
    for i in range(len(stock_close)):
        m[i] = mean(stock_close[i])
    r = [[0 for i in range(len(stock_close[0]))] for j in range(len(stock_close))]
    v = [0 for i in range(len(stock_close))]
    for i in range(len(stock_close)):
        for j in range(len(stock_close[0])):
            r[i][j] = (stock_close[i][j] - m[i]) * (stock_close[i][j] - m[i])
        v[i] = sum(r[i])/len(stock_close[1])
    X2 = []
    for i in range(len(stock_close)):
        X2.append(math.sqrt(v[i] * 252))
    X1 = np.array(X1).reshape(len(X1), 1)
    X2 = np.array(X2).reshape(len(X2), 1)
    client = Client(account_sid, auth_token) 
 
    msg = 'Company\tOpen\tClose \n'
    for i in range(len(X1)):
        # userreturns and userrisk
        if (X1[i] < 0.5 or X2[i] > 204) and (np.sum(np.isnan(X1[i]),dtype=np.float64) == 0  and np.sum(np.isnan(X2[i]),dtype=np.float64) == 0):
            stri = label[i]+'\t:'+str(X1[i])+'\t: '+str(X2[i])+'\n'
            msg +=stri
        break
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=str(msg),      
                              to='whatsapp:+919930414832' 
                          ) 


schedule.every(1).seconds.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("21:03").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# print(time.localtime())

while True:
    schedule.run_pending()
    time.sleep(1)



# import datetime
# import time





#import matplotlib.pyplot as plt




        