from flask import Flask, render_template, request, redirect, url_for
import requests
import json
from urllib.parse import quote
app = Flask(__name__)
server = "http://127.0.0.1:6000"
@app.route('/')
def index():
    return render_template('/index.html')

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
            return redirect('/NoteBook.html')
        return status['status']
    
    return render_template('login.html')

@app.route('/read/<title>')
def read(title):
    title = 'What is a framework?'
    url = server + '/read?title=' + title
    print(url)
    response = requests.get(url)
    article = response.json()
    print(request.path)
    if not article:
        return "No article found for title: " + title, 404
    return render_template('read.html', title = title, content = article['content'])

@app.route('/edit/<title>', methods = ['GET', 'POST'])
def edit(title):
    if request.method == 'POST':
        data = request.form
        url = server + '/edit'
        print(data)
        response = requests.post(url, data)
        status = response.text
        if status == 'OK':
            return redirect(url_for('read', title=request.form['title']))
    return render_template('edit.html')

@app.route('/overview.html')
def overview():
    url = server + '/overview'
    response = requests.get(url)
    titles = response.json()
    if not titles:
        return "You have not edited any articles or have not saved the edited ones.", 404
    return render_template('overview.html', titles=titles)


if __name__ == '__main__':
    app.run(debug=True, port=8000)