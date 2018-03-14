#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

# flag{mips_with_static_is_cr4zy!} 
 
import subprocess 
import hashlib 
import json 
import itertools 
import string
 
def md5(s):
    m2 = hashlib.md5() 
    m2.update(s) 
    return m2.hexdigest()
 
with open('dict') as f:
    d = json.load(f)
 
with open('out') as f:
    out = f.read().strip() 
rst = ''
 
i = 0 
while i < 512:
    try:
        s = out[i:i+32] 
        rst += d[s][-3:-1] 
    except KeyError:
        print 'not found'
        rst += '**' 
    i += 32 
    print rst
print 'done'
