from flask import Flask
from flaskext.mysql import MySQL
from flaskext.mysql import MySQL
mysql = MySQL()
mysql.init_app(app)
app = Flask(__name__)


@app.route('/books' , method = ['POST'])
def getAllBooks():
    return 'Hello, World!'