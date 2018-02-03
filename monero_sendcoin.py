import requests
from decimal import Decimal
from requests.auth import HTTPDigestAuth
import json
from walletconfig import rpcpassword, rpcusername, shard
from app.monero_wallet_models import\
    monero_Wallet_Work, MoneroBlockheight, monero_Wallet

from monero_addtotransactions import monero_addtransaction
from app import db


# simple wallet is running on the localhost and port of 18082
url = "http://test:test@localhost:28080/json_rpc"

# standard json header
headers = {'content-type': 'application/json'}

def sendCoin(f,sendto,amount,paymentid):
    """
    This will send the coin.
    If it fails turn the work to 105 for error
    Update the send transaction with txid

    """

    lastblockheight = db.session.query(MoneroBlockheight).filter_by(id=1).first()
    getuserswallet = db.session.query(monero_Wallet).filter_by(userid=f.userid).first()
    destination_address = str(sendto)

    # cryptonote amount format is different then
    # that normally used by people.
    # thus the float amount must be changed to
    # something that cryptonote understands
    int_amount = int(get_amount(amount))

    # just to make sure that amount->coversion->back
    # gives the same amount as in the initial number
    assert amount == Decimal(get_money(str(int_amount))), "Amount conversion failed"

    # send specified xmr amount to the given destination_address
    recipents = [{"address": destination_address,
                  "amount": int_amount}]

    # using given mixin
    mixin = 4

    # get some random payment_id
    if int(paymentid) == 0:
        # simplewallet' procedure/method to call
        rpc_input = {
            "method": "transfer",
            "params": {"destinations": recipents,
                       "mixin": mixin,
                      }
        }
    else:

        payment_id = str(paymentid)

        # simplewallet' procedure/method to call
        rpc_input = {
            "method": "transfer",
            "params": {"destinations": recipents,
                       "mixin": mixin,
                       "payment_id": payment_id}
        }

    # add standard rpc values
    rpc_input.update({"jsonrpc": "2.0", "id": "0"})

    # execute the rpc request
    response = requests.post(
        url,
        data=json.dumps(rpc_input),
        headers=headers,
        auth=HTTPDigestAuth(rpcusername, rpcpassword))

    # pretty print json output
    response_json = response.json()
    print(json.dumps(response.json(), indent=4))

    # see if successful
    if "result" in response_json:
        if "tx_hash" in response_json["result"]:
            thetxid = response_json["result"]['tx_hash']
            feefromtx = response_json["result"]['fee']
            thefee = Decimal(get_money(str(feefromtx)))
            monero_addtransaction(category=2,
                                  amount=amount,
                                  userid=f.userid,
                                  txid=thetxid,
                                  shard=shard,
                                  block=lastblockheight.blockheight,
                                  balance=getuserswallet.currentbalance,
                                  confirmed=1,
                                  fee=thefee,
                                  address=sendto
                                  )

            db.session.delete(f)
            db.session.commit()
        else:
            if "error" in response_json:
                if "message" in response_json["error"]:
                    theerror = response_json["error"]['message']
                    if theerror == 'not enough unlocked money':
                        f.type = 1
                        db.session.add(f)
                        db.session.commit()

                    else:
                        f.type = 104
                        db.session.add(f)
                        db.session.commit()
                else:
                    f.type = 104
                    db.session.add(f)
                    db.session.commit()
            else:
                f.type = 104
                db.session.add(f)
                db.session.commit()
    else:
        if "error" in response_json:
            if "message" in response_json["error"]:
                theerror = response_json["error"]['message']
                if theerror == 'not enough unlocked money':
                    f.type = 1
                    db.session.add(f)
                    db.session.commit()

                else:
                    f.type = 104
                    db.session.add(f)
                    db.session.commit()
            else:
                f.type = 104
                db.session.add(f)
                db.session.commit()
        else:
            f.type = 104
            db.session.add(f)
            db.session.commit()


def get_amount(amount):
    """
    decode cryptonote amount format to user friendly format.

    """
    CRYPTONOTE_DISPLAY_DECIMAL_POINT = 12

    str_amount = str(amount)

    fraction_size = 0

    if '.' in str_amount:

        point_index = str_amount.index('.')

        fraction_size = len(str_amount) - point_index - 1

        while fraction_size < CRYPTONOTE_DISPLAY_DECIMAL_POINT and '0' == str_amount[-1]:

            str_amount = str_amount[:-1]
            fraction_size = fraction_size - 1

        if CRYPTONOTE_DISPLAY_DECIMAL_POINT < fraction_size:
            return False

        str_amount = str_amount[:point_index] + str_amount[point_index + 1:]

    if not str_amount:
        return False

    if fraction_size < CRYPTONOTE_DISPLAY_DECIMAL_POINT:
        str_amount = str_amount + '0' * (CRYPTONOTE_DISPLAY_DECIMAL_POINT - fraction_size)

    return str_amount


def get_money(amount):
    """
    decode cryptonote amount format to user friendly format.

    """

    CRYPTONOTE_DISPLAY_DECIMAL_POINT = 12

    s = amount

    if len(s) < CRYPTONOTE_DISPLAY_DECIMAL_POINT + 1:
        # add some trailing zeros, if needed, to have constant width
        s = '0' * (CRYPTONOTE_DISPLAY_DECIMAL_POINT + 1 - len(s)) + s

    idx = len(s) - CRYPTONOTE_DISPLAY_DECIMAL_POINT

    s = s[0:idx] + "." + s[idx:]

    return s




def main():
    """
    this will look for work to do.  setup to provice furture expansion
    type 1: send coin offsite

    """

    work = db.session.query(monero_Wallet_Work)
    work = work.filter(monero_Wallet_Work.type != 0)
    work = work.filter(monero_Wallet_Work.shard == shard)
    work = work.order_by(monero_Wallet_Work.created.desc())
    walletwork = work.all()

    for f in walletwork:
        if f:
            if f.type == 1:
                sendCoin(f,
                         sendto=f.sendto,
                         amount=f.amount,
                         paymentid=f.paymentid,

                         )
        else:
            pass



main()
