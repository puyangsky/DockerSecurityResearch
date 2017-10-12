# -*- coding: utf-8 -*-

import pymysql
import utils

from parser.parser import Parser

db = pymysql.connect(utils.getHost(), utils.getUser(), utils.getPwd(), utils.getDb(), use_unicode=True, charset="utf8")
cursor = db.cursor()

sql = "select dockerfile_content from dockerfile WHERE type='nginx' limit 1"
cursor.execute(sql)
# for dockerfile in cursor.fetchall():
try:
    content = cursor.fetchone()[0]
    lines = content.split("\n")
    params = []
    for line in lines:
        if line.strip() == "" or line.startswith("#"):
            continue
        params.append(line.strip())

    p = Parser(params)
    p.parse()

except Exception as e:
    print(e.message)
