# coding:utf-8

original1 = "paraparaparadise"
original2 = "paragraph"

def ngram(input, n):
	list1 = len(input) - n + 1
	ret = []
	for i in range(0, list1):
		ret.append(input[i:i+n])
	return ret

if __name__ == "__main__":

	X = set(ngram(original1, 2))
	Y = set(ngram(original2, 2))
	print X.union(Y) 
	print X.intersection(Y) 
	print X.difference(Y) 

	print "se" in X     #ret = true or false
	print "se" in Y

	