# coding:utf-8

import json
import re

with open("uk.txt") as f:
    lines = f.readlines()
    for line in lines:
        section_line = re.search("^(==+)(.*?)(==+)$", line)
        if section_line is not None:
            print section_line.group(2), len(section_line.group(1)) - 1