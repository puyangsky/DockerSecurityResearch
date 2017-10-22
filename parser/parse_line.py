# -*- coding: utf-8 -*-
# @author puyangsky

import logging.config
import command
from node import Node
from directive import Directive

logging.config.fileConfig("../logger.conf")
logger = logging.getLogger("parse_line")


def run_parser(body):
    child = Node()
    child.name = "run"
    items = body.split("&&")
    for item in items:
        item = item.strip()
        directive = Directive(item)
        child.directives.append(directive)
    return child


def command_parser(body):
    node = Node()
    node.name = "command"
    node.value = body
    return node


def copy_parser(body):
    node = Node()
    node.name = "copy"
    node.value = body
    return node


def add_parser(body):
    node = Node()
    node.name = "add"
    node.value = body
    return node


def from_parser(body):
    node = Node()
    node.name = "from"
    node.value = body
    return node


def arg_parser(body):
    node = Node()
    node.name = "arg"
    node.value = body
    return node


def entrypoint_parser(body):
    node = Node()
    node.name = "entrypoint"
    node.value = body
    return node


def env_parser(body):
    node = Node()
    node.name = "env"
    node.value = body
    return node


def maintainer_parser(body):
    node = Node()
    node.name = "entrypoint"
    node.value = body
    return node


def expose_parser(body):
    node = Node()
    node.name = "entrypoint"
    node.value = body
    return node


def shell_parser(body):
    node = Node()
    node.name = "shell"
    node.value = body
    return node


def onbuild_parser(body):
    node = Node()
    node.name = "onbuild"
    node.value = body
    return node


def stop_signal_parser(body):
    node = Node()
    node.name = "stop_signal"
    node.value = body
    return node


def user_parser(body):
    node = Node()
    node.name = "user"
    node.value = body
    return node


def volume_parser(body):
    node = Node()
    node.name = "volume"
    node.value = body
    return node


def workdir_parser(body):
    node = Node()
    node.name = "workdir"
    node.value = body
    return node


def label_parser(body):
    node = Node()
    node.name = "label"
    node.value = body
    return node


def healthcheck_parser(body):
    node = Node()
    node.name = "healthcheck"
    node.value = body
    return node


line_parser = {
    command.Run: run_parser,
    command.Cmd: command_parser,
    command.Copy: copy_parser,
    command.Add: add_parser,
    command.From: from_parser,
    command.Arg: arg_parser,
    command.Entrypoint: entrypoint_parser,
    command.Env: env_parser,
    command.Maintainer: maintainer_parser,
    command.Expose: expose_parser,
    command.Shell: shell_parser,
    command.Onbuild: onbuild_parser,
    command.StopSignal: stop_signal_parser,
    command.User: user_parser,
    command.Volume: volume_parser,
    command.Workdir: workdir_parser,
    command.Label: label_parser,
    command.Healthcheck: healthcheck_parser,
}
