# coding:utf-8

import sys

with open("hightemp.txt") as f:
	list1 =[]
	for row in f:
		s = row.split("\t")
		flag = 0
		for str in list1:
			if str == s[0]:
				flag = 1
				break
		if flag == 0:
			list1.append(s[0])
	with open ("17.txt", "w") as f0:
		for i in list1:
			f0.write(i)
	print list1
