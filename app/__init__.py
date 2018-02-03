from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_BINDS, customlog
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS

def errorLogger(function, error, kindoferror, user):
    now = str(datetime.utcnow())
    #1= other
    #2 = database
    #3 = bitcoin
    #4 = bitcoin
    u = str(user)
    if kindoferror == 1:
        with open (customlog +"Error-errorlog.txt", "a") as text_file:
            text_file.write(now + '-' +str(function) + '-' + (u) + '-' + str(error) + '\n')
    if kindoferror ==2:
        with open(customlog + "Database-errorlog.txt", "a") as text_file:
            text_file.write(now + '-' +str(function) + '-' + u + '-' + str(error) + '\n')

    if kindoferror == 3:
        with open(customlog + "Bitcoin-errorlog.txt", "a") as text_file:
            text_file.write(now + '-' +str(function) + '-' + u + '-' + str(error) + '\n')

    if kindoferror == 4:
        with open(customlog + "Wallet-errorlog.txt", "a") as text_file:
            text_file.write(now + '-' +str(function) + '-' + u + '-'+ str(error) + '\n')


db = SQLAlchemy(app)
