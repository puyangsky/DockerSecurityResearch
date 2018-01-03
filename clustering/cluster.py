#!/usr/bin/env python
# encoding: utf-8

"""
@author: puyangsky
@file: cluster.py
@time: 2018/1/4 上午1:13
"""

import parser.command as command


def distance(node_A, node_B):
    """
    计算A节点和B节点的相似度
    对于Run标签来说，先统计A和B总共Run标签下的执行命令数量，再计算相同的数量，除以总共数量即为相似度
    即：交集除以并集
    :param node_A:
    :param node_B:
    :return:
    """
    child_A = node_A.child
    child_B = node_B.child
    run_A = child_A[command.Run]
    run_B = child_B[command.Run]
