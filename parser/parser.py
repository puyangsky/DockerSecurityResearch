# -*- coding: utf-8 -*-

import logging
import re

ENV = "ENV"
COPY = "COPY"
CMD = "CMD"
RUN = "RUN"
SHELL = "SHELL" # override the shell cmd
ONBUILD = "ONBUILD"
EXPOSE = "EXPOSE"
ADD = "ADD"
VOLUME = "VOLUME"
ENTRYPOINT = "ENTRYPOINT"
WORKDIR = "WORKDIR"
MAINTAINER = "MAINTAINER"
USER = "USER"
ARG = "ARG"
LABEL = "LABEL"
FROM = "FROM"

logger = logging.getLogger("Parser")

class Parser:
    def __init__(self, lines):
        self.lines = lines
        print("============")

    def parse(self):
        for line in self.lines:
            print(line)

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
            if line.startswith(RUN + " "):
                if not line.endswith("\\"):
                    command = line.split(RUN + " ")[-1]
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