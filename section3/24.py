# coding:utf-8

import re

with open("uk.txt") as f:
    lines = f.readlines()
    for line in lines:
        media_line = re.search(u"(File|ファイル):(.*?)\|", line)
        if media_line is not None:
            print media_line.group(2)