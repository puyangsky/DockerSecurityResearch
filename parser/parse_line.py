# -*- coding: utf-8 -*-
# @author puyangsky

import logging.config
import parser
import command
from node import Node

logging.config.fileConfig("../logger.conf")
logger = logging.getLogger("parse_line")


def run_parser(body):
    child = parser.Node()
    run_commands = []
    index = 0
    directive = ""
    items = body.split("&&")
    for item in items:
        print(item)
    return child


def command_parser(body):
    pass


def copy_parser(body):
    pass


def add_parser(body):
    pass


def from_parser(body):
    node = Node()
    node.name = "from"
    node.value = body
    return node


def arg_parser(body):
    pass


def entrypoint_parser(body):
    pass


def env_parser(body):
    pass


def maintainer_parser(body):
    pass


line_parser = {
    command.Run: run_parser,
    command.Cmd: command_parser,
    command.Copy: copy_parser,
    command.Add: add_parser,
    command.From: from_parser,
    command.Arg: arg_parser,
    command.Entrypoint: entrypoint_parser,
    command.Env: env_parser,
    command.Maintainer: maintainer_parser
}
