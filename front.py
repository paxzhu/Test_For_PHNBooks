from flask import Flask, render_template, request, redirect
import requests
app = Flask(__name__)
server = "http://127.0.0.1:6000"
@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        url = server + '/login'
        response = requests.post(url, data)
        status = response.content
        return status
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)