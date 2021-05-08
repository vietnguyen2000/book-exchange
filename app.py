from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS
import json

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'sql6.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql6411044'
app.config['MYSQL_PASSWORD'] = 'KQwIHnkkbj'
app.config['MYSQL_DB'] = 'sql6411044'

mysql = MySQL(app)
CORS(app)

@app.route('/books' , methods = ['GET'])
def getAllBooks():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM book NATURAL JOIN user')
    mysql.connection.commit()
    data = cur.fetchall()
    cur.close()
    response = []
    for row in data:
        response.append({})
        response[-1]['id'] = row[0]
        response[-1]['title'] = row[1]
        response[-1]['description'] = row[2]
        response[-1]['imageURL'] = row[4]
        response[-1]['user'] = {}
        response[-1]['user']['id'] = row[3]
        response[-1]['user']['username'] = row[5]
        response[-1]['user']['name'] = row[7]

    # print(json.dumps(data))
    return json.dumps(response)

app.run(host='localhost',port = 5000, debug= True)