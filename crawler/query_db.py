# -*- coding: utf-8 -*-

import pymysql
import utils


def connect_db():
    db = pymysql.connect(utils.getHost(), utils.getUser(), utils.getPwd(), utils.getDb(), use_unicode=True,
                         charset="utf8")
    cursor = db.cursor()
    return cursor


#
# def exec_sql():
#     cursor = connect_db()
#     sql = "select dockerfile_content from dockerfile WHERE type='nginx' limit 1"
#     cursor.execute(sql)
#     try:
#         for dockerfile in cursor.fetchall():
#             content = dockerfile[0]
#             lines = content.split("\n")
#             params = []
#             for line in lines:
#                 if line.strip() == "" or line.startswith("#"):
#                     continue
#                 params.append(line.strip())
#
#             p = Parser(params)
#             p.parse_run()
#
#     except Exception as e:
#         print(e.message)


def fetch_many(image_type, count):
    cursor = connect_db()
    sql = "select dockerfile_content from dockerfile WHERE type='%s' LIMIT %d" % (image_type, count)
    print("exec sql: " + sql)
    cursor.execute(sql)
    return cursor.fetchall()


if __name__ == '__main__':
    pass
