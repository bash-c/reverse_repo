import pdb
from z3 import *
array = [164,25, 4, 130, 126, 158, 91, 199, 173, 252, 239, 143, 150, 
251, 126, 39, 104, 104, 146, 208, 249, 9, 219, 208, 101, 
182, 62, 92, 6, 27, 5, 46]
# print len(array)

def getNum():
	b = 0
	num2 = 0
	# 2 ** 30 <= num < 2 ** 31
	s = Solver()
	num = BitVec('num', 64)
	s.add(num >= 2 ** 30)
	s.add(num < 2 ** 31)
	# s.add(num > 1510650850)

	for i in xrange(32):
		if i < 5:
			s.add(((array[num2] ^ (num & 0xff) ^ b) & 0xff) == ord('FLAG{'[i]))
		elif 5 <= i < 24:
			s.add(
					Or(	
						And(
							((array[num2] ^ (num & 0xff) ^ b) & 0xff) >= 65, 
							((array[num2] ^ (num & 0xff) ^ b) & 0xff) <= 90, 
						),
						
						# ((array[num2] ^ (num & 0xff) ^ b) & 0xff) == ord('{'),
						# ((array[num2] ^ (num & 0xff) ^ b) & 0xff) == ord('}'),
						((array[num2] ^ (num & 0xff) ^ b) & 0xff) == ord(' ')

					)
				)
		# elif i == 31:
			# s.add(((array[num2] ^ (num & 0xff) ^ b) & 0xff) == ord('}'))
		b ^= array[num2]
		b &= 0xff
		num2 += 1
		num >>= 1

	if s.check() == sat:
		print s.model()
	# while s.check() == sat:
		# print s.model()
		# s.add(num != s.model()[num])

getNum()