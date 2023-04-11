import pymysql

from db_account_config import db_kwargs
connection = pymysql.connect(**db_kwargs)
cursor = connection.cursor()

sql = "INSERT INTO User (Username, Name, Password)  VALUES (%s, %s, %s);"
values = ('Jack', 'tokyo', '123456')
cursor.execute(sql, values)

sql = "SELECT * FROM User"
cursor.execute(sql)

data = cursor.fetchall()

connection.commit()

print(data)



