import sqlite3, config
import alpaca_trade_api as tradeapi

connection = sqlite3.connect(config.DB_FILE)    #if the flie does not exist it creates one database
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

# Query from Python

cursor.execute("SELECT symbol, name FROM stock")
rows = cursor.fetchall()

# for row in rows:
#     print(row['symbol'])


symbols = [row['symbol'] for row in rows] # creating a list of all symbols in the database


api = tradeapi.REST(config.API_KEY,config.SECRET_KEY,base_url=config.API_URL)
assets = api.list_assets()

for asset in assets:
    try:
        if asset.status == 'active' and asset.tradable and asset.symbol not in symbols:
            print(f"Added a new stock {asset.symbol} {asset.name}")
            cursor.execute("INSERT INTO stock (symbol, name) VALUES(?, ?)",(asset.symbol, asset.name))
    except Exception as e:
        print(asset.symbol)
        print(e)



connection.commit() # Save the database
