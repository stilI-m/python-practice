import requests

# 1. Адрес в интернете, куда мы будем стучаться (сервер с шутками)
url = "https://official-joke-api.appspot.com/random_joke"

print("Стучимся на сервер...")

# 2. Делаем GET-запрос (просим сервер отдать данные)
response = requests.get(url)

# 3. Проверяем, всё ли прошло хорошо (код 200 означает "ОК")
if response.status_code == 200:
    
    # 4. Сервер отдает данные в формате JSON. 
    # Эта команда превращает их в удобный питоновский словарь
    joke_data = response.json()
    
    # 5. Вытаскиваем нужные поля по ключам из словаря
    print("\nШутка найдена!")
    print("Вопрос:", joke_data["setup"])
    print("Ответ:", joke_data["punchline"])
    
else:
    print("Ой, сервер сломался. Код ошибки:", response.status_code)