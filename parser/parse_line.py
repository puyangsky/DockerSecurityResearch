# -*- coding: utf-8 -*-
# @author puyangsky

import logging.config
import re
import parser
import command

logging.config.fileConfig("../logger.conf")
logger = logging.getLogger("parse_line")


def run_parser(line):
    child = parser.Node()
    run_commands = []
    index = 0
    directive = ""
    items = line.split("&&")
    for item in items:
        print(item)
    return child


def command_parser():
    pass


def copy_parser():
    pass


def add_parser():
    pass


def from_parser():
    pass


def arg_parser():
    pass


def entrypoint_parser():
    pass


def env_parser():
    pass


def maintainer_parser():
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
