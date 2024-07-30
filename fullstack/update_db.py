import sqlite3
import alpaca_trade_api as tradeapi

connection = sqlite3.connect('app.db')    #if the flie does not exist it creates one database
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

# Query from Python

cursor.execute("SELECT symbol, company FROM stock")
rows = cursor.fetchall()

# for row in rows:
#     print(row['symbol'])


symbols = [row['symbol'] for row in rows] # creating a list of all symbols in the database



apikey = 'PKHE04W3FWDWPAMOVWSB'
apisecret = 'mww2dno0mgcvVoAdYdik3UslklsTTFwSRout2Y60'
api = tradeapi.REST(apikey,apisecret,base_url='https://paper-api.alpaca.markets')


assets = api.list_assets()

for asset in assets:
    try:
        if asset.status == 'active' and asset.tradable and asset.symbol not in symbols:
            # print(asset.symbol)
            cursor.execute("INSERT INTO stock (symbol, company) VALUES(?, ?)",(asset.symbol, asset.name))
    except Exception as e:
        # print(asset.symbol)
        print(e)



connection.commit() # Save the database