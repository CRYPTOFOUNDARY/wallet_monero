from datetime import datetime
from app.models import MoneroTransactions
from app import db


def monero_addtransaction(category, amount, userid, txid, shard, block, balance, confirmed, fee, address):
    """
    # this function will move the coin from holdings back to vendor.  This is for vendor verification
    :param category:
    :param amount:
    :param userid:
    :param txid:
    :param shard:
    :param block:
    :param balance:
    :param confirmed:
    :param fee:
    :param address:
    :return:
    """
    try:
        now = datetime.utcnow()
        txidd = str(txid)
        theblock = int(block)

        trans = MoneroTransactions(
            category=category,
            userid=userid,
            confirmations=0,
            confirmed=confirmed,
            txid=txidd,
            amount=amount,
            balance=balance,
            block=theblock,
            created=now,
            address=address,
            fee=fee,
            orderid=0,
            shard=shard,
            digital_currency=4,

        )
        db.session.add(trans)
        db.session.commit()

    except Exception as e:
        print("transaction error")
        print(str(e))
        db.session.rollback()