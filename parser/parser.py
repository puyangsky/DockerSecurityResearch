# -*- coding: utf-8 -*-

import json
import logging.config
import re
import command
import parse_line as lparser
from crawler import query_db as db
from node import Node
from utils import docker_fetcher

logging.config.fileConfig("../logger.conf")
logger = logging.getLogger("Parser")


class Parser:
    """
    基本思路：
    每次读取一行，如果有'\'符号就继续append到这一行中
    再解析这一行作为一个child加入到root中
    解析这一行时首先根据其开头的cmd dispatch到不同的处理器中
    分别处理
    """

    def __init__(self, name, dockerfile):
        # print(dockerfile)
        # print("\n==================================================")
        # print("\n==================================================")
        if dockerfile is not None:
            self.lines = dockerfile.split("\n")
        else:
            self.lines = []
        self.root = Node()
        self.root.base_name = name
        self.root.name = name
        self.root.directives = None
        self.base = Node()
        self.handle_comment_and_blank()
        self.dispatch()

    def handle_comment_and_blank(self):
        """
        去掉注释和空行
        """
        pure_lines = []
        for line in self.lines:
            line = line.strip().lower()  # remove white space and to lower
            if line == "" or line.startswith("#"):
                continue  # remove blank line and comment
            else:
                pure_lines.append(line)
        self.lines = pure_lines

    def dispatch(self):
        if len(self.lines) == 0:
            return
        index = 0
        while index < len(self.lines):
            line = self.lines[index]
            # \符号代表连接上一行
            while line.endswith("\\"):
                index += 1
                line = line.strip("\\")
                if index < len(self.lines):
                    line += self.lines[index]
            # 取command
            pattern = re.compile('^(.*?)\s+(.*?)$', re.S)
            match = re.match(pattern, line)
            if match:
                head = match.group(1)
                body = match.group(2)
                if head in lparser.line_parser.keys():
                    if head == command.From and body == self.root.name:
                        print("[WARNING] %s, base image is same as current image, ignore" % self.root.name)
                        break
                    child = lparser.line_parser[head](body)
                    if child is not None:
                        if head == command.From:
                            self.base = child
                        else:
                            self.root.addChild(child)
                else:
                    print("[ERROR] %s, %s" % (head, body))
            index += 1
        self.merge()

    def merge(self):
        """
        合并root节点和base节点
        :return:
        """
        for key in self.base.child.keys():
            if key in self.root.child.keys():
                if key == command.Run:
                    self.root.child[key].directives.directive.extend(self.base.child[key].directives.directive)
                    self.root.child[key].directives.install.extend(self.base.child[key].directives.install)
                if key == command.From:
                    self.root.child[key] = self.base.child[key]
            else:
                self.root.child[key] = self.base.child[key]
        if self.base.base_name != '':
            self.root.base_name = self.base.base_name


def parse(image_type, count, verbose=False):
    root_list = []
    results = db.fetch_many(image_type=image_type, count=count)
    for result in results:
        dockerfile_name, dockerfile = result[0], result[1]
        print("[INFO] parsing %s" % dockerfile_name)
        parser = Parser(dockerfile_name, dockerfile)
        json_str = json.dumps(parser.root, default=lambda obj: obj.__dict__, indent=2)
        if verbose:
            print(json_str)
        root_list.append(parser.root)
    return root_list


def parse_dockerfile(name):
    dockerfile = docker_fetcher.fetch_unofficial(name)
    if len(dockerfile) == 1:
        dockerfile = dockerfile[0][0]
    else:
        return
    parser = Parser(name, dockerfile)
    json_str = json.dumps(parser.root, default=lambda obj: obj.__dict__, indent=2)
    print(json_str)


if __name__ == '__main__':
    # parse("erickoh/nginx", 1, True)
    parse_dockerfile("erickoh/nginx")
