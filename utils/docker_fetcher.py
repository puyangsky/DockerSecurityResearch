# -*- coding: utf-8 -*-
# @author puyangsky

from crawler import query_db


def fetch(name, tag, count):
    db = query_db.DB()
    sql = "SELECT dockerfile FROM official_dockerfile " \
          "WHERE name='%s' AND tag='%s' LIMIT %d" % (name, tag, count)
    # print(sql)
    return db.execute(sql)


if __name__ == '__main__':
    res = fetch("tomcat", "9.0", 1)
    print(res[0][0])
