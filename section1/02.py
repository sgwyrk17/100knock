
# coding:utf-8

if __name__ == "__main__":

	moji1 = u'パトカー'
	moji2 = u'タクシー'


	print ''.join([a + b for a,b in zip(moji1, moji2)])