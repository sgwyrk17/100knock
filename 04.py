# coding:utf-8
import re

if __name__ == "__main__":

	sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
	list1 = re.split('[\s,.]', sentence)
	list1 = filter(lambda s:s != '', list1) #null delete from list1
	count = 0
	dict1 ={}
	for (i, word) in enumerate(list1):
		n = i + 1
		if (n == 1) or (5 <= n <=9) or (n == 15) or (n == 16) or (n == 19):
			dict1.update({word[0:1]:n})
		else:
			dict1.update({word[0:2]:n})

	dict2 = sorted(dict1.items(), key=lambda x:x[1])
	print dict2