# coding:utf-8

import sys
import math

n = int(sys.argv[2])

with open(sys.argv[1]) as f:
	line = f.readlines()
	l = int(math.ceil((len(line) + 1) / n))
	print "number of bunkatu: %d" % l
	for i in range(n):
		with open("split0" + str(i) + ".txt", "w") as f0:
			f0.write(''.join(line[l*i:l*(i+l)-1]))