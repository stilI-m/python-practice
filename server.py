from flask import Flask, request, session, redirect, url_for
from werkzeug.security import check_password_hash
import sqlite3

app = Flask(__name__)

app.secret_key = 'super_secret_key_for_our_crypto_bot'

ADMIN_HASH = "scrypt:32768:8:1$mx2oQD5HWzhzuL2C$c2d97de4f83ab7bc193749e5b29cd665e4e96393c272183222c111fac74712f964d75fcda1e587a2a2fb60d1571e772fc16663a1335a94ea13c6ebff7a535b8c"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password_attempt = request.form.get('password')
        
        if check_password_hash(ADMIN_HASH, password_attempt):
            session['logged_in'] = True  
            return redirect(url_for('show_stats'))
        else:
            return "<h1> Неверный пароль!</h1><a href='/login'>Попробовать снова</a>"
            
    html_form = '''
        <h1>Вход для администратора </h1>
        <form method="post">
            <input type="password" name="password" placeholder="Введите пароль">
            <button type="submit">Войти</button>
        </form>
    '''
    return html_form

@app.route('/')
def show_stats():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    conn = sqlite3.connect('crypto_users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_requests")
    rows = cursor.fetchall() 
    conn.close()

    html = "<h1>Статистика запросов крипто-бота </h1>"
    html += "<p><a href='/logout'>🚪 Выйти из панели</a></p>" 
    html += "<table border='1' cellpadding='5'>"
    html += "<tr><th>Номер</th><th>Telegram ID</th><th>Username</th><th>Монета</th><th>Время</th></tr>"
    
    for row in rows:
        html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td></tr>"
        
    html += "</table>"
    return html

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)