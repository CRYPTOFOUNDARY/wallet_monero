import requests
from requests.auth import HTTPDigestAuth
import json
from walletconfig import rpcpassword, rpcusername, shard
from app.monero_wallet_models import monero_Wallet_Work, monero_Wallet, monero_unconfirmed
from app import db

# simple wallet is running on the localhost and port of 18082
url = "http://test:test@localhost:28080/json_rpc"

# standard json header
headers = {'content-type': 'application/json'}




def sendCoin(userid,sendto,amount,comment):
    # simplewallet' procedure/method to call
    mixin = 4
    int_amount = amount
    recipents = [{"address": sendto,
                  "amount": int_amount}]
    rpc_input = {
        "method": "transfer",
        "params": {"destinations": recipents,
                   "mixin": mixin,
                   "payment_id" : comment}
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




def main():
    #type 1: wallet creation
    #type 2: send coin offsite

    work = db.session.query(monero_Wallet_Work)
    work = work.filter(monero_Wallet_Work.type != 0)
    work = work.filter(monero_Wallet_Work.shard == shard)
    work = work.order_by(monero_Wallet_Work.created.desc())
    walletwork = work.all()

    for f in walletwork:
        # create wallet


        # off site
        if f:
            if f.type == 1:
                sendCoin(f,
                         userid=f.userid,
                         sendto=f.sendto,
                         amount=f.amount,
                         comment=f.txtcomment,
                         )
        else:
            pass



#main()
sendCoin(userid=30)