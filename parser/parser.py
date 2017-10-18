# -*- coding: utf-8 -*-

from crawler import query_db as db
import parse_line as lparser
import logging.config
import re
from node import Node

logging.config.fileConfig("../logger.conf")
logger = logging.getLogger("Parser")


# Directive is the structure used during a build run to hold the state of
# parsing directives.
class Directive:
    def __init__(self):
        pass


class Parser:
    def __init__(self, dockerfile):
        if dockerfile is not None:
            self.lines = dockerfile.split("\n")
        else:
            self.lines = []
        self.root = Node()
        self.root.name = "root"
        self.handle_comment_and_blank()

    def handle_comment_and_blank(self):
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
            while line.endswith("\\"):
                index += 1
                line += self.lines[index]
            # 取command
            pattern = re.compile("^(.*?)\s+(.*?)$", re.S)
            match = re.match(pattern, line)
            if match:
                head = match.group(1)
                body = match.group(2)
                print(head, body)
                child = lparser.line_parser[head](body)
                if child is not None:
                    self.root.addChild(child)
            index += 1


"""
基本思路：
每次读取一行，如果有"\"符号就继续append到这一行中
再解析这一行作为一个child加入到root中
解析这一行时首先根据其开头的cmd dispatch到不同的处理器中
分别处理
"""


def parse():
    results = db.fetch_many(image_type="nginx", count=1)
    for result in results:
        dockerfile = result[0]
        print(dockerfile)
        parser = Parser(dockerfile)
        parser.dispatch()


if __name__ == '__main__':
    parse()
