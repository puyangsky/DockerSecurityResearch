# -*- coding: utf-8 -*-
# @author puyangsky

import command
import logging
import logging.config

logging.config.fileConfig("../logger.conf")
logger = logging.getLogger("parse_line")


def run_parser():
    pass

def cmd_parser():
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
    command.Run: run_parser(),
    command.Cmd: cmd_parser(),
    command.Copy: copy_parser(),
    command.Add: add_parser(),
    command.From: from_parser(),
    command.Arg: arg_parser(),
    command.Entrypoint: entrypoint_parser(),
    command.Env: env_parser(),
    command.Maintainer: maintainer_parser(),
}