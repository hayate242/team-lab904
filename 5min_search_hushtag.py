# -*- coding: utf-8 -*-
from twitter import *
import time

#apiキー情報設定
CONSUMER_KEY        = ''
CONSUMER_SECRET_KEY = ''
ACCESS_TOKEN        = ''
ACCESS_TOKEN_SECRET = ''



def search_tw_and_tw():
    try:
        t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET_KEY))
        # 検索するpy
        apiresults = t.search.tweets(q="#過去問お知らせbot", lang="ja", result_type="recent", count=10)
        print(len(apiresults["statuses"]))
        searched_data = apiresults['statuses']
        for tw in searched_data:
            print(tw["text"])
            t.statuses.update(status=tw["text"])
#   errorが出ても無視
    except Exception as e:
        print(e)


if __name__ == "__main__":

    while True:
        search_tw_and_tw()
        time.sleep(3)
