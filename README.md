# Algorithmic-Trading using SVC and MACD
Algorithmic trading predicts when to buy and sell different stocks which could be of great use to the traders.

 Moving Average Convergence /Divergence indicator shows relationship between two moving averages.MACD is a momentum oscillator  used to trade trends.We define when to buy and sell the stocks using MACD and plot the buy and sell signals so the traders can easily know when to buy and sell particular stocks.
 SVC Algorithm is  a supervised machine learning algorithm and is used to implement a strategy return model so the customers know about the trend of particular stocks by predicting the returns and  it helps in taking future decisions regarding the stocks they are involved in.

## Dataset used
Financial Data was taken from yahoo finance using the pandas Datareader.The Data contains the stocks information of various stocks like AAPLE,GOOGLE,MICROSOFT,NETFLIX,FACEBOOK,AMAZON with all the financial data regarding it.The data was taken from November 11,2021 to the present day .

### Attributes used
Attributes used include the Adjacent Close price,Close price,high,low,volume,open  of the daily financial report of each Companies.

### Datasplit
 The SVC model was split to 80:20 for the training:testing purpose respectively.The SVC model was fitted  and predicted the strategy return of each stocks.

 ### Visualizations
 Different interactive plotly charts like area charts,candlestick chart,guage chart,ohlc chart were used so the user can easily identify and learn about the current trend of each stocks.
 ### Model architecture
 ![122](https://user-images.githubusercontent.com/94182708/202833142-3d2e5525-575f-4bc3-ad82-961b1e89bb32.jpg)
 
 1.MACD  
MACD turns two trend-following indicators, moving averages , into a momentum oscillator by subtracting the longer moving average from the shorter moving average. As a result, the MACD offers the best of both worlds: trend following and momentum.
     ![image](https://user-images.githubusercontent.com/94182708/202832885-d87e9ec7-6bc2-452a-ac01-0f630f0ed6b7.png)
     
     
2.SVC

 Basically, the main goal of the Support Vector Machine is to construct a hyperplane, which it then uses to classify data. Despite generally being categorized as a      classification algorithm, there is an extension of the Support Vector Machine used for regression, known as Support Vector Regression.
 We predicted the strategy return of each stocks using SVC.
 
 ### Training and evaluation
 The data was trained 80% and tested 20% and usually algorithmic trading algorithm rarely have an accuracy of above 50%.
  This model recorded a training accuracy of 57.49% and testing accuracy of 55.77%  
     
   ### Working Model
   
   ![11](https://user-images.githubusercontent.com/94182708/202833947-0f06af10-1115-4fc8-84f5-deadadb1f4c6.jpg)
   
   ### Further scopes
   Much more trading strategies can be implemented based on this model and trading decisions can be made easier than ever.
   

     


