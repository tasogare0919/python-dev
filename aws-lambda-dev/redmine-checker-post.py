# -*- coding:utf-8 -*-
import random
import os
import json
import urllib.request

def lambda_handler(event, context):
    post_slack()
    return "End"

def post_slack():
    user_list = ["USERID"]
    counter = random.randint(0, 2)
    method = "POST"

    send_data = {
        'username': 'UserName',
        'channel': '#Channel',
        'icon_emoji': 'emojiicon',
        'text': '今日の当番は<@' + user_list[counter] + '>です',
    }

    send_text = ("payload=" + json.dumps(send_data)).encode('utf-8')

    request = urllib.request.Request(
        os.environ["WEB_HOOK_URL"],
        data=send_text,
        method=method
    )
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode('utf-8')
