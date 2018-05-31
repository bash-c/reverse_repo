#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from string import printable

# xxd -e -g 4 ./map| cut -d' ' -f2-5 > hexmap
with open("./hexmap") as f:
    m = f.read().split()
    #  print len(m)

m = [int(m[i], 16) for i in xrange(len(m)) if i % 4 == 0]
#  print m, len(m)
#  print set(m), len(set(m))
#  print m.count(0xffffffff)
for idx, c in enumerate(m):
    if c == 0xffffffff:
        print idx / 128, idx - idx / 128 * 128, idx - idx / 128 * 128


'''
    v2 = input_map[4 * (128 * v2 + *hidden_message & 127)]
    v2 = input_map[128 * v2 + *hidden_message & 127]
    v2 = input_map[*hidden_message & 127]
'''
