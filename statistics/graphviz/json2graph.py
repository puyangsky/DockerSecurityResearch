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


def transform(json_file_path):
    graph = pgv.AGraph(directed=True, strict=True, name="graph")
    with open(json_file_path, "r") as f:
        json_data = json.loads(f.read())
        travel_json(json_data, graph)
        print(graph.string())
        graph.layout('dot')
        graph.draw('test.png')


if __name__ == '__main__':
    transform("test.json")
