import telebot
import requests
TOKEN = "8506699429:AAE6fzZTOh46xKxmBnmUEWvviYGAikdbhGM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я крипто-бот. Напиши мне тикер любой монеты (например: BTC, ETH, SOL), и я пришлю ее текущую цену.")

@bot.message_handler(func=lambda message: True)
def get_crypto_price(message):
    coin = message.text.strip().upper()
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin}USDT"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price = float(data['price'])
        bot.reply_to(message, f"Текущая цена {coin}: {price:.2f} $")
    else:
        bot.reply_to(message, f"Ошибка! Монета '{coin}' не найдена на бирже.")

bot.polling(none_stop=True)