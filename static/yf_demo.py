import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


#Define Ticker:
tickers = ['TNA', 'TQQQ', 'SPY']

#define timeframe:
end_date = datetime.today()
start_date = end_date - timedelta(days= 2 )
#print(end_date,start_date)

#download close prices in a dataframe:
close_df = pd.DataFrame()

for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    close_df[ticker] = data['Close']


print(close_df)

