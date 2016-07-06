# coding:utf-8

import json
import re

with open("uk.txt") as f:
    lines = f.readlines()
    for line in lines:
        category_lines = re.search("^\[\[Category:(.*?)(|\|.*)\]\]$", line)
        if category_lines is not None:
            print category_lines.group(1)
