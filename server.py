from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def show_stats():
    conn = sqlite3.connect('crypto_users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_requests")
    rows = cursor.fetchall() 
    conn.close() 

    html = "<h1>Статистика запросов крипто-бота</h1>"
    html += "<table border='1' cellpadding='5'>"
    html += "<tr><th>Номер</th><th>Telegram ID</th><th>Username</th><th>Монета</th><th>Время</th></tr>"
    
    for row in rows:
        html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td></tr>"
        
    html += "</table>"
    return html

if __name__ == '__main__':
    app.run(debug=True)