
import sqlite3
import alpaca_trade_api as tradeapi

connection = sqlite3.connect('app.db')    #if the flie does not exist it creates one database

cursor = connection.cursor()

#cursor.execute("insert into stock (symbol, company) values('ADBE', 'Adobe Inc.')")
#cursor.execute("insert into stock (symbol, company) values('VZ', 'AVerizon')")
#cursor.execute("insert into stock (symbol, company) values('Z', 'Zillow')")

cursor.execute("delete from stock") # delete everything from stock database
apikey = 'PKHE04W3FWDWPAMOVWSB'
apisecret = 'mww2dno0mgcvVoAdYdik3UslklsTTFwSRout2Y60'
api = tradeapi.REST(apikey,apisecret,base_url='https://paper-api.alpaca.markets')

assets = api.list_assets()

for asset in assets:
    # if asset.status == 'VXX':
    #     print(asset)
    #print(asset)
    try:
        if asset.status == 'active' and asset.tradable:
            cursor.execute("INSERT INTO stock (symbol, company) VALUES(?, ?)",(asset.symbol, asset.name))
    except Exception as e:
        # print(asset.symbol)
        print(e)


cursor.execute("delete from stock where symbol = 'AAPL'")
connection.commit() # Save the database

# print (cursor.execute("SELECT * FROM stock WHERE symbol = 'VXX'"))

