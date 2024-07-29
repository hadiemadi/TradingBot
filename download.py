import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

ticker = 'AAPL'
end_date = datetime.today()
start_date = end_date - timedelta(days= 2 )
data = yf.download(ticker, start=start_date, end=end_date)
data.to_csv('AAPL.csv')