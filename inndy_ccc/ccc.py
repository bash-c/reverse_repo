#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'
import binascii
import string
import pdb

hashes = [0x0D641596F, 0x80A3E990, 0x0C98D5C9B, 0x0D05AFAF, 0x1372A12D, 0x5D5F117B, 0x4001FBFD, 0x0A7D2D56B, 0x7D04FB7E, 0x2E42895E, 0x61C97EB3, 0x84AB43C3, 0x9FC129DD, 0x0F4592F4D]

def crc(s, cnt):
    for a in dic:
        for b in dic:
            for c in dic:
                ans = s + a + b + c
                #  print tmp
                if (binascii.crc32(ans) & 0xffffffff) == hashes[cnt]:
                    #  pdb.set_trace()
                    return ans

#  dic = string.ascii_letters + string.digits + " _-{},"
dic = string.printable
#  ans = 'FLAG{'
ans = ''
cnt = 0
while True:
    try:
        ans = crc(ans, cnt)
        cnt += 1
        print ans
    except:
        break
