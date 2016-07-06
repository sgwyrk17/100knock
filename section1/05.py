# coding:utf-8

original = "I am an NLPer"

def ngram(input, n):
	last = len(input) - n + 1
	ret = []
	for i in range(0, last):
		ret.append(input[i:i+n])
	return ret

if __name__ == "__main__":

	print ngram(original, 2)
	original = original.split()
	print ngram(original, 2)