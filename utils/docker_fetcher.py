# -*- coding: utf-8 -*-
# @author puyangsky

from crawler import query_db


def fetch_official(name, tag, count=1):
    db = query_db.DB()
    if tag is None:
        tag = "latest"
    sql = "SELECT dockerfile FROM official_dockerfile " \
          "WHERE name='%s' AND tag='%s' LIMIT %d" % (name, tag, count)
    return db.execute(sql)


def fetch_unofficial(name, count=1):
    db = query_db.DB()
    sql = "SELECT dockerfile_content FROM dockerfile " \
          "WHERE dockerfile_name='%s' LIMIT %d" % (name, count)
    return db.execute(sql)


if __name__ == '__main__':
    res = fetch_official("tomcat", "9.0", 1)
    print(res[0][0])
