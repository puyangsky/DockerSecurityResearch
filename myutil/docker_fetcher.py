# -*- coding: utf-8 -*-
# @author puyangsky

from crawler import query_db


def fetch(name, tag, count):
    db = query_db.DB()
    sql = "SELECT dockerfile_name, dockerfile_content FROM dockerfile " \
          "WHERE dockerfile_name LIKE '%%%s%%' LIMIT %d" % (name, count)
    return db.execute(sql)


if __name__ == '__main__':
    res = fetch("nginx", "", 1)
    print(len(res))
