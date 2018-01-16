#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function

"""
@author: puyangsky
@file: cluster.py
@time: 2018/1/4 上午1:13
"""

import parser.command as command
from parser import parser


class Cluster:
    def __init__(self, image_type, count, verbose=False):
        self.image_type = image_type
        self.count = count
        self.root_list = parser.parse(self.image_type, self.count, verbose)
        self.software = []

    def software_idf(self):
        for node in self.root_list:
            self.software.extend(node.child[command.Run].directives.install)
        print("Total software cnt: %d" % len(self.software))
        for s in self.software: print(s)

    def distance(self):
        """
        计算A节点和B节点的相似度
        对于Run标签来说，先统计A和B总共Run标签下的执行命令数量，再计算相同的数量，除以总共数量即为相似度
        即：交集除以并集
        :return:
        """
        for node in self.root_list:
            run_node = node[command.Run]


if __name__ == '__main__':
    c = Cluster("nginx", 2, False)
    c.software_idf()
