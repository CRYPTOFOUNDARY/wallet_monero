from datetime import datetime
from app.monero_wallet_models import MoneroTransactions
from app import db


# this function will move the coin from holdings back to vendor.  This is for vendor verification
def monero_addtransaction(category, amount, userid, txid, shard, block, balance):
    try:
        now = datetime.utcnow()
        txidd = str(txid)
        theblock = int(block)

        trans = MoneroTransactions(
            category=category,
            userid=userid,
            confirmations=0,
            confirmed=1,
            txid=txidd,
            amount=amount,
            balance=balance,
            block=theblock,
            created=now,
            address='',
            fee=0,
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