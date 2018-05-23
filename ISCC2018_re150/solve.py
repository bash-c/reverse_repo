#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

encrypt = "s_imsaplw_e_siishtnt{g_ialt}F"

before = "abcdefghijklmnopqrstuvwxyzABC"
after = "onpqmlrskjtuihvwgfxyedzAcbBCa"

flag = [encrypt[after.find(c)] for c in before]
print "".join(flag)
