import pandas as pd
import sqlalchemy
from binance import *
from multiprocessing.connection import Client
from sqlalchemy import *

client = Client('api-key', 'api-secret')

bsm = BinanceSocketManager(client)

socket = bsm.trade_socket('BTCUSDT')


def createDataFrame(msg):
    df = pd.DataFrame([msg])
    df = df.loc[:, ['s', 'E', 'p']]
    df.columns = ['symbol', 'Time', 'Price']
    df.Price = df.Price.astype(float)
    df.Time = pd.to_datetime(df.Time, unit='ms')
    return df


# createDataFrame(msg)
engine = sqlalchemy.create_engine('sqlite:///BTCUSDstream.db')

while True:
    await socket.__aenter__()
    msg = await socket.recv()
    frame = createDataFrame(msg)
    frame.to_sql('BTCUSDT', engine, if_exists='append', index=False)
    print(frame)

# createDataFrame(msg)

# engine = sqlalchemy.create_engine('sqlite:///BTCUSDstream.db')
