#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from z3 import *

s = Solver()
a = BitVec("a", 32)
b = BitVec("b", 32)
c = BitVec("c", 32)
d = BitVec("d", 32)
e = BitVec("e", 32)
f = BitVec("f", 32)
g = BitVec("g", 32)
h = BitVec("h", 32)
i = BitVec("i", 32)
j = BitVec("j", 32)
k = BitVec("k", 32)
l = BitVec("l", 32)
w = BitVec("w", 32)
x = BitVec("x", 32)
y = BitVec("y", 32)
z = BitVec("z", 32)

L = (a, b, c, d, e, f, g, h, i, j, k, l, w, x, y, z)
for i in L:
    #  s.add(
            #  Or(
                #  And(
                    #  i >= 48,
                    #  i <= 57,
                    #  ),
                #  And(
                    #  i >= 97,
                    #  i <= 122,
                    #  ),
                #  And(
                    #  i >= 65,
                    #  i <= 90,
                    #  )
                #  )
            #  )
    s.add(i > 0)
    s.add(i < 127)

s.add(a == x - 3)
s.add(d == ((y | 1) & 0xffff))
s.add(y % 2 != 1)
s.add(y == c + 8)
s.add(w == a - 2)
s.add(x == ((d ^ 18) & 0xffff))
s.add(b * 2 == c - 8)
s.add(z == c)
s.add(12 + f == h)
s.add(j * 2 == h - 13)
s.add(e + i == 187)
s.add(e + l == 210)
s.add((h ^ g) == 47)
#  s.add((e ^ f) == 15)
s.add((k ^ f) == 5)
s.add((z ^ 55) > ((g - 4 ^ 113)))
s.add((z ^ 55) < 100)


#  if s.check() == sat:
    #  print s.model()
while s.check() == sat:
    #  print s.model() 
    ss = chr(int(s.model()[a].as_long())) + chr(int(s.model()[b].as_long())) + chr(int(s.model()[c].as_long())) + chr(int(s.model()[d].as_long())) + "-" 
    ss += chr(int(s.model()[e].as_long())) + chr(int(s.model()[f].as_long())) + chr(int(s.model()[g].as_long())) + chr(int(s.model()[h].as_long())) + "-" 
    ss += chr(int(s.model()[i].as_long())) + chr(int(s.model()[j].as_long())) + chr(int(s.model()[k].as_long())) + chr(int(s.model()[l].as_long())) + "-"
    #  ss += chr(int(s.model()[i].as_long())) + chr(int(s.model()[j].as_long())) + chr(int(s.model()[k].as_long())) + "K-"
    #  ss += chr(int(s.model()[i].as_long())) + chr(int(s.model()[j].as_long())) + chr(int(s.model()[k].as_long())) + "j-"
    ss += chr(int(s.model()[w].as_long())) + chr(int(s.model()[x].as_long())) + chr(int(s.model()[y].as_long())) + chr(int(s.model()[z].as_long()))
    #  print s.model()
    print ss
    s.add(a != s.model()[a])

