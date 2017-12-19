#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function

import pygraphviz as pgv
import json

"""
@author: puyangsky
@file: json2graph.py
@time: 2017/12/19 下午11:09
"""


def travel_json(data, root, pre=None):
    # check type of json node
    # list or dict
    # print("type of data:", type(data))
    if type(data) == dict:
        for key0 in data.keys():
            if pre is not None:
                root.add_edge(pre, key0)
            value = data[key0]
            travel_json(value, root, key0)
    elif type(data) == list:
        for item in data:
            travel_json(item, root, pre)
    else:
        if pre is not None:
            root.add_edge(pre, data)


def transform():
    graph = pgv.AGraph(directed=True, strict=True)
    with open("test.json", "r") as f:
        json_data = json.loads(f.read())

    # print(json.dumps(json_data, indent=2))
    travel_json(json_data, graph)
    # A.add_edge(1, 2)
    print(graph.string())
    graph.layout('dot')
    graph.draw('test.png')


if __name__ == '__main__':
    transform()
