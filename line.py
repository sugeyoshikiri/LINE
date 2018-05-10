# -*- coding:utf-8 -*-
import json
import requests

config = json.load(open('config.json', 'r'))
lineToken = config['lineToken']

print(config)
line_notify_api = "https://notify-api.line.me/api/notify"

def lineNotify(linemsg):
    payload = {'message': linemsg}
    headers = {'Authorization': 'Bearer ' + lineToken}
    linemsg = requests.post(line_notify_api, data=payload, headers=headers)

linemsg = "hello world"

lineNotify(linemsg)
