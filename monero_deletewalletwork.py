from app import db
from app.models import MoneroWalletWork


# run once every ten minutes
def deleteoldorder():
    try:
        getwork = db.session.query(MoneroWalletWork).filter_by(type=0).all()
        for f in getwork:
            db.session.delete(f)
            db.session.commit()
    except Exception as e:
        print(str(e))
        db.session.rollback()
        pass


deleteoldorder()
