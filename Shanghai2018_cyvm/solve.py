#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import angr
import claripy

p = angr.Project("./cyvm")

chars = [claripy.BVS('flag_{}'.format(i), 8) for i in range(32)]
#  print(chars)
flag = claripy.Concat(*chars + [claripy.BVV(b'\n')])

st = p.factory.blank_state(addr = 0x400CB1, stdin = flag)

for c in chars:
    st.solver.add(c >= 32)
    st.solver.add(c <= 126)

st.solver.add(chars[0] == 'f')
st.solver.add(chars[1] == 'l')
st.solver.add(chars[2] == 'a')
st.solver.add(chars[3] == 'g')
st.solver.add(chars[4] == '{')

sm = p.factory.simulation_manager(st)
sm.explore(find = 0x400CD2)

#  import pdb; pdb.set_trace()
print(sm.found[0].posix.dumps(0))
