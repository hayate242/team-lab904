#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

def db_sample():
    """ 接続サンプル """

    # 接続する
    con = MySQLdb.connect(
            user='super',
            passwd='pass',
            host='13.113.186.93',
            db='JUni',
            charset='utf8')

    # カーソルを取得する
    cur= con.cursor()

    # クエリを実行する
    sql = "SELECT * FROM schools"
    cur.execute(sql)

    # 実行結果をすべて取得する
    rows = cur.fetchall()

    # 一行ずつ表示する
    for row in rows:
        print(row)

    cur.close
    con.close

if __name__ == "__main__":
    db_sample()
