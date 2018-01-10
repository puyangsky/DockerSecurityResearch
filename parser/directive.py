# -*- coding: utf-8 -*-
# @author puyangsky


# Directive is the structure used during a build run to hold the state of
# parsing directives.
class Directive:
    def __init__(self):
        self.directive = []
        self.install = []

    def add_install(self, software):
        self.install.append(software)

    def add_directive(self, directive):
        self.directive.append(directive)
