#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

import angr

p = angr.Project("./ppp")
state = p.factory.entry_state()

for _ in xrange(4):
    k = state.posix.files[0].read_from(1)
    state.se.add(k > 0x30)
    state.se.add(k < 0x40)

k = state.posix.files[0].read_from(1)
state.se.add(k == 0xa)
state.posix.files[0].seek(0)
state.posix.files[0].length = 5

sm = p.factory.simulation_manager(state)
sm.explore(find = 0x8048692, avoid = 0x80486A5)

if len(sm.found) > 0:
    inp = sm.found[0].posix.files[0].all_bytes()
    print sm.found[0].solver.eval(inp, cast_to = str)

