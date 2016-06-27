# coding:utf-8
import random

str1 = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def change(word):
	if len(word) <= 4:
		return word
	else:
		mid_list = list(word[1:-1])
		random.shuffle(mid_list)
		return word[0] + "".join(mid_list) + word[-1]

def append(str):
	ret = []
	for word in str.split():
		ret.append(change(word))
	return " ".join(ret)


if __name__ == "__main__":
	print append(str1)

