# coding:utf-8
import re

if __name__ == "__main__":

	sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
	list1 = re.split('[\s,.]', sentence)
	list1 = filter(lambda s:s != '', list1) #null delete from list1
	list2 = []

	for word in list1:
		list2.append(len(word))

	print list2




