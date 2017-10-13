# -*- coding: utf-8 -*-

import re
import command as CMD

import logging.config

logging.config.fileConfig("../logger.conf")
logger = logging.getLogger("Parser")


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
        self.child = []  # child node
        self.next = None  # the next item in the current sexp
        self.value = ""  # actual content
        self.startLine = 0  #
        self.endLine = 0  #
        self.name = ""  # node Name

    def addChild(self, child):
        self.child.append(child)


# Directive is the structure used during a build run to hold the state of
# parsing directives.
class Directive:
    def __init__(self):
        pass


class Parser:
    def __init__(self, lines):
        self.lines = lines
        root = Node()
        root.name = "root"

    def parse(self):
        for line in self.lines:
            print(line)

    def handle_comment_and_blank(self):
        pure_lines = []
        for line in self.lines:
            line = line.strip().lower()  # remove white space
            if line == "" or line.startswith("#"):
                continue  # remove blank line and comment
            else:
                pure_lines.append(line)

        self.lines = pure_lines

    def parse_run(self):
        # 记录
        run_commands = []
        size = len(self.lines)
        index = 0
        if size == 0:
            return

        pattern = re.compile("^RUN (.*)\\\$")
        while index < size:
            line = self.lines[index]
            command = ""
            if line.startswith(CMD.Run + " "):
                if not line.endswith("\\"):
                    command = line.split(CMD.Run + " ")[-1]
                else:
                    m = pattern.match(line)
                    if m:
                        command += m.group(1)
                        index += 1
                        while index < size:
                            line = self.lines[index]
                            if line.endswith("\\"):
                                command += line.strip("\\")
                                index += 1
                            else:
                                break
                                # print ("final command: \n" + command)
                if command != "":
                    run_commands.append(command)
                    for cmd in command.split("&&"):
                        print(cmd)
            index += 1
