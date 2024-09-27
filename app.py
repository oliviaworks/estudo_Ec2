from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# Função para obter a conexão com o banco de dados
def get_db_connection():
    conn = psycopg2.connect(
        host="dpg-crqknc88fa8c7393rv4g-a.oregon-postgres.render.com", 
        database="flaskdb_wrds", 
        user="user", 
        password="BNGfrfKhIs3ZJGKuTI7vM2a65qQoNtvF"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, name, email FROM users')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
