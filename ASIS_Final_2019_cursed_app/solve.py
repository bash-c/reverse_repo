#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ASIS{y0u_c4N_s33_7h15_15_34513R_7h4n_Y0u_7h1nk_r16h7?__!!!}
from subprocess import *
import string
import sys

command = "perf stat -x : -e instructions:u ./cursed_app.elf ./license 1>/dev/null"

flag = 'ASIS{'

def write_file(cont):
    with open("./license", "wb") as f:
        f.write(cont)

write_file(flag)
'''
Desktop cat license
ASIS{
Desktop perf stat -x : -e instructions:u ./cursed_app.elf ./license 1>/dev/null
167689::instructions:u:377798:100.00::
'''
ins_count = 167689
while True:
        delta = 0
	count_chr = ''
	for i in string.printable:
                write_file(flag + i)
		target = Popen(command, stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=True)
		target_output = target.communicate()
                #  import pdb;pdb.set_trace()
                #  print(target_output)
		instructions = int(target_output[0].split(':')[0])
		if ins_count + 20 > instructions > ins_count + 10:
			count_chr = i
                        delta = instructions - ins_count
			ins_count = instructions
                        break
	flag += count_chr
        print(delta, flag)
