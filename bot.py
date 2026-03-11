import telebot
import requests
import sqlite3

conn = sqlite3.connect('crypto_users.db', check_same_thread=False)

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER,
        username TEXT,
        coin TEXT,
        request_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()
TOKEN = "8506699429:AAE6fzZTOh46xKxmBnmUEWvviYGAikdbhGM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я крипто-бот. Напиши мне тикер любой монеты (например: BTC, ETH, SOL), и я пришлю ее текущую цену.")

@bot.message_handler(func=lambda message: True)
def get_crypto_price(message):
    coin = message.text.strip().upper()
    user_id = message.from_user.id
    username = message.from_user.username
    cursor.execute("INSERT INTO user_requests (telegram_id, username, coin) VALUES (?, ?, ?)", (user_id, username, coin))
    conn.commit()
    print(f'В базу данных записано: {username} искал {coin}')
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin}USDT"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price = float(data['price'])
        bot.reply_to(message, f"Текущая цена {coin}: {price:.2f} $")
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAANKabAYjn0wFNOucnbeOpjJ8k96k8IAAlEZAAJxUvhLb6zXHKQwRGo6BA")
    else:
        bot.reply_to(message, f"Ошибка! Монета '{coin}' не найдена на бирже.")
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAMqabAVktolcz7je1RfrHhE2r8-hDUAAvsVAAIZalFIbzYfFAX-ZBk6BA")
@bot.message_handler(content_types=['sticker'])
def catch_sticker_id(message):
    print("ID этого стикера:", message.sticker.file_id)
bot.polling(none_stop=True)