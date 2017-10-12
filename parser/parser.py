# -*- coding: utf-8 -*-

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


class Parser:
    def __init__(self, lines):
        self.lines = lines

    def parse(self):
        for line in self.lines:
            print(line)