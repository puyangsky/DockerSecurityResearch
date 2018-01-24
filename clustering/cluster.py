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
from utils import docker_fetcher


class Cluster:
    def __init__(self, image_type, count, verbose=False):
        self.image_type = image_type
        self.count = count
        self.verbose = verbose
        self.node_list = parser.parse(self.image_type, self.count, verbose)
        self.software = set()
        self.software_list = []
        self.software_map = {}
        self.idf_map = {}
        self.score_map = {}

    def prepare_data(self):
        for node in self.node_list:
            if self.verbose:
                print("==========%s========" % node.name)
                for x in node.child[command.Run].directives.install:
                    print(x, end=", ")
                print()
            if command.Run in node.child.keys():
                self.software_list.extend(node.child[command.Run].directives.install)

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
            if command.Run in node.child.keys():
                for x in node.child[command.Run].directives.install:
                    self.score_map[node.name] += self.idf_map[x]
        # sort by value
        sorted_list = sorted(self.score_map.items(), key=lambda d: d[1], reverse=True)
        for x in sorted_list:
            print(x[0], x[1])
        # TODO(puyangsky): show top3 image's dockerfile
        first_dockfile = docker_fetcher.fetch_unofficial(sorted_list[48][0], 1)
        print(first_dockfile[0][0])

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
    c = Cluster("nginx", 50, False)
    c.prepare_data()
    c.calculate_idf()
