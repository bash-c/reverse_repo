#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

# coding: utf-8

import angr


main_addr = 0x4028A0 # main函数入口

find = 0x402A04 # main函数结束处

flag_length = 68


# 搜索时避开的路径

avoid_lst = [

 0x400718,0x40079c,0x400820,0x4008a4,0x400928,0x4009ac,0x400a30,0x400aac,

 0x400b30,0x400bac,0x400c30,0x400cb4,0x400d38,0x400dbc,0x400e40,0x400ec4,

 0x400f48,0x400fcc,0x401050,0x4010d4,0x401158,0x4011dc,0x401260,0x4012e4,

 0x401368,0x4013ec,0x401470,0x4014f4,0x401578,0x4015fc,0x401680,0x4016fc,

 0x401780,0x401804,0x401888,0x40190c,0x401990,0x401a14,0x401a98,0x401b1c,

 0x401ba0,0x401c24,0x401ca8,0x401d2c,0x401db0,0x401e34,0x401eb8,0x401f3c,

 0x401fc0,0x402044,0x4020c8,0x40214c,0x4021d0,0x402254,0x4022d8,0x40235c,

 0x4023e0,0x402464,0x4024e8,0x40256c,0x4025f0,0x402674,0x4026f8,0x40277c,

 0x4027f8,0x40287c

]



p = angr.Project('release.stripped')


state = p.factory.blank_state(addr=main_addr)


# 约束：flag范围在可见字符内（32-127）

for i in range(flag_length-2):

 c = state.posix.files[0].read_from(1)

 state.solver.add(state.solver.And(c <= '~', c >= 0))


# 约束：flag最后两个字符为'}

c = state.posix.files[0].read_from(1)

state.solver.add(state.solver.And(c == "'"))

c = state.posix.files[0].read_from(1)

state.solver.add(state.solver.And(c == "}"))


# 约束：flag最后以\x00作字符串结尾结束

c = state.posix.files[0].read_from(1)

state.solver.add(state.solver.And(c == "\x00"))


# 重定位输入到开始处（0），且长度为68

state.posix.files[0].seek(0)

state.posix.files[0].length = 68


ex = p.surveyors.Explorer(start=state, find=find, avoid=avoid_lst)


ex.run()


flag = ex._f.posix.dumps(0)

print flag

# hackim18{'W0W_Wow_W0W_WoW_y0u_h4v3_m4th_sk1ll5_W0oW_W0owOwo0w_Wo0W'}
