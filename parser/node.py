# -*- coding: utf-8 -*-
# @author puyangsky


# Node is a structure used to represent a parse tree.
#
# In the node there are three fields, Value, Next, and Children. Value is the
# current token's string value. Next is always the next non-child token, and
# children contains all the children. Here's an example:
#
# (value next (child child-next child-next-next) next-next)
#
# This data structure is frankly pretty lousy for handling complex languages,
# but lucky for us the Dockerfile isn't very complicated. This structure
# works a little more effectively than a "proper" parse tree for our needs.
import sys

import command


class Node(object):
    def __init__(self):
        self.child = {}  # child node
        self.value = []  # actual content
        self.name = ""  # node Name
        self.directives = None  # Directive

    def addChild(self, child):
        if child.name not in self.child.keys():
            self.child[child.name] = child
        else:
            # merge child
            if child.name == command.Run:
                self.child[child.name].directives.directive.extend(child.directives.directive)
                self.child[child.name].directives.install.extend(child.directives.install)
            else:
                self.child[child.name].value.extend(child.value)
