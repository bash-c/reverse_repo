#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from string import printable
from libnum import s2n

table = [82, 57, 76, 121, 54, 78, 111, 74, 118, 115, 73, 80, 110, 87, 104, 69, 84, 89, 116, 72, 101, 52, 83, 100, 108, 43, 77, 98, 71, 117, 106, 97, 90, 112, 107, 49, 48, 50, 119, 75, 67, 114, 55, 47, 79, 68, 103, 53, 122, 88, 65, 70, 113, 81, 102, 120, 66, 105, 99, 86, 51, 109, 56, 85, 0]
table = "".join(map(chr, table))
#  print table, len(table)

key = [101, 81, 52, 121, 52, 54, 43, 86, 117, 102, 90, 122, 100, 70, 78, 70, 100, 120, 48, 122, 117, 100, 115, 97, 43, 121, 89, 48, 43, 74, 50, 109]
key = map(chr, key)
#  key = "".join(map(chr, key))
#  print key, len(key)

def func(ipt):
    out = []
    #  for idx in xrange(0, 24 - 2, 3):
    for idx in xrange(1):
        out.append(table[(ipt[idx] >> 2) & 63])
    
        out.append(table[((ipt[idx] & 3) * 16) | ((ipt[idx + 1] & 240) / 16)])
    
        out.append(table[((ipt[idx + 1] & 15) * 4) | ((ipt[idx + 2] & 192) / 64)])
        
        out.append(table[ipt[idx + 2] & 63])

    return out

#  print key[: 4]
flag = ""
idx = 0
while True:
    for a in printable:
        for b in printable:
            for c in printable:
                ipt = [ord(a), ord(b), ord(c)]
                #  print ipt
                #  print func(ipt)
                if func(ipt) == key[idx: idx + 4]:
                    #  print "".join(map(chr, ipt))
                    flag += "".join(map(chr, ipt))
                    print flag
                    if "}" in flag:
                        exit()
                    idx += 4
    
