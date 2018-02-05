from app import db
from app.monero_wallet_models import monero_Wallet_Work


# run once every ten minutes
def deleteoldorder():
    try:
        getwork = db.session.query(monero_Wallet_Work).filter_by(type=0).all()
        for f in getwork:
            db.session.delete(f)
            db.session.commit()
    except:
        db.session.rollback()
        pass

deleteoldorder()
