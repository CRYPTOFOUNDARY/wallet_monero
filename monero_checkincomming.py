import requests
from requests.auth import HTTPDigestAuth
import json
from walletconfig import rpcpassword, rpcusername, shard
from app import db
from app.monero_wallet_models import \
    monero_Wallet,\
    MoneroBlockheight,\
    MoneroTransactions

from monero_addtotransactions import monero_addtransaction
from decimal import Decimal

# simple wallet is running on the localhost and port of 18082
url = "http://test:test@localhost:28080/json_rpc"

# standard json header
headers = {'content-type': 'application/json'}


def checkincomming():


    # getblockinfo
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
    print(json.dumps(response.json(), indent=4))

    if "result" in response_json:
        if "payments" in response_json["result"]:
            for incpayments in response_json["result"]["payments"]:
                userpaymentid = incpayments['payment_id']

                blockheight = incpayments['block_height']
                hashid = incpayments['tx_hash']
                amount = Decimal(get_money(str(incpayments['amount'])))
                # get user with that payment id
                getuserswallet = db.session.query(monero_Wallet).filter_by(paymentid=userpaymentid).first()
                if getuserswallet is not None:

                    # see if already in db
                    gettransaction = db.session.query(MoneroTransactions).filter_by(txid=hashid).first()
                    if gettransaction is None:

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
                            else:
                                gettransaction.confirmations = 16
                                gettransaction.confirmed = 1
                                db.session.add(gettransaction)
                                db.session.commit()

                        else:
                            # already confirmaed pass
                            pass

                else:
                    #user has no wallet..future update
                   pass

def get_money(amount):
    movetwelvedecimals = 12

    s = amount

    if len(s) < movetwelvedecimals + 1:
        # add some trailing zeros, if needed, to have constant width
        s = '0' * (movetwelvedecimals + 1 - len(s)) + s

    idx = len(s) - movetwelvedecimals

    s = s[0:idx] + "." + s[idx:]

    return s
checkincomming()


