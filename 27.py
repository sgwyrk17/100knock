# coding:utf-8

import re

def cleaner(str):
    str = re.sub(r"(\'\'\'\'\')|(\'\'\')|(\'\')|", "", str)
    str = re.sub(r"\[\[([^|\]]+?\|)*(.+?)\]\]", r"\2", str)
    # str = re.sub(r"\[\[記事名((\|)|(#節名))(.*?)\]\]", "(.*?)", str)
    return str

with open("uk.txt") as f:
    lines = f.readlines() #list
    str_lines = '' #list to str
    for line in lines:
        str_lines += str(line)
    str_lines = re.split(r"\n[\|}]", str_lines)
    basicinfo_dict={}
    for line in str_lines:
        basicinfo_line = re.search("(.*?)\s=\s(.*)", line, re.S) #re.S = "." de \n mo match
        if basicinfo_line is not None:
            basicinfo_dict[basicinfo_line.group(1)] = cleaner(basicinfo_line.group(2))

    for k, v in sorted(basicinfo_dict.items(), key=lambda x: x[1]):
        print k, v