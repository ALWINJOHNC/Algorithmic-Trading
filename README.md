# Algorithmic-Trading using SVC and MACD
 Moving Average Convergence /Divergence indicator shows relationship between two moving averages.MACD is a momentum oscillator  used to trade trends.We define when to buy and sell the stocks using MACD and plot the buy and sell signals so the traders can easily know when to buy and sell particular stocks.
 SVC Algorithm is  a supervised machine learning algorithm and is used to implement a strategy return model so the customers know about the trend of particular stocks by predicting the returns and  it helps in taking future decisions regarding the stocks they are involved in.

## Dataset used
Financial Data was taken from yahoo finance using the pandas Datareader.The Data contains the stocks information of various stocks like AAPLE,GOOGLE,MICROSOFT,NETFLIX,FACEBOOK,AMAZON with all the financial data regarding it.The data was taken from November 11,2021 to the present day .

### Attributes used
Attributes used include the Adjacent Close price,Close price,high,low,volume,open  of the daily financail report of each Companies.

###Datasplit
 The SVC model was split to 80:20 for the training:testing purpose respectively.The SVC model was fitted  and predicted the strategy return of each stocks.

 ### visualisations
 Different interactive plotly charts like area charts,candlestick chart,guage chart,ohlc chart were used so the user can easily identify and learn about the current trend of each stocks.
 ### Model architecture
