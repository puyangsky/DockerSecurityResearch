# -*- coding: utf-8 -*-
# @author puyangsky

import logging.config
import re
import command
import parser
import thesaurus
from directive import Directive
from node import Node
import constants
from utils import docker_fetcher

logging.config.fileConfig("../logger.conf")
logger = logging.getLogger("parse_line")


def purify_code(line):
    install_list = line.split(" ")
    pure_install_list = []
    # 去掉'-'开头的参数
    for install in install_list:
        if install.strip().startswith("-"):
            continue
        pure_install_list.append(install.strip())
    return " ".join(pure_install_list)


def purify_install(install):
    install = install.strip()
    return install.split("=")[0]


def run_parser(body):
    child = Node()
    child.name = command.Run
    items = body.split("&&")
    directive = Directive()
    for item in items:
        item = item.strip()
        install_flag = False
        for prefix in thesaurus.INSTALL_PREFIX.keys():
            item = purify_code(item)
            match = re.search(prefix, item)
            if match:  # 说明这一行安装了软件
                tmp = re.sub(prefix, constants.SEP, item).strip()
                if not tmp.startswith(constants.SEP):
                    break
                item = re.sub(prefix, '', item).strip()
                install_flag = True
                install_list = item.split(" ")
                for install in install_list:
                    install_pattern = re.compile("^\w.*$")
                    if install_pattern.match(install):
                        install = purify_install(install)
                        if len(install.strip()) == 0:
                            continue
                        directive.add_install(install)
                    # else:
                    #     print >> sys.stderr, "invalid format: %s" % install
                break
        if not install_flag:
            directive.add_directive(item)
    child.directives = directive
    return child


def command_parser(body):
    node = Node()
    node.name = command.Cmd
    node.value.append(body)
    return node


def copy_parser(body):
    node = Node()
    node.name = command.Copy
    node.value.append(body)
    return node


def add_parser(body):
    node = Node()
    node.name = command.Add
    node.value.append(body)
    return node


def from_parser(body):
    node = Node()
    node.name = command.From
    node.value.append(body)
    # print("             |")
    # print("             V")
    # print("Base Image: %s" % body)
    items = body.split(":")
    if len(items) == 2:
        system = str(items[0]).strip()
        tag = str(items[1]).strip()
        # parse base image recursively
        base_dockerfile = docker_fetcher.fetch_official(system, tag, 1)
    else:
        system = str(items[0]).strip()
        base_dockerfile = docker_fetcher.fetch_official(system, None, 1)
    if len(base_dockerfile) != 1:
        # try to fetch unofficial dockerfile
        base_dockerfile = docker_fetcher.fetch_unofficial(system, 1)
        if len(base_dockerfile) != 1:
            return None
    base_parser = parser.Parser(body, base_dockerfile[0][0])
    return base_parser.root


def arg_parser(body):
    node = Node()
    node.name = command.Arg
    node.value.append(body)
    return node


def entrypoint_parser(body):
    node = Node()
    node.name = command.Entrypoint
    node.value.append(body)
    return node


def env_parser(body):
    node = Node()
    node.name = command.Env
    node.value.append(body)
    return node


def maintainer_parser(body):
    node = Node()
    node.name = command.Maintainer
    node.value.append(body)
    return node


def expose_parser(body):
    node = Node()
    node.name = command.Expose
    node.value.append(body)
    return node


def shell_parser(body):
    node = Node()
    node.name = command.Shell
    node.value.append(body)
    return node


def onbuild_parser(body):
    node = Node()
    node.name = command.Onbuild
    node.value.append(body)
    return node


def stop_signal_parser(body):
    node = Node()
    node.name = command.StopSignal
    node.value.append(body)
    return node


def user_parser(body):
    node = Node()
    node.name = command.User
    node.value.append(body)
    return node


def volume_parser(body):
    node = Node()
    node.name = command.Volume
    node.value.append(body)
    return node


def workdir_parser(body):
    node = Node()
    node.name = command.Workdir
    node.value.append(body)
    return node


def label_parser(body):
    node = Node()
    node.name = command.Label
    node.value.append(body)
    return node


def healthcheck_parser(body):
    node = Node()
    node.name = command.Healthcheck
    node.value.append(body)
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


if __name__ == '__main__':
    # res = docker_fetcher.fetch("nginx", "", 1)
    # print(res)
    from statistics.graphviz import json2graph as j2g
    j2g.transform("../statistics/graphviz/test.json")
