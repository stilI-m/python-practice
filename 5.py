import requests
print("Введите монету (Например: BTC, ETH, DOGE, SOL)")
print("Для выхода напишите: 'exit'")
while True:
    coin = input('Какую монету ищем? ').strip().upper()
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin}USDT"
    if coin == 'EXIT':
        print("Пока!")
        break
    response = requests.get(url)
    if response.status_code == 200:
        crypto_data = response.json()
        price = float(crypto_data['price'])
        print(f'Стоимсоть {coin}: {price:.2f} $')
    else:
        print('Такой валюты нет или ввод неверен')
    
    