# coding=utf-8
from app import db


class MoneroTransactions(db.Model):
    __tablename__ = 'monero_transactions'
    __bind_key__ = 'monero_wallet'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.INTEGER)
    userid = db.Column(db.INTEGER)
    confirmations = db.Column(db.INTEGER)
    txid = db.Column(db.Text)
    amount = db.Column(db.INTEGER)
    balance = db.Column(db.INTEGER)
    block = db.Column(db.INTEGER)
    created = db.Column(db.DATETIME)
    address = db.Column(db.Text)
    fee = db.Column(db.INTEGER)
    orderid = db.Column(db.INTEGER)
    shard = db.Column(db.INTEGER)
    digital_currency = db.Column(db.INTEGER)
    confirmed = db.Column(db.INTEGER)


class monero_transOrphan(db.Model):
    __tablename__ = 'monero_transorphan'
    __bind_key__ = 'monero_wallet'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    btc = db.Column(db.DECIMAL(20, 8))
    btcaddress = db.Column(db.TEXT)
    txid = db.Column(db.TEXT)


class monero_unconfirmed(db.Model):
    __tablename__ = 'monero_unconfirmed'
    __bind_key__ = 'monero_wallet'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.INTEGER)

    unconfirmed1 = db.Column(db.DECIMAL(20, 8))
    unconfirmed2 = db.Column(db.DECIMAL(20, 8))
    unconfirmed3 = db.Column(db.DECIMAL(20, 8))
    unconfirmed4 = db.Column(db.DECIMAL(20, 8))
    unconfirmed5 = db.Column(db.DECIMAL(20, 8))
    unconfirmed6 = db.Column(db.DECIMAL(20, 8))
    unconfirmed7 = db.Column(db.DECIMAL(20, 8))
    unconfirmed8 = db.Column(db.DECIMAL(20, 8))
    unconfirmed9 = db.Column(db.DECIMAL(20, 8))
    unconfirmed10 = db.Column(db.DECIMAL(20, 8))

    txid1 = db.Column(db.TEXT)
    txid2 = db.Column(db.TEXT)
    txid3 = db.Column(db.TEXT)
    txid4 = db.Column(db.TEXT)
    txid5 = db.Column(db.TEXT)
    txid6 = db.Column(db.TEXT)
    txid7 = db.Column(db.TEXT)
    txid8 = db.Column(db.TEXT)
    txid9 = db.Column(db.TEXT)
    txid10 = db.Column(db.TEXT)



class monero_Wallet(db.Model):
    __tablename__ = 'monero_wallet'
    __bind_key__ = 'monero_wallet'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.INTEGER)
    currentbalance = db.Column(db.INTEGER)
    address1 = db.Column(db.TEXT)
    address1status = db.Column(db.INTEGER)
    locked = db.Column(db.INTEGER)
    shard = db.Column(db.INTEGER)
    transactioncount = db.Column(db.INTEGER)
    unconfirmed = db.Column(db.DECIMAL(20, 8))
    paymentid = db.Column(db.TEXT)

class monero_Wallet_Work(db.Model):
    __tablename__ = 'monero_wallet_work'
    __bind_key__ = 'monero_wallet'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.INTEGER)
    type = db.Column(db.INTEGER)
    amount = db.Column(db.DECIMAL(20, 8))
    sendto = db.Column(db.Text)
    comment = db.Column(db.Text)
    created = db.Column(db.DATETIME)
    txtcomment = db.Column(db.Text)
    shard = db.Column(db.INTEGER)


class monero_walletFee(db.Model):
    __tablename__ = 'monero_walletfee'
    __bind_key__ = 'monero_wallet'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.DECIMAL(20, 8))


class MoneroWalletAddresses(db.Model):
    __tablename__ = 'moneroaddresses'
    __bind_key__ = 'monero_wallet'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.TEXT)
    shard = db.Column(db.INTEGER)
    userid = db.Column(db.INTEGER)
    status = db.Column(db.INTEGER)


class MoneroBlockheight(db.Model):
    __tablename__ = 'monero_blockheight'
    __bind_key__ = 'monero_wallet'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    blockheight = db.Column(db.INTEGER)
    lastcheckedheight = db.Column(db.INTEGER)
