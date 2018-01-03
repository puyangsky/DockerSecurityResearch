# -*- coding: utf-8 -*-
# @author puyangsky

import sys
import json
import requests


def fetch_content(argv):
    if len(argv) < 2:
        print("missing args, exit...")
        sys.exit(0)
    metadata_file = argv[1]
    with open(metadata_file, 'r') as f:
        content = f.read()
        metadata = json.loads(content)
        for (name, urls) in metadata.items():
            print(name)
            for url in urls:
                docker_file = requests.get(url).content
                print(docker_file)


if __name__ == '__main__':
    fetch_content(sys.argv)
