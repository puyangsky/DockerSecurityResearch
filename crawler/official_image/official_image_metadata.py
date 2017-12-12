# -*- coding: utf-8 -*-
# @author puyangsky

import requests
from crawler.query_db import DB
import re
import json
import sys

official_image_list = {}
official_image_map = {}
# data_file = "data/official_image_metadata.json"
github_url = "https://github.com/docker-library/official-images/tree/master/library"


# def parse_github_page():
#     content = requests.get(github_url).content
#     page = etree.HTML(content)
#     items = page.xpath("//a[@class='js-navigation-open']/@href")
#     print(items)
#     for i in range(1, len(items)):
#         repo_name = items[i]
#         image_name = repo_name.split("/")[-1]
#         url = "https://raw.githubusercontent.com" + repo_name.replace("blob/", "")
#         print(image_name + " : " + url)
#         page_content = dockerfile = requests.get(url).content
#
#
# def parse_image_version(content):
#     pass


def get_dockerfile_url():
    db = DB()
    sql = 'select name,url from officialimage'
    res = db.execute(sql)
    for item in res:
        official_image_list[str(item[0])] = str(item[1])
    # print(official_image_list)


def get_page_content(argv):
    """
    解析dockerhub页面，获取dockerfile的url列表
    :return:
    """
    if len(argv) < 2:
        print("missing args, exit...")
        sys.exit(0)
    data_file = argv[1]
    if len(official_image_list) == 0:
        get_dockerfile_url()
    pattern = re.compile(".*(https://github.com/[\S]*?Dockerfile).*", re.IGNORECASE)
    for (name, url) in official_image_list.items():
        print(name)
        content = requests.get(url).content
        dockerfile_urls = re.findall(pattern, content)
        urls = set()
        for dockerfile_url in dockerfile_urls:
            dockerfile_url = dockerfile_url.replace("github.com", "raw.githubusercontent.com")
            dockerfile_url = dockerfile_url.replace("blob/", "")
            urls.add(dockerfile_url)
        urls = list(urls)
        official_image_map[name] = urls
        print(urls)
    with open(data_file, "a+") as f:
        f.write(json.dumps(official_image_map))


if __name__ == '__main__':
    get_page_content(sys.argv)
