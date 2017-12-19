# -*- coding: utf-8 -*-

import pymysql
import utils


class DB:
    def __init__(self, host=utils.getHost(),
                 user=utils.getUser(),
                 pwd=utils.getPwd(),
                 db_name=utils.getDb()):
        _db = pymysql.connect(host, user, pwd, db_name, use_unicode=True,
                              charset="utf8")
        self.cursor = _db.cursor()

    def execute(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()


def connect_db():
    _db = pymysql.connect(utils.getHost(), utils.getUser(), utils.getPwd(), utils.getDb(), use_unicode=True,
                          charset="utf8")
    cursor = _db.cursor()
    return cursor


def fetch_many(image_type, count):
    cursor = connect_db()
    sql = "select dockerfile_content from dockerfile WHERE type='%s' LIMIT %d" % (image_type, count)
    # print("exec sql: " + sql)
    cursor.execute(sql)
    return cursor.fetchall()


if __name__ == '__main__':
    db = DB()
    rs = db.execute("select * from dockerfile WHERE dockerfile_name like '%nginx%' LIMIT 10")
    for r in rs:
        print(r)
    print(len(rs))
