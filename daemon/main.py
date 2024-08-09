import time
import sys 
import requests
import os
from dotenv import load_dotenv
from flask import json, jsonify
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from python.db import fetch_messages,insert_into_sms_archive,delete_message
load_dotenv()
i=1
while True:
    try:
        time.sleep(2)
        messages = fetch_messages()
        if len(messages) > 0:
            api = os.getenv('DAEMONAPI')
            for message in messages:
                print(message)
                message_body = {
            "SenderId": os.getenv('DAEMONSENDERID'),
        "MessageParameters": [
        {
      "Number":int(message[2]),
      "Text": message[1]
        }
        ],
        "ApiKey": os.getenv('DAEMONAPIKEY'),
        "ClientId":os.getenv('DAEMONCLIENTID')
        }
                session = requests.session()
                session.headers.update({'Content-Type': 'application/json'})
                response = session.post(api,json=message_body)
                print(response.json())
                if response.json().get('ErrorCode') == 0:
                    status = insert_into_sms_archive(message)
                    delete_status = delete_message(message[0])
    except Exception as e:
        print(e)


