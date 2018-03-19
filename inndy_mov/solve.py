#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from subprocess import Popen, PIPE
from string import printable

ans = "FLAG{"
while True:
    if "}" in ans:
        print ans
        break

    
    for c in printable:
        f = Popen("./mov", shell = True, stdin = PIPE, stdout = PIPE)
        tmp = ans + c
        f.stdin.write(tmp + "\n")
        
        stdout, stderr = f.communicate()
        if "Good" in stdout:
            ans = tmp
            print ans
            break

