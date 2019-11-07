# -*- coding:utf-8 -*-
import os
import random
import json
import urllib.request


def lambda_handler(event, context):
    post_slack()
    return ("End")

def post_slack():
    user_list = ["U0KTQF99R", "UGSEMJ9EK", "UHD6KN35F"]
    counter = [0, 1, 2]
    random.shuffle(counter)
    method = "POST"
    print("Today's Redmine Checker Pick up Start.")

    send_data = {
        'username': 'Redmine-Checker',
        'channel': '#channel',
        'icon_emoji': ':iconalias:',
        'text': '10時の当番は<@' + user_list[counter[0]] + '>です\r\n```URLS```'
    }

    send_text = ("payload=" + json.dumps(send_data)).encode('utf-8')

    request = urllib.request.Request(
        os.environ["WEB_HOOK_URL"],
        data=send_text,
        method=method
    )
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode('utf-8')