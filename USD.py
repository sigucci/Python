import time
import pandas as pd
import requests

previous_price = float(requests.get('https://finance.google.com/finance?q=USDRUB').text.split('ref_')[1].split('>')[1].split('<')[0])

while True:
 
    current_price = float(requests.get('https://finance.google.com/finance?q=USDRUB').text.split('ref_')[1].split('>')[1].split('<')[0])

 
    percentage_change = (current_price - previous_price) / previous_price * 100

    if abs(percentage_change) >= 2:
        print(f"Цена доллара к рублю изменилась на {percentage_change:.2f}% за последний час.")

    previous_price = current_price

    time.sleep(1)

