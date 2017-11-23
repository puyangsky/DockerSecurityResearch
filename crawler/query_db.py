# -*- coding: utf-8 -*-

import pymysql
import utils


class DB:
    def __init__(self):
        db = pymysql.connect(utils.getHost(), utils.getUser(), utils.getPwd(), utils.getDb(), use_unicode=True,
                             charset="utf8")
        self.cursor = db.cursor()

    def execute(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()


def connect_db():
    db = pymysql.connect(utils.getHost(), utils.getUser(), utils.getPwd(), utils.getDb(), use_unicode=True,
                         charset="utf8")
    cursor = db.cursor()
    return cursor


def fetch_many(image_type, count):
    cursor = connect_db()
    sql = "select dockerfile_content from dockerfile WHERE type='%s' LIMIT %d" % (image_type, count)
    # print("exec sql: " + sql)
    cursor.execute(sql)
    return cursor.fetchall()


if __name__ == '__main__':
    pass
