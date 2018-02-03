from app import db
from app import errorLogger
from datetime import datetime
from app.models import btccash_Wallet_Work,  User


# type 1: wallet creation
# type 2: send bitcoin offsite
# type 3: get new address


##THIS function creates the wallet and puts its first address there
def getnewaddress(userid):
    user = db.session.query(User).filter(User.id == userid).first()
    timestamp = datetime.utcnow()
    type_transaction = 3
    try:
        wallet = btccash_Wallet_Work(
            userid=userid,
            type=type_transaction,
            amount =0,
            sendto=0,
            comment=0,
            created=timestamp,
            txtcomment='',
            shard=user.shard
        )
        db.session.add(wallet)
        db.session.commit()

    except Exception as e:
        errorLogger(function='createWallet', error=e, kindoferror=4, user=userid)
        db.session.rollback()

