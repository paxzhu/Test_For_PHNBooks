from flask import Flask, request
import json
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
    if data and data[0] == password:
        return json.dumps({'status':'success'})
    return json.dumps({'status':'failed'})

@app.route('/read')
def read():
    title = request.args['title']
    
    sql = "SELECT * FROM Notes WHERE Title=%s"
    cursor = connection.cursor()
    cursor.execute(sql, title)
    article = cursor.fetchone()
    if not article:
        return "No article found for title: " + title, 404
    # return article[1]
    title, content = article
    return json.dumps({'title':title, 'content':content})

@app.route('/edit')
def edit(article):

    pass

@app.route('/overview')
def overview():
    pass


if __name__ == '__main__':
    app.run(debug=True, port=6000)