from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

from db_account_config import db_kwargs
connection = pymysql.connect(**db_kwargs)

@app.route('/login', )
def login():
    # username = request.form['username']
    # password = request.form['password']

    # sql = "SELECT Password FROM User WHERE Username=%s"

    # cursor = connection.cursor()
    # cursor.execute(sql, (username))
    # data = cursor.fetchone()
    # connection.commit()

    # if data[0] == password:
    #     return 'status: success'
    # else:
    #     return 'status: failed'
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)