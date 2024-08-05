from datetime import datetime, timedelta


API_KEY = 'PKHE04W3FWDWPAMOVWSB'
SECRET_KEY = 'mww2dno0mgcvVoAdYdik3UslklsTTFwSRout2Y60'
API_URL = 'https://paper-api.alpaca.markets'
DB_FILE = '/Users/hei/PythonProjects/TradingBot/app.db' # path to your database
# START_DATE = "2020-07-01"
# END_DATE = "2024-08-03"
LIMIT_BAR = 100
latest_date = (datetime.now() + timedelta(days=-3))
START_DATE = (latest_date + timedelta(days=-LIMIT_BAR)).strftime('%Y-%m-%d')
END_DATE = latest_date.strftime('%Y-%m-%d')

