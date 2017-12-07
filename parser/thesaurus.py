# -*- coding: utf-8 -*-
# @author puyangsky

INSTALL_PREFIX = {
    "apt-get\s+install":  ["ubuntu", "debian"],
    "apk\s+add":          ["alpine"],
    "yum\s+install":      ["centos", "fedora", "redhat"],
}

UPDATE_PREFIX = {
    "apt-get\s+update":  ["ubuntu", "debian"],
    "apk\s+update":      ["alpine"],
    "yum\s+update":      ["centos", "fedora", "redhat"],
}
