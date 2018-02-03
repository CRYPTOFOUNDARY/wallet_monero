from app import db
from datetime import datetime


class AgoraFee(db.Model):
    __tablename__ = 'fees'
    __bind_key__ = 'db1'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    btctrade = db.Column(db.DECIMAL(20, 8))
    btc_cash_trade = db.Column(db.DECIMAL(20, 8))
    digtrade = db.Column(db.DECIMAL(20, 8))
    itempurchase = db.Column(db.DECIMAL(20, 8))


class Agorafeeholdings(db.Model):
    __tablename__ = 'account_fee_holdings'
    __bind_key__ = 'db1'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.DECIMAL(20, 8))
    timestamp = db.Column(db.DateTime, index=True)
    total = db.Column(db.DECIMAL(20, 8))


class Agoraprofit(db.Model):
    __tablename__ = 'account_profit'
    __bind_key__ = 'db1'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.DECIMAL(20, 8))
    order = db.Column(db.INTEGER)
    timestamp = db.Column(db.DateTime, index=True)
    total = db.Column(db.DECIMAL(20, 8))


class Notifications(db.Model):
    __tablename__ = 'notifications'
    __bind_key__ = 'db1'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.INTEGER)
    username = db.Column(db.TEXT)
    userid = db.Column(db.INTEGER)
    timestamp = db.Column(db.DateTime)
    salenumber = db.Column(db.INTEGER)
    bitcoin = db.Column(db.DECIMAL(20, 8))
    read = db.Column(db.INTEGER)


class User(db.Model):
    __tablename__ = 'users'
    __bind_key__ = 'db1'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.Text, unique=True, index=True)
    password_hash = db.Column(db.Text)
    member_since = db.Column(db.DateTime(), default=datetime.utcnow())
    email = db.Column(db.Text)
    wallet_pin = db.Column(db.Text)
    profileimage = db.Column(db.Text)
    stringuserdir = db.Column(db.Text)
    bio = db.Column(db.TEXT)
    country = db.Column(db.Text)
    currency = db.Column(db.INTEGER)
    vendor_account = db.Column(db.INTEGER)
    selling_from = db.Column(db.Text)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow())
    admin = db.Column(db.INTEGER)
    admin_role = db.Column(db.INTEGER)
    dispute = db.Column(db.INTEGER)
    fails = db.Column(db.INTEGER)
    locked = db.Column(db.INTEGER)
    vacation = db.Column(db.INTEGER)
    shopping_timer = db.Column(db.DATETIME)
    lasttraded_timer = db.Column(db.DATETIME)
    shard = db.Column(db.INTEGER)




