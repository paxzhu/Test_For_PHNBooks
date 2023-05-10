from flask import Flask, render_template, request, redirect, url_for, session
import requests
import json
from urllib.parse import quote
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
server = "http://127.0.0.1:6000"

# @app.before_request
# def loads_user():
#     if 'username' not in session:
#         return redirect(url_for('login'))

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('overview_authors'))

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        print(data)
        url = server + '/login'
        response = requests.post(url, data)
        status = response.json()
        print(status)
        if status['status'] == 'success':
            session['username'] = request.form['username']
            return redirect(url_for('overview_authors'))
        # flash(error)
    
    return render_template('login.html')


@app.route('/read/<title>')
def read(title):
    url = server + '/read?title=' + quote(title)
    print(url)
    response = requests.get(url)
    article = response.json()
    print(request.path)
    if not article:
        return "No article found for title: " + title, 404
    return render_template('read.html', title = title, content = article['content'])

@app.route('/edit/', defaults={'title':''})
@app.route('/edit/<title>', methods = ['GET', 'POST'])
def edit(title):
    if request.method == 'POST':
        data = request.form
        url = server + '/edit'
        response = requests.post(url, data)
        status = response.text
        # handle exception: database query error
        if status == 'OK':
            return redirect(url_for('read', title=request.form['title']))
    # user did not specify a title to edit, return an empty edit-page
    if not title:
        return render_template('edit.html')
    # user specified a title, update the content or create an article with the title
    url = server + '/edit?title=' + quote(title)
    response = requests.get(url)
    article = response.json()
    if not article:
        return render_template('edit.html', title=title)
    return render_template('edit.html', title=title, content=article['content'])


@app.route('/overview/articles.html')
def overview_articles():
    url = server + '/overview/articles'
    response = requests.get(url)
    titles = response.json()
    if not titles:
        return "You have not edited any articles or have not saved the edited ones.", 404
    return render_template('articles.html', titles=titles)

@app.route('/overview/')
def overview_authors():
    url = server + '/overview/authors'
    response = requests.get(url)
    authors = response.json()
    if not authors:
        return "No User"
    return render_template('authors.html', authors=authors)

if __name__ == '__main__':
    app.run(debug=True, port=8000)