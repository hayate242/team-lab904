#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import time
from twitter import *

#apiキー情報設定
CONSUMER_KEY        = 'HnMPhlOt5eJQz0TzqKZXP2ztu'
CONSUMER_SECRET_KEY = 'lOishur9V9YFLCipTguzsTX1KbDugbDBDnbCu0zfFA1zBFysKV'
ACCESS_TOKEN        = '881025654090747904-8CLYjfOiFssgzLJuWHYonT3LRXZaklR'
ACCESS_TOKEN_SECRET = 'rv6jwgo2jjd5UxiN8OOD9n7Vai1Eaf7Bog3rNUargf7Mr'

class notify_tweet:

    lastTime = ""
    # lastTime = "2017-04-27 10:33:00"
    def ask_db(self):
        # 接続する
        con = MySQLdb.connect(
                user='super',
                passwd='pass',
                host='13.113.186.93',
                db='testdb',
                charset='utf8')

        # カーソルを取得する
        cur= con.cursor()

        # クエリを実行する
        # sql = "SELECT university,department,major,lesson,year,datetime FROM contents where datetime > '2017-04-27 10:33:00'"
        if self.lastTime :
            sql = "SELECT university,department,major,lesson,year,created_at FROM contents where created_at > '"+str( self.lastTime )+"'"
            print("SELECT university,department,major,lesson,year,created_at FROM contents where created_at > '"+str( self.lastTime )+"'")
        else:
            sql = "SELECT university,department,major,lesson,year,created_at FROM contents"
        cur.execute(sql)

        # 実行結果をすべて取得する
        rows = cur.fetchall()

        # 一行ずつ表示する
        for row in rows:
            print(row)
            self.tweet_on_Bot(row)
        # 最後の値(最終時刻を取得) ↓rowが最後の配列格納してる
        if len(rows) != 0 :
            self.lastTime = row[-1]
        print("last checked time = "+str(self.lastTime))

        cur.close
        con.close


    def tweet_on_Bot( self, row ):
        try:

            t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET_KEY))
            # make string here
            tweet_data = ""

            tweet_data = str(row[0])+str(row[1])+str(row[2])+"の授業 #"+str(row[3])+" ("+str(row[4])+"年)が追加されました\n時刻"+str(row[5])
            print(tweet_data)
            t.statuses.update(status=tweet_data)

        #errorが出ても無視
        except Exception as e:
            print(e)

if __name__ == "__main__":
    n = notify_tweet()

    while True:
        n.ask_db()
        time.sleep(3)
