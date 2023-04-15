from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

from db_account_config import db_kwargs
connection = pymysql.connect(**db_kwargs)

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    sql = "SELECT Password FROM User WHERE Username=%s"

    cursor = connection.cursor()
    cursor.execute(sql, (username))
    data = cursor.fetchone()
    connection.commit()
    if data and data[0] == password:
        return 'success'
    return 'failed'

if __name__ == '__main__':
    app.run(debug=True, port=6000)