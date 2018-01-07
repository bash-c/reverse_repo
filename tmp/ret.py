#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from z3 import *

s = Solver()
n4 = BitVec("n4", 32)
n5 = BitVec("n5", 32)

s.add(n4 < 100)
s.add(n5 < 100)
s.add(n4 * n4 - n5 * n5 == 56 * (n4 + n5))
s.add(n4 * n4 + n4 * n5 + n5 * n5 > 1e4)
s.add(n4 * n4 - n4 * n5 - n5 * n5 < 1e4)
s.add(n4 % n5 == 7)

while s.check() == sat:
    print s.model()
    s.add(n4 != s.model()[n4])
else:
    print "unset"
