from flask import Flask, render_template, request
import pymysql
from db_account_config import db_kwargs

app = Flask(__name__)
connection = pymysql.connect(**db_kwargs)

@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    sql = "SELECT Password FROM User WHERE Username=%s"

    cursor = connection.cursor()
    cursor.execute(sql, (username))
    data = cursor.fetchone()
    connection.commit()
    status = 'failed'
    if data[0] == password:
        status = 'success'
    return render_template('greeting.html',status = status)

if __name__ == "__main__":
    app.run(port=8000)
