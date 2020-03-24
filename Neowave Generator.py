#This utility will help to generate Neo Wave chart from data downloaded from yahoo finance 
# Neo wave is concept created from elliot wave analysis of securities price
 
import pandas as pd
from datetime import datetime

#from dateutil.relativedelta import *
import matplotlib.pyplot as plt
Low =0
High =0

#copy the csv folder to folder where this python code is existing

df2 = pd.read_csv('NIFTY Midcap 100 Historical Data.csv')
df2

Low  = df2['Low']
High = df2['High']
 
df2['Date']= pd.to_datetime(df2['Date']) 
 
# set start date and set the frequency of no of days for the data analysis and chart creation.. this utility is not useful for 
# creating neo wave for short duration such as intra day .It must be used only for 15 days or for long term understanding
# of securities .For example we have use analysis to start from 2015 and freq has been set to 50


days =  pd.Series(pd.date_range('2015-06-01',periods=180,freq='50D'))

# Duration from date also need to be incremented by 50 days. idea is to find high and low price of security within 50 days and so on
seconddays = days + pd.Timedelta(days=50)

frame = { 'Firstdate': days, 'Seconddate': seconddays } 
  
combinedays = pd.DataFrame(frame) 
  
# Creating an empty data frame 
dffinal  = df = pd.DataFrame()

#logic to create base data for plotting neo wave 

for index ,row in combinedays.iterrows():
        
        df3 = df2[(df2['Date'] > row['Firstdate']) & (df2['Date'] < row['Seconddate'])]
        if df3.empty == False:
            highindex = df3[['High']].idxmax()
            #print (df3)
            lowindex =   df3[['Low']].idxmin()
            df4 =df3.loc [highindex]
            df7  = df4[['Date','High']]
            df8  = df7.rename(columns = { "Date": "Date","High": "StockPrice"})
            df5 =df3.loc [lowindex]
            df9  = df5[['Date','Low']]
            df10  = df9.rename(columns = {"Date": "Date","Low": "StockPrice"})
            df6  = pd.concat([df8,df10])
            df6.index = pd.to_datetime(df6['Date'])
            del df6['Date']                               
            dffinal  = dffinal.append(df6)
 
 
# sorting data frame by name 
dffinal.sort_index(axis=0,inplace = True)

# create Neo wave starat after setting the required parameters

dffinal['StockPrice'].plot(kind= 'line',figsize=(13,6))
plt.ylabel('Stock Price') 
plt.xlabel('Date')
plt.title('MIDCAP 100 2005-2020 Neo Wave Chart-Duration 50 days')
plt.grid(True, linewidth=0.5, color ='#000000', linestyle = '-' )
plt.show()

#dffinal['StockPrice'].dtype
dffinal.tail(100)
#combinedays
#df3