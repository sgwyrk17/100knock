# coding:utf-8

with open("hightemp.txt") as f:
	 lines = f.readlines()
	 lines.sort(key = lambda x: x.split('\t')[2], reverse = True)
	 print('').join(lines)