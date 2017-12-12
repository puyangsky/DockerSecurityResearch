# -*- coding: utf-8 -*-
# @author puyangsky

import re
import sys
import argparse


def main(arg):
    if len(arg) != 3:
        print("Invalid parameters! Exit")
        sys.exit(1)
    filename = arg[1]
    pattern = arg[2]
    with open(filename, 'r') as f:
        content = f.read()
        pattern = re.compile(pattern, re.S)
        find = re.match(pattern, content)
        if find:
            print(find.group(1))
        else:
            print("Not find, exit")


if __name__ == '__main__':
    main(sys.argv)
