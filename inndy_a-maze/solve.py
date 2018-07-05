#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

'''
    v2 = input_map[4 * (128 * v2 + *hidden_message & 127)]
'''

from string import printable

# xxd -e -g 4 ./map| cut -d' ' -f2-5 > hexmap
with open("./hexmap") as f:
    hexmap = f.read().split()
    #  print len(hexmapm)

m = [int(i, 16) for i in hexmap]
