import requests
url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
response = requests.get(url)
print("Узнаем курс на Binance...")
if response.status_code == 200:
    crypto_data = response.json()
    float_price = float(crypto_data['price'])
    print(f"Стоимость {crypto_data['symbol']} на текущий момент: {float_price:.2f}")
else:
    print(f"Не удалось связаться с биржей. Код: {response.status_code} $")