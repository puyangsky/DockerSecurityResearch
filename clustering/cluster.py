#!/usr/bin/env python
# encoding: utf-8

"""
@author: puyangsky
@file: cluster.py
@time: 2018/1/4 上午1:13
"""
from __future__ import print_function
import parser.command as command
from parser import parser
import math


class Cluster:
    def __init__(self, image_type, count, verbose=False):
        self.image_type = image_type
        self.count = count
        self.node_list = parser.parse(self.image_type, self.count, verbose)
        self.software = set()
        self.software_list = []
        self.software_map = {}
        self.idf_map = {}
        self.score_map = {}

    def prepare_data(self):
        for node in self.node_list:
            print("==========%s========" % node.name)
            self.software_list.extend(node.child[command.Run].directives.install)
            for x in node.child[command.Run].directives.install:
                print(x, end=", ")
            print()
        # print("Total software cnt: %d" % len(self.software_list))
        for s in self.software_list:
            if s in self.software_map:
                self.software_map[s] = self.software_map[s] + 1
            else:
                self.software_map[s] = 1

    def calculate_idf(self):
        """
        计算安装的软件的idf
        idf = log(总dockerfile数 / 包含该软件的dockerfile数 + 1)
        """
        for x, y in self.software_map.items():
            self.idf_map[x] = math.log(self.count / (y+1))
        for node in self.node_list:
            self.score_map[node.name] = 0
            for x in node.child[command.Run].directives.install:
                self.score_map[node.name] += self.idf_map[x]
        for x, y in self.score_map.items():
            print(x, y)

    def distance(self):
        """
        计算A节点和B节点的相似度
        对于Run标签来说，先统计A和B总共Run标签下的执行命令数量，再计算相同的数量，除以总共数量即为相似度
        即：交集除以并集
        :return:
        """
        for node in self.node_list:
            run_node = node[command.Run]


if __name__ == '__main__':
    c = Cluster("nginx", 10, False)
    c.prepare_data()
    c.calculate_idf()
