#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

# Imports from Miasm framework
from miasm2.core.bin_stream                 import bin_stream_str
from miasm2.arch.x86.disasm                 import dis_x86_32
from miasm2.arch.x86.ira                    import ir_a_x86_32
from miasm2.arch.x86.regs                   import all_regs_ids, all_regs_ids_init
from miasm2.ir.symbexec                     import symbexec
from miasm2.expression.simplifications      import expr_simp

# Binary path and offset of the target function
offset = 0x3e0
fname = "./re"

# Get Miasm's binary stream
bin_file = open(fname).read()
bin_stream = bin_stream_str(bin_file)

# Disassemble blocks of the function at 'offset'
mdis = dis_x86_32(bin_stream)
disasm = mdis.dis_multibloc(offset)

# Create target IR object and add all basic blocks to it
ir = ir_a_x86_32(mdis.symbol_pool)
for bbl in disasm: ir.add_bloc(bbl)

# Init our symbols with all architecture known registers
symbols_init =  {}
for i, r in enumerate(all_regs_ids):
    symbols_init[r] = all_regs_ids_init[i]

# Create symbolic execution engine
symb = symbexec(ir, symbols_init)

# Get the block we want and emulate it
# We obtain the address of the next block to execute
block = ir.get_bloc(offset)
nxt_addr = symb.emulbloc(block)

# Run the Miasm's simplification engine on the next
# address to be sure to have the simplest expression
simp_addr = expr_simp(nxt_addr)

# The simp_addr variable is an integer expression (next basic block offset)
if isinstance(simp_addr, ExprInt):
  print("Jump on next basic block: %s" % simp_addr)

# The simp_addr variable is a condition expression
elif isinstance(simp_addr, ExprCond):
  branch1 = simp_addr.src1
  branch2 = simp_addr.src2
  print("Condition: %s or %s" % (branch1,branch2))
