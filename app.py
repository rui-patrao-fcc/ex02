from flask import Flask, render_template, request
import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    conn = pymysql.connect(
        host=os.getenv("MYSQL_HOST"),
        port=int(os.getenv("MYSQL_PORT")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
        )
    
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    cursor.execute("SELECT id, numero, nome from aluno order by nome ASC;")
    alunos=cursor.fetchall()

    return render_template('index.html',dados=alunos)

if __name__ == "__main__":
    app.run(debug=True)