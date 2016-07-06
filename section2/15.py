# coding:utf-8

import sys

n = int(sys.argv[2])

with open(sys.argv[1]) as f:
	lines = f.readlines()
	print ("".join(lines[-n:]))