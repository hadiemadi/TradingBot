import sqlite3, config


connection = sqlite3.connect(config.DB_FILE)    #if the flie does not exist it creates one database

cursor = connection.cursor()

cursor.execute("""
    DROP TABLE stock_price

""")

cursor.execute("""
    DROP TABLE stock

""")

connection.commit()