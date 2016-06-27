# coding:utf-8
# 29.py

import re
import requests

def cleaner(str):
    str = re.sub(r"(\'\'\'\'\')|(\'\'\')|(\'\')|", "", str)
    str = re.sub(r"\[\[([^|\]]+?\|)*(.+?)\]\]", r"\2", str)
    str = re.sub(r"\[.*?\]", r"", str)
    str = re.sub(r"<.*?>", r"", str)
    str = re.sub(r"\{\{.+?\|.+?\|(.+?)\}\}", r"\1", str)
    return str

def json_search(json_data):
    ret_dict = {}
    for k, v in json_data.items():
        if isinstance(v, list):
            for e in v:
                ret_dict.update(json_search(e))
        elif isinstance(v, dict):
            ret_dict.update(json_search(v))
        else:
            ret_dict[k] = v
    return ret_dict
 
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

    url = "https://en.wikipedia.org/w/api.php"
    payload = {"action": "query",
               "titles": "File:{}".format(basicinfo_dict.get(u"国旗画像")),
               "prop": "imageinfo",
               "format": "json",
               "iiprop": "url"}

    json_data = requests.get(url, params = payload).json()

    print json_search(json_data).get("url")