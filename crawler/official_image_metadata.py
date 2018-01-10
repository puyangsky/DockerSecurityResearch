# -*- coding: utf-8 -*-
# @author puyangsky

from __future__ import print_function

import re
import sys
import uuid

import requests

from query_db import DB

official_image_list = {}
official_image_map = {}
db = DB()


def get_dockerfile_url():
    sql = 'select name,url from officialimage'
    res = db.execute(sql)
    for item in res:
        official_image_list[str(item[0])] = str(item[1])


def get_dockerfile_content(url):
    return requests.get(url).content


def dump_to_db(name, url, tag, dockerfile_content):
    dockerfile_content = dockerfile_content.replace("\\", "\\\\")
    dockerfile_content = dockerfile_content.replace("\"", "'")
    sql = 'insert into official_dockerfile (name,url,tag,dockerfile,uuid) VALUES ' \
          '("%s", "%s", "%s", "%s", "%s")' \
          % (str(name), str(url), str(tag), str(dockerfile_content), str(uuid.uuid4()))
    try:
        db.insert(sql)
    except Exception as e:
        print >> sys.stderr, e.message
        print >> sys.stderr, sql
        sys.exit(1)
    print("insert 1 item into officialimage_dockerfile")


def get_page_content():
    """
    解析dockerhub页面，获取dockerfile的url列表
    :return:
    """
    if len(official_image_list) == 0:
        get_dockerfile_url()
    pattern = re.compile("<li>(<a href=\"https://github.com/\S*?dockerfile\".*?</a>)</li>",
                         re.I)
    url_pattern = re.compile(".*<a href=\"(\S*?)\".*")
    tag_pattern = re.compile("<code>(.*?)</code>", re.I)
    for (name, url) in official_image_list.items():
        print(name)
        content = requests.get(url).content
        matches = re.findall(pattern, content)
        print("%d matches" % len(matches))
        urls = set()
        for match_str in matches:
            dockerfile_content = ""
            match = re.match(url_pattern, match_str)
            if match:
                dockerfile_url = match.group(1)
                dockerfile_url = dockerfile_url.replace("github.com", "raw.githubusercontent.com")
                dockerfile_url = dockerfile_url.replace("blob/", "")
                urls.add(dockerfile_url)
                dockerfile_content = get_dockerfile_content(dockerfile_url)
                print(dockerfile_url)
            tags = re.findall(tag_pattern, match_str)
            for tag in tags:
                dump_to_db(name, url, tag, dockerfile_content)


if __name__ == '__main__':
    get_page_content()
    # get_dockerfile_url()
