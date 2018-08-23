#!/usr/bin/env python
# -*- coding: utf-8 -*-

off_418000 = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm\0"

off_418004 = "TOiZiZtOrYaToUwPnToBsOaOapsyS"
print len(off_418004),len(off_418000)

def decode(a):

	flag = ""

	for i in range(len(a)):
		if i %2 == 0:
			flag += a[i]
			continue
		for j,k in enumerate(off_418000):
			if a[i] == k:
				print i,j
				if chr(j+38).isupper():
					flag += chr(j+38)
				else:
					flag += chr(j+96)
				break

	return flag

def encode(flag):

	cipher = ""
	for j,i in enumerate(flag):
		if j %2 == 0:
			cipher += i
			continue
		if ord(i) < ord('a') or ord(i) > ord('z'):
			cipher += off_418000[ord(i)-38]
		else:
			cipher += off_418000[ord(i)-96]
	return cipher

if __name__ == "__main__":
	flag = off_418004
	flag = decode(flag)
	print flag
	cipher = encode(flag)

	print cipher == off_418004
