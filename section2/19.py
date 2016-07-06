# coding:utf-8

with open("hightemp.txt") as f:
	 list = [s.split('\t')[0] for s in f]
	 dict = {k:list.count(k) for k in list}
	 sorted_dict = sorted(dict, key = lambda k:dict[k], reverse = True)
	 with open("19.txt", "w") as f0:
	 	f0.write('\n'.join(str(dict[k]) + ' ' + k for k in sorted_dict))
	 print('\n'.join(str(dict[k]) + ' ' + k for k in sorted_dict))
	 