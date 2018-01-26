#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = "M4x"

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
	s.add(num >= 2 ** 31)
	s.add(num < 2 ** 32)
	# s.add(num > 1510650850)

	for i in xrange(32):
		if i < 5:
			s.add(((array[num2] ^ (num & 0x7f) ^ b) & 0x7f) == ord('FLAG{'[i]))
		elif 5 <= i < 31:
			s.add(
					Or(	
						And(
							((array[num2] ^ (num & 0x7f) ^ b) & 0x7f) >= 65, 
							((array[num2] ^ (num & 0x7f) ^ b) & 0x7f) <= 90, 
						),
						
						# ((array[num2] ^ (num & 0x7f) ^ b) & 0x7f) == ord('{'),
						# ((array[num2] ^ (num & 0x7f) ^ b) & 0x7f) == ord('}'),
						((array[num2] ^ (num & 0x7f) ^ b) & 0x7f) == ord(' ')

					)
				)
                elif i == 31:
                        s.add(((array[num2] ^ (num & 0x7f) ^ b) & 0x7f) == ord('}'))
		b ^= array[num2]
		b &= 0x7f
		num2 += 1
		num >>= 1

	if s.check() == sat:
		print s.model()
                #bug
		#  print s.model()[num].as_long()
	# while s.check() == sat:
		# print s.model()[num]
		# s.add(Or(num != s.model()[num].as_long()))

def getFlag():
	text2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ{} "
	num = 3658134498
	num2 = 0
	b = 0 
	flag = ""

	while num:
		c = chr((array[num2] ^ (num & 0x7f) ^ b) & 0x7f)
		if c not in text2:
			print ord(c)
		flag += c
		b ^= array[num2]
		num2 += 1
		num >>= 1
		print flag

#  getNum()
getFlag()
