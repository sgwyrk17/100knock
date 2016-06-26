# coding:utf-8

def generate(x, y, z):
	return unicode(x) + u"時の" + unicode(y) + u"は" + unicode(z)

if __name__ == "__main__":
	x = 12
	y = u"気温"
	z = 22.4

	print generate(x, y, z)