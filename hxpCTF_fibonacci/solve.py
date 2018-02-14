#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from unicorn import *
#  from unicorn.x86_const import *
from unicorn.x86_const import UC_X86_REG_RDI as RDI, UC_X86_REG_RIP as RIP, UC_X86_REG_RSP as RSP, UC_X86_REG_RSI as RSI, UC_X86_REG_RAX as RAX
from pwn import u32, p32

def read(name):
    with open(name) as f:
        return f.read()

stack = [] #storing the arguments
d = {} #holds ret values

def hookCode(mu, addr, size, userData):
    #  print ">>> Tracing instruction at 0x%x, instruction size = 0x%x" % (addr, size)

    funcEntry = 0x400670
    funcRet = [0x4006F1, 0x400709]

    skipList = [0x4004EF, 0x4004F6, 0x400502, 0x40054F]
    if addr in skipList:
        mu.reg_write(RIP, addr + size)

    elif addr == 0x400560:
        print chr(mu.reg_read(RDI)),
        mu.reg_write(RIP, addr + size)

    elif addr == funcEntry:
        arg0 = mu.reg_read(RDI)
        rrsi = mu.reg_read(RSI)
        arg1 = u32(mu.mem_read(rrsi, 4))

        if (arg0, arg1) in d:
            (retVal, retRef) = d[(arg0, arg1)]
            mu.reg_write(RAX, retVal)
            mu.mem_write(rrsi, p32(retRef))
            mu.reg_write(RIP, 0x400582)

        else:
            stack.append((arg0, arg1, rrsi))

    elif addr in funcRet:
        (arg0, arg1, rrsi) = stack.pop()

        retVal = mu.reg_read(RAX)
        retRef = u32(mu.mem_read(rrsi, 4))
        d[(arg0, arg1)] = (retVal, retRef)

mu = Uc(UC_ARCH_X86, UC_MODE_64)#架构类型， 架构细节说明

base = 0x400000 #二进制文件机制
stackAddr = 0x0 #栈基址
stackSize = 1024 * 1024 #栈大小

# mem_map映射内存
mu.mem_map(base, 1024 * 1024)
mu.mem_map(stackAddr, stackSize)

mu.mem_write(base, read("./fibonacci")) #加载二进制文件到基址
mu.reg_write(RSP, stackAddr + stackSize - 1) #设置rsp指向申请的栈空间底部

mu.hook_add(UC_HOOK_CODE, hookCode)
mu.emu_start(0x4004E0, 0x400575) #开始地址和结束地址
