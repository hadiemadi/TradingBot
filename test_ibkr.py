from ib_insync import *

ib = IB()


ib.connect( port = 7496, clientId=1)



# stock = Contract(secType= 'Stock', )


stock = Stock('AMD', 'SMART', 'USD')

ib.reqMktData(stock, '', False,False)


bars = ib.reqHistoricalData(
    stock, endDateTime='', durationStr='30 D',
    barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=False)

# convert to pandas dataframe (pandas needs to be installed):
# df = util.df(bars)
# print(df)

print(bars)