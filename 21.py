# coding:utf-8

import json

with open("uk.txt") as f:
    lines = f.readlines()
    for line in lines:
        if "Category" in line:
            print line