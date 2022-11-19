# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 18:35:09 2022

@author: Hp
"""

import  streamlit as st
import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import plotly.express as px
import plotly.graph_objects as go
st.set_page_config(layout="wide")
import matplotlib.pyplot as plt
import numpy as np
import pandas_ta as ta
import base64

start = dt.datetime(2021,11,11)
end = dt.datetime.now()

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: 100% 100%;


    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local(r'C:\Users\Hp\bgg.jpg')

st.markdown(f'<h1 style="color:red;background-color: rgba(255, 255, 255, 0.3);font-size:48px;border-radius:3%;">{"Algorithmic trading"}</h1>', unsafe_allow_html=True)
st.header("Predicting when to buy and sell your stocks")
tab1, tab2, tab3 = st.tabs(["stocks share visualizations", "Trade Signals", "Strategy return"])
with tab1:
    st.header("Visualizing different stocks share price")
    
    stocks = web.DataReader(['FB','AMZN', 'AAPL', 'NFLX', 'GOOGL', 'MSFT'], 'yahoo', start, end)
    stocks_close = pd.DataFrame(web.DataReader(['FB','AMZN', 'AAPL', 'NFLX', 'GOOGL', 'MSFT'], 'yahoo', start, end)['Close'])
    area_chart = px.area(stocks_close.FB, title = 'FACEBOOK SHARE PRICE (2021-2022)')
    
    area_chart.update_xaxes(title_text = 'Date')
    area_chart.update_yaxes(title_text = 'FB Close Price', tickprefix = '$')
    area_chart.update_layout(showlegend = False)


    option = st.selectbox("", ("Select your stock","FB","AMZN","AAPL"))


# Customized Area chart
    if option == "FB":
        c_area = px.area(stocks_close.FB, title = 'FACBOOK SHARE PRICE (2021-2022)')
        
        c_area.update_xaxes(
            title_text = 'Date',
            rangeslider_visible = True,
            rangeselector = dict(
                buttons = list([
                    dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
                    dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
                    dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
                    dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
                    dict(step = 'all')])))
        
        c_area.update_yaxes(title_text = 'FB Close Price', tickprefix = '$')
        c_area.update_layout(showlegend = False,
            title = {
                'text': 'FACEBOOK SHARE PRICE (2021-2022)',
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
        st.plotly_chart(c_area,use_container_width=True)
    elif option == "AMZN":
        c_candlestick = go.Figure(data = [go.Candlestick(x = stocks.index, 
                                                       open = stocks[('Open',    'AMZN')], 
                                                       high = stocks[('High',    'AMZN')], 
                                                       low = stocks[('Low',    'AMZN')], 
                                                       close = stocks[('Close',    'AMZN')])])
        
        c_candlestick.update_xaxes(
            title_text = 'Date',
            rangeslider_visible = True,
            rangeselector = dict(
                buttons = list([
                    dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
                    dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
                    dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
                    dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
                    dict(step = 'all')])))
        
        c_candlestick.update_layout(
            title = {
                'text': 'AMAZON SHARE PRICE (2021-2022)',
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
        
        c_candlestick.update_yaxes(title_text = 'AMZN Close Price', tickprefix = '$')
        st.plotly_chart(c_candlestick, use_container_width=True)
        
    elif option == "AAPL":
        c_ohlc = go.Figure(data = [go.Ohlc(x = stocks.index, 
                                                       open = stocks[('Open',    'AAPL')], 
                                                       high = stocks[('High',    'AAPL')], 
                                                       low = stocks[('Low',    'AAPL')], 
                                                       close = stocks[('Close',    'AAPL')])])
        
        c_ohlc.update_xaxes(
            title_text = 'Date',
            rangeslider_visible = True,
            rangeselector = dict(
                buttons = list([
                    dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
                    dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
                    dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
                    dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
                    dict(step = 'all')])))
        
        c_ohlc.update_layout(
            title = {
                'text': 'APPLE SHARE PRICE (2021-2022)',
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
        c_ohlc.update_yaxes(title_text = 'AAPL Close Price', tickprefix = '$')
        st.plotly_chart(c_ohlc, use_container_width=True)
        
        
    st.header ('Customize your stocks from bullet charts') 
    # Customized Bullet chart
    
    c_bullet = go.Figure()
    
    c_bullet.add_trace(go.Indicator(
        mode = "number+gauge+delta", 
        value = int(stocks_close['NFLX'].tail(1)),
        delta = {'reference': int(stocks_close['NFLX'].tail(2)[0])},
        domain = {'x': [0.25, 1], 
                  'y': [0.08, 0.25]},
        title = {'text':"<b>NETFLIX DAY<br>RANGE</b><br><span style='color: gray; font-size:0.8em'>U.S. $</span>", 
                 'font': {"size": 14}},    
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 550]},
            'threshold': {
                'line': {'color': "Red", 'width': 2},
                'thickness': 0.75,
                'value': 505},
            'steps': [
                {'range': [0, 350], 'color': "gray"},
                {'range': [350, 550], 'color': "lightgray"}],
            'bar': {'color': 'black'}}))
    
    c_bullet.add_trace(go.Indicator(
        mode = "number+gauge+delta", 
        value = int(stocks_close['GOOGL'].tail(1)),
        delta = {'reference': int(stocks_close['GOOGL'].tail(2)[0])},
        domain = {'x': [0.25, 1], 
                  'y': [0.4, 0.6]},
        title = {'text':"<b>GOOGLE DAY<br>RANGE</b><br><span style='color: gray; font-size:0.8em'>U.S. $</span>", 
                 'font': {"size": 14}},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 1800]},
            'threshold': {
                'line': {'color': "red", 'width': 2},
                'thickness': 0.75,
                'value': 1681},
            'steps': [
                {'range': [0, 1300], 'color': "gray"},
                {'range': [1300, 1800], 'color': "lightgray"}],
            'bar': {'color': 'black'}}))
    
    c_bullet.add_trace(go.Indicator(
        mode = "number+gauge+delta", 
        value = int(stocks_close['MSFT'].tail(1)),
        delta = {'reference': int(stocks_close['MSFT'].tail(2)[0])},
        domain = {'x': [0.25, 1], 
                  'y': [0.7, 0.9]},
        title = {'text':"<b>MICROSOFT DAY<br>RANGE</b><br><span style='color: gray; font-size:0.8em'>U.S. $</span>", 
                 'font': {"size": 14}},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 250]},
            'threshold': {
                'line': {'color': "red", 'width': 2},
                'thickness': 0.75,
                'value': 208},
            'steps': [
                {'range': [0, 150], 'color': "gray"},
                {'range': [150, 250], 'color': "lightgray"}],
            'bar': {'color': "black"}}))
    
    c_bullet.update_layout(height = 400 , margin = {'t':0, 'b':0, 'l':0})
    st.plotly_chart(c_bullet, use_container_width=True)
    # Gauge chart
    st.header('know the daily range of stocks and invest')
    
    gauge = go.Figure(go.Indicator(
        domain = {'x': [0, 1], 
                  'y': [0, 1]},
        value = int(stocks_close['FB'].tail(1)),
        mode = "gauge+number+delta",
        title = {'text':"<b>FACEBOOK DAY RANGE</b><br><span style='color: gray; font-size:0.8em'>U.S. $</span>", 
                 'font': {"size": 20}},
        delta = {'reference': int(stocks_close['FB'].tail(2)[0])},
        gauge = {
                 'axis': {'range': [None, 300]},
                 'steps' : [
                     {'range': [0, 200], 'color': "lightgray"},
                     {'range': [200, 300], 'color': "gray"}],
                 'threshold' : {'line': {'color': "red", 'width': 4}, 
                                'thickness': 0.75, 
                                'value': 276}}))
    st.plotly_chart(gauge, use_container_width=True)
    
    
    


with tab2:
    st.header("Creating Signals to predict when to buy and sell your stocks ")
    st.header('Using MACD to create Signal Line')
   #Calculate the MACD and signal indicators
#calculate short term EMA

    shortEMA=stocks_close.AAPL.ewm(span=12,adjust=False).mean()
    #calculate short term EMA
    LongEMA=stocks_close.AAPL.ewm(span=26,adjust=False).mean()
    #calculate the MACD line
    MACD=shortEMA-LongEMA
    signal=MACD.ewm(span=9,adjust=False).mean()
    fig=plt.figure(figsize=(12.2,4.5))
    plt.plot(stocks_close.index,MACD,label="AAPL MACD",color='red')
    plt.plot(stocks_close.index,signal,label='Signal line',color='blue')
    plt.xticks(rotation=45)
    plt.legend(loc='upper left')
    st.pyplot(fig)
    data=stocks_close
    st.header('Buy and Sell Signals')
    import talib
    data['SMA 30'] = ta.sma(data['AAPL'],30)
    data['SMA 100'] = ta.sma(data['AAPL'],100)
    #SMA BUY SELL
    #Function for buy and sell signal
    def buy_sell(data):
        signalBuy = []
        signalSell = []
        position = False 
    
        for i in range(len(data)):
            if data['SMA 30'][i] > data['SMA 100'][i]:
                if position == False :
                    signalBuy.append(stocks['Adj Close']['AAPL'][i])
                    signalSell.append(np.nan)
                    position = True
                else:
                    signalBuy.append(np.nan)
                    signalSell.append(np.nan)
            elif data['SMA 30'][i] < data['SMA 100'][i]:
                if position == True:
                    signalBuy.append(np.nan)
                    signalSell.append(stocks['Adj Close']['AAPL'][i])
                    position = False
                else:
                    signalBuy.append(np.nan)
                    signalSell.append(np.nan)
            else:
                signalBuy.append(np.nan)
                signalSell.append(np.nan)
        return pd.Series([signalBuy, signalSell])
    data['Buy_Signal_price'], data['Sell_Signal_price'] = buy_sell(data)
    fig, ax = plt.subplots(figsize=(14,8))
    ax.plot(stocks['Adj Close']['AAPL'] , label = 'AAPL' ,linewidth=0.5, color='blue', alpha = 0.9)
    ax.plot(data['SMA 30'], label = 'SMA30', alpha = 0.85)
    ax.plot(data['SMA 100'], label = 'SMA100' , alpha = 0.85)
    ax.scatter(data.index , data['Buy_Signal_price'] , label = 'Buy' , marker = '^', color = 'green',alpha =1 )
    ax.scatter(data.index , data['Sell_Signal_price'] , label = 'Sell' , marker = 'v', color = 'red',alpha =1 )
    ax.set_title( "AAPL  Price History with buy and sell signals",fontsize=10, backgroundcolor='blue', color='white')
    ax.set_xlabel(f'{start} - {end}' ,fontsize=18)
    ax.set_ylabel('Close Price INR (₨)' , fontsize=18)
    legend = ax.legend()
    ax.grid()
    plt.tight_layout()
    st.pyplot(fig,ax)
with tab3:
    st.header('know the strategy return of your stocks')
    stocks['Open-Close']=stocks['Open']['MSFT']-stocks['Close']['MSFT']
    stocks['High-Low']=stocks['High']['MSFT']-stocks['Low']['MSFT']
    df2=stocks
    x=df2[['Open-Close','High-Low']]
    y=np.where(stocks['Close']['MSFT'].shift(-1)>stocks['Close']['MSFT'],1,0)
    split_percentage=0.80
    split=int(split_percentage*len(stocks))
    x_train=x[:split]
    y_train=y[:split]
    
    x_test=x[split:]
    y_test=y[split:]
    from sklearn.svm import SVC
    SVC().fit(x,y)
    cls=SVC().fit(x_train,y_train)
    from sklearn.metrics import accuracy_score
    accuracy_train=accuracy_score(y_train,cls.predict(x_train))
    accuracy_test=accuracy_score(y_test,cls.predict(x_test))
    option2 = st.selectbox("", ("Select your stock","FB","AMZN","AAPL","MSFT","GOOGL"))
    if option2 == "GOOGL":
        st.header('Strategy return of Google stocks')
        
        stocks['predicted_signal']=cls.predict(x)
        stocks['Return']=stocks['Close']['GOOGL'].pct_change()
        stocks['strategy']=stocks.Return*stocks.predicted_signal.shift(1)
        stocks['strategy_return']=stocks.Return*stocks.predicted_signal.shift(1)
        fig2=plt.figure(figsize=(2.8,2.0))
        geometric_returns=(stocks.strategy_return.iloc[split:]+1).cumprod()
        geometric_returns.plot(figsize=(10,7),color='g')
        plt.ylabel("strategy_return(%)")
        plt.xlabel("Date")
        st.pyplot(fig2)
    elif option2=="AMZN":
        st.header('Strategy return of Amazon stocks')
        stocks['Open-Close']=stocks['Open']['AMZN']-stocks['Close']['AMZN']
        stocks['High-Low']=stocks['High']['AMZN']-stocks['Low']['AMZN']
        df3=stocks
        x1=df3[['Open-Close','High-Low']]
        y1=np.where(stocks['Close']['AMZN'].shift(-1)>stocks['Close']['AMZN'],1,0)
        split_percentage=0.80
        split=int(split_percentage*len(stocks))
        x_train=x1[:split]
        y_train=y1[:split]
        
        x_test=x1[split:]
        y_test=y1[split:]
        from sklearn.svm import SVC
        SVC().fit(x1,y1)
        cls=SVC().fit(x_train,y_train)
        accuracy_train=accuracy_score(y_train,cls.predict(x_train))
        accuracy_test=accuracy_score(y_test,cls.predict(x_test))
        stocks['predicted_signal']=cls.predict(x)
        stocks['Return']=stocks['Close']['AMZN'].pct_change()
        stocks['strategy']=stocks.Return*stocks.predicted_signal.shift(1)
        stocks['strategy_return']=stocks.Return*stocks.predicted_signal.shift(1)
        fig3=plt.figure(figsize=(2.8,2.0))
        geometric_returns=(stocks.strategy_return.iloc[split:]+1).cumprod()
        geometric_returns.plot(figsize=(2.8,2.0),color='g')
        plt.ylabel("strategy_return(%)")
        plt.xlabel("Date")
        st.pyplot(fig3)
    elif option2=="MSFT":
       st.header('Strategy return of Microsoft stocks')
       stocks['Open-Close']=stocks['Open']['MSFT']-stocks['Close']['MSFT']
       stocks['High-Low']=stocks['High']['MSFT']-stocks['Low']['MSFT']
       df4=stocks
       x2=df4[['Open-Close','High-Low']]  
       y2=np.where(stocks['Close']['MSFT'].shift(-1)>stocks['Close']['MSFT'],1,0)
       split_percentage=0.80
       split=int(split_percentage*len(stocks))
       x_train=x2[:split]
       y_train=y2[:split]
        
       x_test=x2[split:]
       y_test=y2[split:] 
       from sklearn.svm import SVC
       SVC().fit(x2,y2)
       stocks['predicted_signal']=cls.predict(x)
       stocks['Return']=stocks['Close']['MSFT'].pct_change()
       stocks['strategy']=stocks.Return*stocks.predicted_signal.shift(1)
       stocks['strategy_return']=stocks.Return*stocks.predicted_signal.shift(1)
       fig4=plt.figure(figsize=(2.8,2.0))
       geometric_returns=(stocks.strategy_return.iloc[split:]+1).cumprod()
       geometric_returns.plot(figsize=(2.8,2.0),color='g')
       plt.ylabel("strategy_return(%)")
       plt.xlabel("Date")
       st.pyplot(fig4)








    
    



    

