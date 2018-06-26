from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_BINDS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS



db = SQLAlchemy(app)
