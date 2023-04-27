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
    print(title)
    sql = "SELECT * FROM Notes WHERE Title=%s"
    cursor = connection.cursor()
    cursor.execute(sql, title)
    data = cursor.fetchone()
    article = {}
    if data:
        article['content'] = data[1]
    return json.dumps(article)

@app.route('/edit')
def edit(article):
    title = request.form['title']
    content = request.form['content']
    sql = "INSERT INTO Notes(Title, Content) Values(%s, %s)"
    cursor = connection.cursor()
    cursor.execute(sql, (title, content))
    cursor.commit()
    pass

@app.route('/overview')
def overview():
    sql = "SELECT Title FROM Notes"
    cursor = connection.cursor()
    cursor.execute(sql)
    articles = cursor.fetchall()
    titles = {article[0]:None for article in articles}
    return json.dumps(titles)  
           


if __name__ == '__main__':
    app.run(debug=True, port=6000)