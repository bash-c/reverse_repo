import string
import pdb
dic = string.printable

def fun1(c, n):
	# pdb.set_trace()
	# print c, n
	return (ord(c) ^ (2 * ord(c) - 6)) - 2 * n

# test = '1' * 16
# for i, j in enumerate(test):
	# print hex(fun1(j, i))
	
	
data = [0xB9, 0x3A, 0xA9, 0xD8, 0x15, 0x8A, 0xE7, 0x42, 0x69, 0x90, 0xCA, 0xA3, 0x4D, 0xD8, 0xD9, 0xC9]   
# print len(data)
# for i in dic:
	# if fun1(i, 5) == 0x8A:
		# print i

ans = ""
for i in range(16):
	for j in dic:
		if fun1(j, i) == data[i]:
			# print i, "hit"
			ans += j
			break
			
print ans
