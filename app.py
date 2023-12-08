from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///padaria.sqlite3'
app.config['SECRET_KEY'] = 'padaria321'

from views import *

if __name__ == '__main__':
    app.run(debug=True)
