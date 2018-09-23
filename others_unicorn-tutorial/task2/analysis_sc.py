#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unicorn.x86_const import UC_X86_REG_ESP as ESP, UC_X86_REG_EAX as EAX, UC_X86_REG_EBX as EBX, UC_X86_REG_ECX as ECX, UC_X86_REG_EDX as EDX, UC_X86_REG_ESI as ESI, UC_X86_REG_EDI as EDI, UC_X86_REG_EIP as EIP
from unicorn.x86_const import *
from unicorn import *
import json
import pdb

BASE = 0x400000
STACK_BASE = 0x0
STACK_SIZE = 1024 * 1024
shellcode = "\xe8\xff\xff\xff\xff\xc0\x5d\x6a\x05\x5b\x29\xdd\x83\xc5\x4e\x89\xe9\x6a\x02\x03\x0c\x24\x5b\x31\xd2\x66\xba\x12\x00\x8b\x39\xc1\xe7\x10\xc1\xef\x10\x81\xe9\xfe\xff\xff\xff\x8b\x45\x00\xc1\xe0\x10\xc1\xe8\x10\x89\xc3\x09\xfb\x21\xf8\xf7\xd0\x21\xd8\x66\x89\x45\x00\x83\xc5\x02\x4a\x85\xd2\x0f\x85\xcf\xff\xff\xff\xec\x37\x75\x5d\x7a\x05\x28\xed\x24\xed\x24\xed\x0b\x88\x7f\xeb\x50\x98\x38\xf9\x5c\x96\x2b\x96\x70\xfe\xc6\xff\xc6\xff\x9f\x32\x1f\x58\x1e\x00\xd3\x80"

def hook_code(mu, addr, size, user_data):
    opcode = mu.mem_read(addr, size)
    if opcode == '\xcd\x80':
        hook_result = {}
        eax = mu.reg_read(EAX)
        hook_result.update({"eax": eax})
        ebx = mu.reg_read(EBX)
        hook_result.update({"ebx": ebx})
        ecx = mu.reg_read(ECX)
        hook_result.update({"ecx": ecx})

        if eax == 15:
            #  pdb.set_trace()
            filename = mu.mem_read(ebx, 32).split('\0')[0]
            print "filename: ", filename
            print "attri: ", oct(ecx)
        elif eax == 0:
            print "Exit..."

        edx = mu.reg_read(EDX)
        hook_result.update({"edx": edx})
        esi = mu.reg_read(ESI)
        hook_result.update({"esi": esi})
        edi = mu.reg_read(EDI)
        hook_result.update({"edi": edi})
        
        print "Find syscall:"
        print json.dumps(hook_result, indent = 4, separators = (",", ":"))

        mu.reg_write(EIP, addr + size)
        if eax == 1:
            exit()

if __name__ == "__main__":
    mu = Uc(UC_ARCH_X86, UC_MODE_32)

    mu.mem_map(BASE, 1024 * 1024)
    mu.mem_map(STACK_BASE, STACK_SIZE)

    mu.mem_write(BASE, shellcode)
    mu.reg_write(ESP, STACK_BASE + STACK_SIZE / 2)

    mu.hook_add(UC_HOOK_CODE, hook_code)
    mu.emu_start(BASE, BASE - 1)

