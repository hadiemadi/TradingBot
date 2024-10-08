
import sqlite3, config
import alpaca_trade_api as tradeapi

connection = sqlite3.connect(config.DB_FILE)    #if the flie does not exist it creates one database

cursor = connection.cursor()

#cursor.execute("insert into stock (symbol, company) values('ADBE', 'Adobe Inc.')")
#cursor.execute("insert into stock (symbol, company) values('VZ', 'AVerizon')")
#cursor.execute("insert into stock (symbol, company) values('Z', 'Zillow')")

cursor.execute("delete from stock") # delete everything from stock database

api = tradeapi.REST(config.API_KEY,config.SECRET_KEY,base_url=config.API_URL)

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

