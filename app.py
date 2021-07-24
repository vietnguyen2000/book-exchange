from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS
import sys
import json

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'vietnguyen2000.ddns.net'
app.config['MYSQL_USER'] = 'cnpmnc'
app.config['MYSQL_PASSWORD'] = 'cnpmnc'
app.config['MYSQL_DB'] = 'book_exchange'

mysql = MySQL(app)
CORS(app)


@app.route('/', methods=['GET'])
def home():
    return 'book-exchange app backend'


@app.route('/books', methods=['GET'])
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


@app.route('/book/<id>', methods=['GET'])
def getBookById(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM book NATURAL JOIN user WHERE id = ' + str(id))
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


if __name__ == "__main__":
    if 'prod' in sys.argv:
        app.run(host='0.0.0.0', port=80)
    else:
        app.run(host='localhost', port=5000, debug=True)
