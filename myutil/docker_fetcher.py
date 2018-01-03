# -*- coding: utf-8 -*-
# @author puyangsky

from crawler import query_db


def fetch(name, tag, count):
    db = query_db.DB()
    sql = "SELECT name, dockerfile FROM official_dockerfile " \
          "WHERE name LIKE '%%%s%%' AND tag LIKE '%%%s%%' LIMIT %d" % (name, tag, count)
    return db.execute(sql)


if __name__ == '__main__':
    res = fetch("nginx", "", 1)
    print(len(res))
