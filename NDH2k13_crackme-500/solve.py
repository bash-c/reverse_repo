#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from os import system
import string
import commands

if __name__ == "__main__":
    dic = string.ascii_letters + string.digits + "+_ "
    pwd  = "________"
    idx = 0x0
    off  = 0x00
    sav  = 0x00
    while pwd.find("Good Password") == -1:
        pwd = pwd[:off] + dic[idx] + pwd[off+1:];
        '''
        NDH2k13_crackme-500 [master●] echo aaaaaaaa| /home/m4x/pin-3.6-97554-g31f0a167d-gcc-linux/pin -t ./myInscount.so -- ./crackme
        Jonathan Salwan loves you <3
        ----------------------------
        
        Password: Bad password
        Count 185559

        '''
        cmd = "echo %s| /home/m4x/pin-3.6-gcc-linux/pin -t ./myInscount.so -- ./crackme" %(pwd)
        #  print cmd
        #  print commands.getstatusoutput(cmd)[1]
        res = int(commands.getstatusoutput(cmd)[1].split("Count")[1])
        
        print "insert('%s') = %d ins" %(pwd, res)
        if sav == 0x00:
            sav = res
        if res - sav > 2000:
            off += 1
            if off >= len(pwd):
                break
            idx = 0x0
            sav = 0
        idx += 1
        sav = res

    print "The password is %s" %(pwd)
    system("echo %s| ./crackme" % pwd)
