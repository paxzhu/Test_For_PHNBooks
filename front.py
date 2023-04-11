from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi~'

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(port=8000)