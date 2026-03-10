import requests

url = "https://official-joke-api.appspot.com/random_joke"

print("Стучимся на сервер...")

response = requests.get(url)
if response.status_code == 200:

    joke_data = response.json()
    print("\nШутка найдена!")
    print("Вопрос:", joke_data["setup"])
    print("Ответ:", joke_data["punchline"])
    
else:
    print("Ой, сервер сломался. Код ошибки:", response.status_code)