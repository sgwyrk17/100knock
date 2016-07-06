# coding:utf-8

def cipher(str1):
	ret = ""
	for char in str1:
		if char.islower() == True:
			ret += chr(219 - ord(char))
		else:
			ret += char
	return ret


if __name__ == "__main__":
	str1 = "I am hungry"
	angou = cipher(str1)
	print angou
	hukugou = cipher(angou)
	print hukugou
