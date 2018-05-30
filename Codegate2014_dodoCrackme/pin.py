#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from subprocess import Popen, PIPE
from sys import argv
import string
import pdb

pinPath = "/home/m4x/pin-3.6-gcc-linux/pin"
pinInit = lambda tool, elf: Popen([pinPath, '-t', tool, '--', elf], stdin = PIPE, stdout = PIPE)
pinWrite = lambda cont: pin.stdin.write(cont)
pinRead = lambda : pin.communicate()[0]

if __name__ == "__main__":
    flag = argv[1]
    dic = map(chr, range(32, 128))
    while True:
        last = 0
        for i in dic:
            #  pdb.set_trace()
            pin = pinInit("./myInscount1.so", "./crackme")
            pinWrite(flag + i)
            #  print pinRead()
            now = int(pinRead().split('Count')[1])
            print "input({}) -> ins({}) -> delta({})".format(flag + i, now, now - last)
        
            if now - last < 0:
                flag = flag + i
                print "flag now: {}".format(flag)
        
                if len(flag) == 31:
                    print "Find flag: {}".format(flag)
                    exit()
        
                break

            last = now

