#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from subprocess import Popen, PIPE
import string

def run(tmp):
    f = Popen("./mx", shell = True, stdin = PIPE, stdout = PIPE)
    #  tmp = nowflag + a + b + c
    f.stdin.write(tmp + '\n')
    stdout, _ = f.communicate()
    return stdout[: 3]

flag = "flag{change53233}"
dic = string.ascii_lowercase + string.digits
#  key = '\x5f\x70\x64\x6d'
#  key = '\x65\x37\x23\x37'
key = '\x65\x43\x30'

for a in dic:
    for b in '}':
        #  for c in "}":
       tmp = a + b
       print tmp
       stdout = run(tmp)
       if stdout == key:
           print "success"
           print tmp
           exit()

