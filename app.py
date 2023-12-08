from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///padaria.sqlite3'
app.config['SECRET_KEY'] = 'padaria321'

login_manager = LoginManager(app)

db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
