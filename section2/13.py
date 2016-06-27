# coding:utf-8

import sys

with open("col1.txt", "r") as col1, open("col2.txt", "r") as col2:
	with open("result.txt", "w") as result:
		for row1, row2 in zip(col1.readlines(), col2.readlines()):
			result.write(row1.rstrip() + "\t" + row2)
