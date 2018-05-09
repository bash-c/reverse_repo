#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

with open("./baby_mips") as f:
    s = list(f.read())

for idx in xrange(len(s)):
    if s[idx] == '\xeb' and s[idx + 1] == '\x02' and (idx % 4 == 0):
        s[idx] = s[idx + 1] = s[idx + 2] = s[idx + 3] = '\x00'

with open("./baby_mips_patched", "w") as f:
    f.write("".join(s))
