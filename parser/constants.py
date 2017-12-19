# -*- coding: utf-8 -*-
# @author puyangsky

import command

"""
if image's base system in below,
the iterable parse will end.
"""
systems = [
    'ubunut',
    'debian',
    'centos',
    'redhat',
    'fedora',
    'alpine',
    'scratch',
]

command_weight = {
    command.Run: 0.2,
    command.Cmd: 0.2,
    command.Onbuild: 0.1,
    command.Add: 0.1,
    command.Copy: 0.1,
    command.Expose: 0.1,
    command.Env: 0.1,
    command.Volume: 0.05,
    command.Shell: 0.05,
    command.From: 0,
    command.Arg: 0,
    command.Label: 0,
    command.Healthcheck: 0,
    command.User: 0,
    command.Workdir: 0,
    command.StopSignal: 0,
    command.Entrypoint: 0,
    command.Maintainer: 0,
}
