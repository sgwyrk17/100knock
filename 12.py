# coding:utf-8

import sys

with open(sys.argv[1]) as f:
	with open("col1.txt", "w") as col1, open("col2.txt", "w") as col2:
		for row in f:
			s = row.split("\t")
			col1.write(s[0] + "\n")
			col2.write(s[1] + "\n")
