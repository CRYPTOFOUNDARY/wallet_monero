from app import db
from app.models import \
    MoneroTransactions, MoneroWalletFee
from app.generalfunctions import floating_decimals
from sqlalchemy import func


def getlastestfee():

    """
    THis will query the last 10 withdrawls...get the average fee
    :return:
    """

    getratings = db.session.query(func.avg(MoneroTransactions.fee))
    getratings = getratings.filter(MoneroTransactions.category == 2)
    getratings = getratings.order_by(MoneroTransactions.created.desc())
    avgrate = getratings.limit(10)
    x = (avgrate[0][0])
    y = floating_decimals(x, 8)

    thefee = db.session.query(MoneroWalletFee).filter_by(id=1).first()
    thefee.amount = y
    db.session.add(thefee)
    db.session.commit()
getlastestfee()