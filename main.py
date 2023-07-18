import sys
import os
from flask import Flask, render_template, url_for, request, flash, redirect, jsonify, session
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# SQLite URI compatible - checking if OS is Windows or Linux/MacOS to make sure prefix is right
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

# app and database path initialization [25]
app = Flask(__name__)
app.config['SECRET_KEY'] = 'emma'
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'database.db')
print(app.config['SQLALCHEMY_DATABASE_URI'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
        db.create_all()
    app.run(debug=True, port=5000)