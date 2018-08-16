#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import string
import itertools

m = lambda s: hashlib.md5(s).hexdigest()
dic = map(chr, range(0x0, 0xff))
#  dic = string.printable
#  dic = '''d4rk{pr0            4nd_als0_gGWp_Y0u!_4 r3_qul7e_gudthls _plseach  _me}'''
#  dic = "".join(set(dic))

with open("./md5s") as f:
    md5s = f.readlines()
#  print md5s
#  for i in md5s:
    #  print len(i.strip())

ans = ""
for i in xrange(0, 20):

    #  if i not in [2, 3, 13, 16]:
    if i not in []:
        for j in itertools.permutations(dic, 4):
            #  print ''.join(j)
            if m(m(''.join(j))) == md5s[i].strip():
                ans += ''.join(j)
                print "Found", i, ans
                break
    
        else:
            ans += "????"
            print "Not found", i


