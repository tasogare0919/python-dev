# -*- coding:utf-8 -*-
import random
import requests
import json

user_list = ["U0KTQF99R","UGSEMJ9EK","UHD6KN35F"]
counter = random.randint(0,2)
print(user_list[counter])

WEB_HOOK_URL = "https://hooks.slack.com/services/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"
requests.post(WEB_HOOK_URL, data = json.dumps({
    'text': '今日のRedmineチェッカー当番は<@' + user_list[counter] + '>です',
    'username': 'Redmine-Checker',
    'channel': '#prj-famima-sp2-ops',
    'icon_emoji': ':famipay:'
}))

