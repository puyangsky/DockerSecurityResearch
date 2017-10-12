# -*- coding: utf-8 -*-

lines = open("../db.conf", "r").readlines()


def getHost():
    for line in lines:
        if line.startswith("host="):
            return line.split("host=")[1].strip().strip("\n")


def getUser():
    for line in lines:
        if line.startswith("user="):
            return line.split("user=")[1].strip().strip("\n")


def getPwd():
    for line in lines:
        if line.startswith("pwd="):
            return line.split("pwd=")[1].strip().strip("\n")


def getDb():
    for line in lines:
        if line.startswith("db="):
            return line.split("db=")[1].strip().strip("\n")
