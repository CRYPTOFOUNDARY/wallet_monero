import requests
from requests.auth import HTTPDigestAuth
import json
from walletconfig import rpcpassword, rpcusername
from app import db
from app.monero_wallet_models import \
    MoneroBlockheight


# simple wallet is running on the localhost and port of 18082
url = "http://test:test@localhost:28080/json_rpc"

# standard json header
headers = {'content-type': 'application/json'}

def getblockheight():
    rpc_input = {
        "method": "getheight",

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

        lastheight = response_json["result"]['height']

        lastblockheight = db.session.query(MoneroBlockheight).filter_by(id=1).first()
        lastblockheight.blockheight = int(lastheight)

        db.session.add(lastblockheight)
        db.session.commit()

getblockheight()