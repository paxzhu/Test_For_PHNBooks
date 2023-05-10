from flask import Flask, request
import json
import pymysql

app = Flask(__name__)

from db_account_config import db_kwargs
connection = pymysql.connect(**db_kwargs)

def get_article_or_empty(title):
    # query the db and return the result
    cursor = connection.cursor()
    sql = 'SELECT * FROM Article WHERE Title=%s'
    cursor.execute(sql, title)
    data = cursor.fetchone()
    article = {}
    if data:
        article['content'] = data[2]
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
    article = get_article_or_empty(title)
    return json.dumps(article)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        # default behavior: insert table entry into table
        sql = "INSERT INTO Article(Content, Title) Values(%s, %s)"
        # if title exists, update the content
        if get_article_or_empty(title):
            sql = "UPDATE Article SET Content=%s WHERE Title=%s"

        cursor = connection.cursor()
        cursor.execute(sql, (content, title))
        connection.commit()
        return 'OK'
    
    title = request.args['title']
    article = get_article_or_empty(title)
    return json.dumps(article)

@app.route('/overview/articles')
def overview_articles():
    sql = "SELECT Title FROM Article"
    cursor = connection.cursor()
    cursor.execute(sql)
    articles = cursor.fetchall()
    # print(articles)
    titles = {article[0]:None for article in articles}
    
    return json.dumps(titles)  

@app.route('/overview/authors')
def overview_authors():
    sql = """SELECT Author.author_id, Author.Username, COUNT(Article.article_id) AS article_count
            FROM User as Author
            LEFT JOIN Article ON Author.author_id = Article.author_id
            GROUP BY Author.author_id, Author.Username;"""
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    authors = {}
    if data:
        authors = { id:(name, works) for id, name, works in data}
    return json.dumps(authors)

if __name__ == '__main__':
    app.run(debug=True, port=6000)