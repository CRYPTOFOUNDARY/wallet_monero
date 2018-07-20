import requests
from requests.auth import HTTPDigestAuth
import json
from walletconfig import rpcpassword, rpcusername, shard, url
from app import db
from app.monero_wallet_models import \
    monero_Wallet,\
    MoneroBlockheight,\
    MoneroTransactions,\
    monero_unconfirmed,\
    monero_transOrphan

from monero_addtotransactions import monero_addtransaction
from decimal import Decimal
from app.generalfunctions import floating_decimals


# standard json header
headers = {'content-type': 'application/json'}




def addtounconfirmed(amount, userid, txid):
    """
    # this function can track multiple incomming unconfirmed amounts
    :param amount:
    :param userid:
    :param txid:
    :return:
    """
    unconfirmedtable = db.session.query(monero_unconfirmed).filter_by(userid=userid).first()
    x = floating_decimals(amount, 8)
    if unconfirmedtable is None:

        newunconfirmed = monero_unconfirmed(
                                    userid=userid,
                                    unconfirmed1=0,
                                    unconfirmed2=0,
                                    unconfirmed3=0,
                                    unconfirmed4=0,
                                    unconfirmed5=0,
                                    unconfirmed6=0,
                                    unconfirmed7=0,
                                    unconfirmed8=0,
                                    unconfirmed9=0,
                                    unconfirmed10=0,
                                    )
        db.session.add(newunconfirmed)
    else:
        try:
            if unconfirmedtable.unconfirmed1 == 0:

                unconfirmedtable.unconfirmed1 = x
                unconfirmedtable.txid1 = txid
                db.session.add(unconfirmedtable)
                db.session.commit()

            elif unconfirmedtable.unconfirmed2 == 0:
                unconfirmedtable.txid2 = txid
                unconfirmedtable.unconfirmed2 = x
                db.session.add(unconfirmedtable)
                db.session.commit()

            elif unconfirmedtable.unconfirmed3 == 0:
                unconfirmedtable.txid3 = txid
                unconfirmedtable.unconfirmed3 = x
                db.session.add(unconfirmedtable)
                db.session.commit()

            elif unconfirmedtable.unconfirmed4 == 0:
                unconfirmedtable.txid4 = txid
                unconfirmedtable.unconfirmed4 = x
                db.session.add(unconfirmedtable)
                db.session.commit()

            elif unconfirmedtable.unconfirmed5 == 0:
                unconfirmedtable.unconfirmed5 = x
                unconfirmedtable.txid5 = txid
                db.session.add(unconfirmedtable)
                db.session.commit()

            elif unconfirmedtable.unconfirmed6 == 0:
                unconfirmedtable.unconfirmed6 = x
                unconfirmedtable.txid6 = txid
                db.session.add(unconfirmedtable)
                db.session.commit()

            elif unconfirmedtable.unconfirmed7 == 0:
                unconfirmedtable.unconfirmed7 = x
                unconfirmedtable.txid7 = txid
                db.session.add(unconfirmedtable)
                db.session.commit()

            elif unconfirmedtable.unconfirmed8 == 0:
                unconfirmedtable.unconfirmed8 = x
                unconfirmedtable.txid8 = txid
                db.session.add(unconfirmedtable)
                db.session.commit()

            elif unconfirmedtable.unconfirmed9 == 0:
                unconfirmedtable.unconfirmed9 = x
                unconfirmedtable.txid9 = txid
                db.session.add(unconfirmedtable)
                db.session.commit()

            elif unconfirmedtable.unconfirmed10 == 0:
                unconfirmedtable.unconfirmed10 = x
                unconfirmedtable.txid10 = txid
                db.session.add(unconfirmedtable)
                db.session.commit()
                
            else:
                pass
        except Exception as e:
            print(str(e))



def removeunconfirmed(userid, txid):
    """
    # this function removes the amount from unconfirmed
    :param userid:
    :param txid:
    :return:
    """

    try:
        unconfirmeddelete = db.session.query(monero_unconfirmed).filter_by(userid=userid).first()
        if unconfirmeddelete.txid1 == txid:
            unconfirmeddelete.txid1 = ''
            unconfirmeddelete.unconfirmed1 = 0
            db.session.add(monero_unconfirmed)
            db.session.commit()

        elif unconfirmeddelete.txid2 == txid:
            unconfirmeddelete.txid2 = ''
            unconfirmeddelete.unconfirmed2 = 0
            db.session.add(monero_unconfirmed)
            db.session.commit()

        elif unconfirmeddelete.txid3 == txid:
            unconfirmeddelete.txid3 = ''
            unconfirmeddelete.unconfirmed3 = 0
            db.session.add(monero_unconfirmed)
            db.session.commit()

        elif unconfirmeddelete.txid4 == txid:
            unconfirmeddelete.txid4 = ''
            unconfirmeddelete.unconfirmed4 = 0
            db.session.add(monero_unconfirmed)
            db.session.commit()

        elif unconfirmeddelete.txid5 == txid:
            unconfirmeddelete.txid5 = ''
            unconfirmeddelete.unconfirmed5 = 0
            db.session.add(monero_unconfirmed)
            db.session.commit()

        elif unconfirmeddelete.txid6 == txid:
            unconfirmeddelete.txid6 = ''
            unconfirmeddelete.unconfirmed6 = 0
            db.session.add(monero_unconfirmed)
            db.session.commit()

        elif unconfirmeddelete.txid7 == txid:
            unconfirmeddelete.txid7 = ''
            unconfirmeddelete.unconfirmed7 = 0
            db.session.add(monero_unconfirmed)
            db.session.commit()

        elif unconfirmeddelete.txid8 == txid:
            unconfirmeddelete.txid8 = ''
            unconfirmeddelete.unconfirmed8 = 0
            db.session.add(monero_unconfirmed)
            db.session.commit()

        elif unconfirmeddelete.txid9 == txid:
            unconfirmeddelete.txid9 = ''
            unconfirmeddelete.unconfirmed9 = 0
            db.session.add(monero_unconfirmed)
            db.session.commit()

        elif unconfirmeddelete.txid10 == txid:
            unconfirmeddelete.txid10 = ''
            unconfirmeddelete.unconfirmed10 = 0
            db.session.add(monero_unconfirmed)
            db.session.commit()
        else:
            pass
    except Exception as e:
        print(str(e))



def getbalanceUnconfirmed(userid):
    """
    # this function removes the amount from unconfirmed
    :param userid:
    :return:
    """
    unconfirmeddelete = db.session.query(monero_unconfirmed).filter_by(userid=userid).first()
    
    a = Decimal(unconfirmeddelete.unconfirmed1)
    b = Decimal(unconfirmeddelete.unconfirmed2)
    c = Decimal(unconfirmeddelete.unconfirmed3)
    d = Decimal(unconfirmeddelete.unconfirmed4)
    e = Decimal(unconfirmeddelete.unconfirmed5)
    f = Decimal(unconfirmeddelete.unconfirmed6)
    g = Decimal(unconfirmeddelete.unconfirmed7)
    h = Decimal(unconfirmeddelete.unconfirmed8)
    i = Decimal(unconfirmeddelete.unconfirmed9)
    j = Decimal(unconfirmeddelete.unconfirmed10)

    total = a + b + c + d + e + f + g + h + i + j

    wallet = monero_Wallet.query.filter_by(userid=userid).first()
    totalchopped = floating_decimals(total, 8)
    wallet.unconfirmed = totalchopped
    db.session.add(wallet)
    db.session.commit()


def checkincomming():
    # getblockinfo
    try:
        lastblockheight = db.session.query(MoneroBlockheight).filter_by(id=1).first()
        lastchecked = lastblockheight.lastcheckedheight
        rpc_input = {
            "method": "get_bulk_payments",
            "params": {"payment_ids": True,
                       "min_block_height": lastchecked}
        }

        # add standard rpc values
        rpc_input.update({"jsonrpc": "2.0", "id": "0"})

        # execute the rpc request
        response = requests.post(
            url,
            data=json.dumps(rpc_input),
            headers=headers,
            auth=HTTPDigestAuth(rpcusername, rpcpassword))

        response_json = response.json()

        if "result" in response_json:
            if "payments" in response_json["result"]:
                for incpayments in response_json["result"]["payments"]:
                    userpaymentid = incpayments['payment_id']

                    blockheight = incpayments['block_height']
                    hashid = incpayments['tx_hash']
                    amount = Decimal(get_money(str(incpayments['amount'])))
                    # get user with that payment id
                    getuserswallet = db.session.query(monero_Wallet).filter_by(paymentid=userpaymentid).first()
                    #print(json.dumps(response.json(), indent=4))
                    if getuserswallet is not None:

                        # see if already in db
                        gettransaction = db.session.query(MoneroTransactions).filter_by(txid=hashid).first()
                        if gettransaction is None:
                            print("found new transaction:", str(hashid))

                            # add amount to current balance
                            currentbalance = getuserswallet.currentbalance
                            newbalance = Decimal(currentbalance) + Decimal(amount)
                            getuserswallet.currentbalance = newbalance
                            db.session.add(getuserswallet)
                            db.session.commit()

                            # add to transactions
                            monero_addtransaction(category=3,
                                                  amount=amount,
                                                  userid=getuserswallet.userid,
                                                  txid=hashid,
                                                  shard=shard,
                                                  block=blockheight,
                                                  balance=newbalance,
                                                  confirmed=0,
                                                  fee=0,
                                                  address=''
                                                  )

                            # add total of incomming
                            addtounconfirmed(amount=amount,
                                             userid=getuserswallet.userid,
                                             txid=hashid
                                             )

                            getbalanceUnconfirmed(getuserswallet.userid)

                            if int(lastblockheight.blockheight) < int(blockheight):
                                lastblockheight.blockheight = int(blockheight)
                                db.session.add(lastblockheight)
                                db.session.commit()
                            else:
                                pass


                        else:
                            # check to see how many confirmations
                            currentblockheight = lastblockheight.blockheight
                            if gettransaction.confirmed == 0:
                                howmanyconfirmations = currentblockheight - gettransaction.block
                                if howmanyconfirmations <= 15:
                                    gettransaction.confirmations = howmanyconfirmations
                                    db.session.add(gettransaction)
                                    db.session.commit()
                                    # add to unconfirmed
                                    getbalanceUnconfirmed(getuserswallet.userid)

                                else:
                                    removeunconfirmed(userid=getuserswallet.userid, txid=hashid)

                                    gettransaction.confirmations = 16
                                    gettransaction.confirmed = 1
                                    db.session.add(gettransaction)

                                    lastblockheight.lastcheckedheight = blockheight
                                    db.session.add(lastblockheight)
                                    db.session.commit()

                                    getbalanceUnconfirmed(userid=getuserswallet.userid)



                            else:
                                # already confirmaed pass
                                pass

                    else:
                        y = db.session.query(monero_unconfirmed).filter_by(txid=hashid).first()
                        if y:
                            pass
                        else:
                            # orphan transaction..put in background.
                            # they prolly sent no payment id ..
                            trans = monero_transOrphan(
                                btc=amount,
                                txid=hashid,
                            )
                            db.session.add(trans)
                            db.session.commit()
    except Exception as e:
        print(str(e))
        print("checkincomming error")




def get_money(amount):
    try:
        movetwelvedecimals = 12

        s = amount

        if len(s) < movetwelvedecimals + 1:
            # add some trailing zeros, if needed, to have constant width
            s = '0' * (movetwelvedecimals + 1 - len(s)) + s

        idx = len(s) - movetwelvedecimals

        s = s[0:idx] + "." + s[idx:]

        return s
    except Exception as e:
        print(str(e))
        print("get_money error")


checkincomming()


