#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from string import printable

with open("./hexmap") as f:
    m = f.read().split()

m = [int(i, 16) for i in m]
#  LODWORD(v2) = *(_DWORD *)&input_map[512 * v2 + 4 * (*hidden_message & 0x7F)];
#  print len(m), type(m)
#  print set(m), len(set(m))

endList = [i for i, c in enumerate(m) if c == 0xffffffff]
#  for i in endList:
    #  print (i - (ord('}') & 0x7f) * 4) / 512

endList = [i for i, c in enumerate(m) if c == 501]
print endList
#  [80517, 151080]

for i in printable:
    if (80517 - 4 * ord(i)) / 512 in m:
        print i
        print (80517 - 4 * ord(i)) / 512
