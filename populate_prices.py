
import sqlite3, config
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame, TimeFrameUnit


api = tradeapi.REST(config.API_KEY,config.SECRET_KEY,base_url=config.API_URL)
assets = api.list_assets()

connection = sqlite3.connect(config.DB_FILE)    #if the flie does not exist it creates one database
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

# Query from Python

cursor.execute("SELECT id, symbol, name FROM stock")
rows = cursor.fetchall()

# symbols = []
# stock_dict = {}
# for row in rows:
#     symbol = row['symbol']
#     symbols.append(symbol)
#     stock_dict[symbol] = row['id']

# symbols = [row['symbol'] for row in rows]
# print(symbols)
# stock_ids = [row['id'] for row in rows]
# stock_dict = dict(zip(symbols,stock_ids))
# print(stock_dict)

symbols = []
stock_dict = {}
for row in rows:
    symbol = row['symbol']
    symbols.append(symbol)
    stock_dict[symbol] = row['id']



# barset = api.get_bars(['AAPL','MSFT'], TimeFrame(1, TimeFrameUnit.Day), "2023-01-01", "2024-08-02")
# for bar in barset:
#     print(bar.S)


# barsets = api.get_bars(['AAPL'],TimeFrame(1, TimeFrameUnit.Day))
# barsets = api.get_bars('SUSHI/USD',TimeFrame(1, TimeFrameUnit.Day)) # No data
# print(barsets.df)

chunk_size = 200


for i in range(0,len(symbols)-300,chunk_size):
    # print(i)
    # print(i+chunk_size)
    symbol_chunk = symbols[i:i+chunk_size]
    # print(symbol_chunk)
    # print(len(symbol_chunk))
    barsets = api.get_bars(symbol_chunk,TimeFrame(1, TimeFrameUnit.Day),config.START_DATE, config.END_DATE)
    # barsets = api.get_bars(symbol_chunk,TimeFrame(1, TimeFrameUnit.Day),"2020-07-01", "2020-08-01")
    for bar in barsets:
        stock_id= stock_dict[bar.S]
# symbol = bar.S
        # print(bar.S)
        print(f'processing symbol:{bar.S}')
        # print(stock_id, bar.t.date(), bar.o, bar.h, bar.l, bar.c,  bar.v)
        cursor.execute("INSERT INTO stock_price (stock_id, date, open, high, low, close, volume) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                       (stock_id, bar.t.date(), bar.o, bar.h, bar.l, bar.c,  bar.v))


connection.commit()

cursor.close()

# for i in range(0,13,5):
#     print(i)

######### practice



# api = tradeapi.REST(config.API_KEY,config.SECRET_KEY,base_url=config.API_URL)

# barsets = api.get_bars(['AAPL','MSFT'],TimeFrame(1, TimeFrameUnit.Minute))


# # barsets = api.get_bars(['AAPL','MSFT'],tradeapi.rest.TimeFrame.Day)
# # barsets = api.get_bars(['AAPL','MSFT'],tradeapi.rest.TimeFrameUnit.Day)
# # barsets = api.get_bars(['AAPL','MSFT'],tradeapi.rest.TimeFrame.Day)

# # barsets = api.get_bars(['AAPL','MSFT'],TimeFrame(1, TimeFrameUnit.Day), "2021-06-08", "2021-06-08")
# barsets = api.get_bars(['AAPL','MSFT'],TimeFrame(1, TimeFrameUnit.Minute))


# # print(api.get_bars("AAPL", TimeFrame(45, TimeFrameUnit.Minute), "2021-06-08", "2021-06-08", adjustment='raw').df)



# # for bar in barsets:
#     # print(f'processing symbol:{bar.S}')
#     # print(bar.t, bar.o, bar.h,bar.l,bar.c,bar.v)
    
# print(barsets.df)
#     # print(bar.S)
# # connection = sqlite3.connect(config.DB_FILE)    #if the flie does not exist it creates one database
# # connection.row_factory = sqlite3.Row

# # cursor = connection.cursor()

# # # Query from Python

# # cursor.execute("SELECT symbol, company FROM stock")
# # rows = cursor.fetchall()

# # # for row in rows:
# # #     print(row['symbol'])


# # symbols = [row['symbol'] for row in rows] # creating a list of all symbols in the database
