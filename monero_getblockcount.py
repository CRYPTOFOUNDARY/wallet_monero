import requests
from requests.auth import HTTPDigestAuth
import json
from walletconfig import rpcpassword, rpcusername, url
from app import db
from app.models import \
    MoneroBlockheight


def getblockheight():
    try:
        # standard json header
        headers = {'content-type': 'application/json'}

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
        if "result" in response_json:

            lastheight = response_json["result"]['height']

            lastblockheight = db.session.query(MoneroBlockheight).filter_by(id=1).first()
            lastblockheight.blockheight = int(lastheight)

            db.session.add(lastblockheight)
            db.session.commit()
    except Exception as e:
        print(str(e))


getblockheight()