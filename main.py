import sys
import os
from flask import Flask
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin

# SQLite URI compatible - checking if OS is Windows or Linux/MacOS to make sure prefix is right
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

# app and database path initialization [25]
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ics4u'
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initializing database and login manager
db = SQLAlchemy(app)
login_manager = LoginManager(app)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route("/about")
def about():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    with app.app_context():
        # creating all databases that were initialized and running web app
        db.create_all()
        
    app.run(debug=True, port=5000)