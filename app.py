from flask import Flask, request
import json
import pymysql

app = Flask(__name__)

from db_account_config import db_kwargs
connection = pymysql.connect(**db_kwargs)

def query_db(title):
    # query the db and return the result
    cursor = connection.cursor()
    sql = 'SELECT * FROM Notes WHERE Title=%s'
    cursor.execute(sql, title)
    data = cursor.fetchone()
    article = {}
    if data:
        article['content'] = data[1]
    return article

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
    article = query_db(title)
    return json.dumps(article)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        # default behavior: insert table entry into table
        sql = "INSERT INTO Notes(Content, Title) Values(%s, %s)"
        # if title exists, update the content
        if query_db(title):
            sql = "UPDATE Notes SET Content=%s WHERE Title=%s"

        cursor = connection.cursor()
        cursor.execute(sql, (content, title))
        connection.commit()
        return 'OK'
    
    title = request.args['title']
    article = query_db(title)
    return json.dumps(article)

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