from django.shortcuts import render
from django.http import HttpResponse
from sklearn.linear_model import LinearRegression
import json
# pandas and numpy are used for data manipulation
import pandas as pd
import numpy as np
import io
import datetime
import urllib,base64
# matplotlib and seaborn are used for plotting graphs
import matplotlib.pyplot as plt
#%matplotlib inline
plt.style.use('seaborn-darkgrid')

# yahoo finance is used to fetch data
import yfinance as yf

details = {'title':'Portfolio Management','founders': ['Rahul Solanki', 'Niti Shah', 'Janice Shah'],'Quote':'Where there is a will there is a way' }
def home(request):
    context = {
        'details' : details,
        'title' : 'Portolio Management'
    }
    return render(request,'startPage/home.html',context)

def about(request):
    return render(request,'startPage/about.html',{'title':'About Page'})

def material(request):
    prev = datetime.datetime.now()
    now = prev
    now -= datetime.timedelta(1)
    prev -= datetime.timedelta(365)

    Df = yf.download('GLD', prev.date(), now.date(), auto_adjust=True)

    # Only keep close columns
    Df = Df[['Close']]

    # Drop rows with missing values
    Df = Df.dropna()

    # Plot the closing price of GLD
    fig = Df.Close.plot(figsize=(10, 7),color='r')
    plt.ylabel("Gold ETF Prices")
    plt.title("Gold ETF Price Series")
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    url_one = urllib.parse.quote(string)
    plt.close(fig)

    # Define explanatory variables
    Df['S_3'] = Df['Close'].rolling(window=3).mean()
    Df['S_9'] = Df['Close'].rolling(window=9).mean()
    Df['next_day_price'] = Df['Close'].shift(-1)

    Df = Df.dropna()
    X = Df[['S_3', 'S_9']]

    # Define dependent variable
    y = Df['next_day_price']

    # Split the data into train and test dataset
    t = .8
    t = int(t*len(Df))

    # Train dataset
    X_train = X[:t]
    y_train = y[:t]

    # Test dataset
    X_test = X[t:]
    y_test = y[t:]

    # Create a linear regression model
    linear = LinearRegression().fit(X_train, y_train)
    predicted_price = linear.predict(X_test)
    predicted_price = pd.DataFrame(
        predicted_price, index=y_test.index, columns=['price'])

    # R square
    r2_score = linear.score(X[t:], y[t:])*100
    float("{0:.2f}".format(r2_score))

    gold = pd.DataFrame()

    gold['price'] = Df[t:]['Close']
    gold['predicted_price_next_day'] = predicted_price
    gold['actual_price_next_day'] = y_test
    gold['gold_returns'] = gold['price'].pct_change().shift(-1)

    gold['signal'] = np.where(gold.predicted_price_next_day.shift(1) < gold.predicted_price_next_day,1,0)

    gold['strategy_returns'] = gold.signal * gold['gold_returns']
    fig = ((gold['strategy_returns']+1).cumprod()).plot(figsize=(10,7),color='g')
    plt.ylabel('Cumulative Returns')
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    url_three = urllib.parse.quote(string)
    plt.close(fig)
    
    prev = now
    prev -= datetime.timedelta(25)
    data = yf.download('GLD', prev.date(), now.date(), auto_adjust=True)
    data['S_3'] = data['Close'].rolling(window=3).mean()
    data['S_9'] = data['Close'].rolling(window=9).mean()
    data = data.dropna()
    data['predicted_gold_price'] = linear.predict(data[['S_3', 'S_9']])
    data['signal'] = np.where(data.predicted_gold_price.shift(1) < data.predicted_gold_price,"Buy","No Position")
    s = []
    date = now
    for i in range(7):
        date += datetime.timedelta(1)
        dateStr = date.strftime("%d %b %Y ")
        s.append(dateStr)
    df = data.tail(7)
    df['index'] = s 
    json_records = df.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    context = {
        'data' : data,
        'data1':url_one,
        'data3':url_three
    }
    return render(request,'startPage/material.html',context)

def silver(request):
    # prev = datetime.datetime.now()
    # now = prev
    # now -= datetime.timedelta(1)
    # prev -= datetime.timedelta(365)
    Df = yf.download('SI=F', '2019-10-25', '2020-10-25', auto_adjust=True)

    # Only keep close columns
    Df = Df[['Close']]

    # Drop rows with missing values
    Df = Df.dropna()

    # Plot the closing price of GLD
    fig = Df.Close.plot(figsize=(10, 7),color='r')
    plt.ylabel("Silver ETF Prices")
    plt.title("Silver ETF Price Series")
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    url_one = urllib.parse.quote(string)
    plt.close(fig)
    
    # Define explanatory variables
    Df['S_3'] = Df['Close'].rolling(window=3).mean()
    Df['S_9'] = Df['Close'].rolling(window=9).mean()
    Df['next_day_price'] = Df['Close'].shift(-1)

    Df = Df.dropna()
    X = Df[['S_3', 'S_9']]

    # Define dependent variable
    y = Df['next_day_price']

    # Split the data into train and test dataset
    t = .8
    t = int(t*len(Df))

    # Train dataset
    X_train = X[:t]
    y_train = y[:t]

    # Test dataset
    X_test = X[t:]
    y_test = y[t:]

    # Create a linear regression model
    linear = LinearRegression().fit(X_train, y_train)
    
    predicted_price = linear.predict(X_test)
    predicted_price = pd.DataFrame(predicted_price, index=y_test.index, columns=['price'])

    # R square
    r2_score = linear.score(X[t:], y[t:])*100
    float("{0:.2f}".format(r2_score))

    silver = pd.DataFrame()

    silver['price'] = Df[t:]['Close']
    silver['predicted_price_next_day'] = predicted_price
    silver['actual_price_next_day'] = y_test
    silver['silver_returns'] = silver['price'].pct_change().shift(-1)

    silver['signal'] = np.where(silver.predicted_price_next_day.shift(1) < silver.predicted_price_next_day,1,0)

    silver['strategy_returns'] = silver.signal * silver['silver_returns']
    fig = ((silver['strategy_returns']+1).cumprod()).plot(figsize=(10,7),color='g')
    plt.ylabel('Cumulative Returns')
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    url_three = urllib.parse.quote(string)
    plt.close(fig)
    # prev = now
    # prev -= datetime.timedelta(25)
    data = yf.download('SI=F','2020-9-30', '2020-10-25', auto_adjust=True)
    data['S_3'] = data['Close'].rolling(window=3).mean()
    data['S_9'] = data['Close'].rolling(window=9).mean()
    data = data.dropna()
    data['predicted_silver_price'] = linear.predict(data[['S_3', 'S_9']])
    data['signal'] = np.where(data.predicted_silver_price.shift(1) < data.predicted_silver_price,"Buy","No Position")
    s = []
    date = datetime.datetime.now()
    for i in range(7):
        date += datetime.timedelta(1)
        dateStr = date.strftime("%d %b %Y ")
        s.append(dateStr)
    df = data.tail(7)
    df['index'] = s 
    json_records = df.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    context = {
        'data' : data,
        'data1':url_one,
        'data3':url_three
    }
    return render(request,'startPage/silver.html',context)
