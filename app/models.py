from app import db
from datetime import datetime

class MoneroTransactions(db.Model):
    __tablename__ = 'monero_transactions'
    __bind_key__ = 'norrath_wallet_monero'
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.INTEGER)
    userid = db.Column(db.INTEGER)
    confirmations = db.Column(db.INTEGER)
    confirmed = db.Column(db.INTEGER)
    txid = db.Column(db.Text)
    amount = db.Column(db.DECIMAL(20, 8))
    balance = db.Column(db.DECIMAL(20, 8))
    block = db.Column(db.INTEGER)
    created = db.Column(db.DateTime)
    address = db.Column(db.Text)
    fee = db.Column(db.DECIMAL(20, 8))
    orderid = db.Column(db.INTEGER)
    shard = db.Column(db.INTEGER)
    digital_currency = db.Column(db.INTEGER)


class MoneroTransOrphan(db.Model):
    __tablename__ = 'monero_transorphan'
    __bind_key__ = 'norrath_wallet_monero'
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    btc = db.Column(db.DECIMAL(20, 8))
    txid = db.Column(db.TEXT)


class MoneroUnconfirmed(db.Model):
    __tablename__ = 'monero_unconfirmed'
    __bind_key__ = 'norrath_wallet_monero'
    __table_args__ = {'useexisting': True}
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


class MoneroWallet(db.Model):
    __tablename__ = 'monero_wallet'
    __bind_key__ = 'norrath_wallet_monero'
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.INTEGER)
    currentbalance = db.Column(db.DECIMAL(20, 8))
    address1 = db.Column(db.TEXT)
    address1status = db.Column(db.INTEGER)
    locked = db.Column(db.INTEGER)
    shard = db.Column(db.INTEGER)
    transactioncount = db.Column(db.INTEGER)
    unconfirmed = db.Column(db.DECIMAL(20, 8))
    paymentid = db.Column(db.TEXT)


class MoneroWalletWork(db.Model):
    __tablename__ = 'monero_wallet_work'
    __bind_key__ = 'norrath_wallet_monero'
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.INTEGER)
    type = db.Column(db.INTEGER)
    amount = db.Column(db.DECIMAL(20, 8))
    sendto = db.Column(db.Text)
    paymentid = db.Column(db.Text)
    created = db.Column(db.DateTime)
    txnumber = db.Column(db.INTEGER)
    shard = db.Column(db.INTEGER)



class MoneroBlockheight(db.Model):
    __tablename__ = 'monero_blockheight'
    __bind_key__ = 'norrath_wallet_monero'
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    blockheight = db.Column(db.INTEGER)


class MoneroWalletFee(db.Model):
    __tablename__ = 'monero_walletfee'
    __bind_key__ = 'norrath_wallet_monero'
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.DECIMAL(20, 8))


class SiteFees(db.Model):
    """
    These are fees for transactions
    """
    __tablename__ = 'fees'
    __bind_key__ = 'norrath'
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    btctrade = db.Column(db.DECIMAL(20, 8))
    monero = db.Column(db.DECIMAL(20, 8))


class MoneroFeeProfit(db.Model):
    """
    The extra percent goes to wallet from withdraws

    """
    __tablename__ = 'monero_fee_holdings'
    __bind_key__ = 'norrath'
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.DECIMAL(20, 8))
    DateTime = db.Column(db.DateTime, index=True)
    total = db.Column(db.DECIMAL(20, 8))
    digital_currency = db.Column(db.INTEGER)
    shard = db.Column(db.INTEGER)


class MoneroHoldings(db.Model):
    """
    Monero in Escrow
    """
    __tablename__ = 'monero_holdings'
    __bind_key__ = 'norrath'
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.DECIMAL(20, 8))
    DateTime = db.Column(db.DateTime)
    userid = db.Column(db.INTEGER)
    total = db.Column(db.DECIMAL(20, 8))


class ProfitMonero(db.Model):
    """
    Profit Monero
    """
    __tablename__ = 'monero_profit'
    __bind_key__ = 'norrath'
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.DECIMAL(20, 8))
    order = db.Column(db.INTEGER)
    DateTime = db.Column(db.DateTime)
    total = db.Column(db.DECIMAL(20, 8))


class User(db.Model):
    __tablename__ = 'norrath_users_users'
    __table_args__ = {'useexisting': True, "schema":"norrath_users"}

    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    username = db.Column(db.TEXT)
    password_hash = db.Column(db.TEXT)
    member_since = db.Column(db.DateTime(), default=datetime.utcnow())
    bio = db.Column(db.TEXT)
    last_seen = db.Column(db.DateTime())
    country = db.Column(db.TEXT)
    currency = db.Column(db.INTEGER)

    admin = db.Column(db.INTEGER)
    admin_role = db.Column(db.INTEGER)

    btcfee = db.Column(db.DECIMAL(20, 8))
    shard_btc = db.Column(db.INTEGER)
    wallet_pin = db.Column(db.TEXT)


