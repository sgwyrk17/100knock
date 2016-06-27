# coding:utf-8

import sys

with open("hightemp.txt") as f:
	r = f.readlines()
	print('\n'.join(set(x.split('\t')[0] for x in r)))