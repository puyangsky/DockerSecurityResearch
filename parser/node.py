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
class Node:
    def __init__(self):
        self.child = {}  # child node
        self.next = None  # the next item in the current sexp
        self.value = ""  # actual content
        self.startLine = 0  #
        self.endLine = 0  #
        self.name = ""  # node Name

    def addChild(self, child):
        self.child[child.name] = child