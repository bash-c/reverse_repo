### 1-bit-missile 
We know that it is a `bios rom` from the result of `strings ./rom`.

So we run it using `qemu-system-i386 -nographic -bios ./rom` and debugging with `qemu-system-i386 -nographic -bios ./rom -s -S`.

After attaching to the rom, we're able to dump the code in gdb using `dump binary memory dump.bin 0x100000 0xffffff`

> we know the start address is 0x100000 because "*Jumping to boot code at 00100000(07fd7000)*"
> 

Then we open dump.bin with IDA and rebase it to 0x100000. After searching strings, we find an interesting function like:
```C
void __cdecl __noreturn sub_10009E(char a1)
{
  char *a1a; // [esp+4h] [ebp-14h]

  print("FLAG if hit confirmed:");
  if ( (unsigned int)(data[19] ^ data[24]) < data[32] || (unsigned int)(data[19] ^ data[24]) > data[33] )
  {
    print("address out of scope!");
    sub_100160();
  }
  a1a = (char *)malloc(64);
  copy_str(a1a, (char *)(data[19] ^ data[24]));
  if ( *a1a )
    print(a1a);
  else
    print("MISSED!");
  sub_100160();
}
```

So we set a breakpoint at `0x100128`, which is:
```asm
seg000:00100122                 push    [ebp+a2]        ; a2
seg000:00100125                 push    [ebp+a1]        ; a1
seg000:00100128                 call    copy_str
seg000:0010012D                 add     esp, 10h
```

When we take a look in the debugger, we found the arg2 in `copy_str` points NULL, that's why the rom always prints `MISSED!`.
```asm
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
─────────────────────[ REGISTERS ]──────────────────────
 EAX  63 —▸ 0 ◂— 0x0
 EBX  0x7ff3798 —▸ 0x7fef0d9 —▸ 0x505f5342 —▸ 0 ◂— 0x0
 ECX  0x1086e8 —▸ 0x26c0 —▸ 0 ◂— 0x0
 EDX  0 ◂— 0x0
 EDI  0x100000 —▸ 0x906622eb —▸ 0 ◂— 0x0
 ESI  0x1b8 —▸ 0 ◂— 0x0
 EBP  0x10d498 —▸ 0x7ff4fd8 —▸ 0xa0000 —▸ 0 ◂— 0x0
 ESP  0x10d470 —▸ 0x1086a8 —▸ 0 ◂— 0x0
 EIP  0x100128 —▸ 0x3d68e8 —▸ 0 ◂— 0x0
───────────────────────[ DISASM ]───────────────────────
 ► 0x100128    call   0x103e95
 
   0x10012d    add    esp, 0x10
   0x100130    mov    eax, dword ptr [ebp - 0x14]
   0x100133    movzx  eax, byte ptr [eax]
   0x100136    test   al, al
   0x100138    jne    0x10014c
 
   0x10013a    sub    esp, 0xc
   0x10013d    push   0x10500d
   0x100142    call   0x103ca3
 
   0x100147    add    esp, 0x10
   0x10014a    jmp    0x10015a
───────────────────────[ STACK ]────────────────────────
00:0000│ esp  0x10d470 —▸ 0x1086a8 —▸ 0 ◂— 0x0
01:0004│      0x10d474 —▸ 0xc8000 —▸ 0 ◂— 0x0
02:0008│      0x10d478 —▸ 63 —▸ 0 ◂— 0x0
03:000c│      0x10d47c —▸ 1 —▸ 0 ◂— 0x0
04:0010│      0x10d480 —▸ 0x1b8 —▸ 0 ◂— 0x0
05:0014│      0x10d484 —▸ 0x1086a8 —▸ 0 ◂— 0x0
06:0018│      0x10d488 —▸ 0xc8000 —▸ 0 ◂— 0x0
07:001c│      0x10d48c —▸ 64 —▸ 0 ◂— 0x0
Breakpoint *0x100128
pwndbg> x/s 0xc8000
0xc8000:	""
```

So we search `flag` and found that:
```asm
pwndbg> find /w 0xa0000, 0xe0000, 0x67616c66
0xc0000
1 pattern found.
pwndbg> x/3s 0xc0000
0xc0000:	"flag{xxxxxxxxxx"...
0xc000f:	'x' <repeats 15 times>...
0xc001e:	"xxxxxx}"
```

Clearly, if we change `data[19] ^ data[24] == 0xc0000`, we will get flag.

There are two options:
1. modify 0xef5a3f92 to 0xef5abf92(data[24])
2. modify 0xef56bf92 to 0xef563f92(data[19])

Finally, option 2 works.
```bash
1-bit-missile nc arcade.fluxfingers.net 1816
Enter target byte [0 - 262143]: 194401
]> 10111111 <[
Enter target bit: [0 - 7]: 7
}X> ---------------------------------------{0}
]> 00111111 <[
......
flag{only_cb_can_run_this_simple_elf}
```
