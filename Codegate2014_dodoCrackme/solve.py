#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from subprocess import Popen, PIPE
from sys import argv

pinPath = "/home/m4x/pin-3.6-gcc-linux/pin"
flag = argv[1]

dic = map(chr, range(32, 128))

while True:
    last = 0
    for i in dic:
        pin = Popen([pinPath, '-t', './myInscount1.so', '--', './crackme'], stdin = PIPE, stdout = PIPE)
        pin.stdin.write(flag + i)
        out, err = pin.communicate()
        now = int(out.split('Count')[1])
        print "input({}) -> ins({}) -> delta({})".format(flag + i, now, now - last)

        if now - last < 0:
            flag = flag + i
            print "flag now: {}".format(flag)

            if len(flag) == 31:
                print "Find flag: {}".format(flag)
                exit()

            break

        last = now
