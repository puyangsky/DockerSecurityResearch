# -*- coding: utf-8 -*-
# @author puyangsky

import crawler.query_db as db

if __name__ == '__main__':
    cursor = db.fetch_many("nginx", 10)
    for dockerfile in cursor:
        content = dockerfile[0]
        print content
        break
