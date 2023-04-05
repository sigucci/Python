import time
import pandas as pd
from binance.client import Client

client = Client(api_key='key', api_secret='s.key')

previous_price = float(client.futures_symbol_ticker(symbol='ETHUSDT')['price'])

while True:

    current_price = float(client.futures_symbol_ticker(symbol='ETHUSDT')['price'])

    percentage_change = (current_price - previous_price) / previous_price * 100

    if abs(percentage_change) >= 1:
        print(f"Цена ETHUSDT изменилась на {percentage_change:.2f}% за последний час.")

    previous_price = current_price

    time.sleep(1)
