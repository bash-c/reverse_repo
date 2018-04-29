### 2ex (solved)

```bash
2ex echo -n 0| ./mx| hd
00000000  65 40 40 40 40 40 40 40  40 40 40 40 24 3d 5d 5e  |e@@@@@@@@@@@$=]^|
00000010  40 40 40 40 40 40 40 3d  0a                       |@@@@@@@=.|
00000019
2ex echo -n 00| ./mx| hd
00000000  65 31 40 40 40 40 40 40  40 40 40 40 24 3d 5d 5e  |e1@@@@@@@@@@$=]^|
00000010  40 40 40 40 40 40 40 3d  0a                       |@@@@@@@=.|
00000019
2ex echo -n 000| ./mx| hd
00000000  65 31 40 2a 40 40 40 40  40 40 40 40 24 3d 5d 5e  |e1@*@@@@@@@@$=]^|
00000010  40 40 40 40 40 40 40 3d  0a                       |@@@@@@@=.|
00000019
2ex echo -n 0000| ./mx| hd
00000000  65 31 40 2a 65 40 40 40  40 40 40 40 24 3d 5d 5e  |e1@*e@@@@@@@$=]^|
00000010  40 40 40 40 40 40 40 3d  0a                       |@@@@@@@=.|
00000019
2ex echo -n 00000| ./mx| hd
00000000  65 31 40 2a 65 31 40 40  40 40 40 40 24 3d 5d 5e  |e1@*e1@@@@@@$=]^|
00000010  40 40 40 40 40 40 40 3d  0a                       |@@@@@@@=.|
00000019
2ex echo -n 000000| ./mx| hd
00000000  65 31 40 2a 65 31 40 2a  40 40 40 40 24 3d 5d 5e  |e1@*e1@*@@@@$=]^|
00000010  40 40 40 40 40 40 40 3d  0a                       |@@@@@@@=.|
00000019
2ex hd out 
00000000  e2 94 82 5f 72 2d 2b 5f  43 6c 35 3b 76 67 71 5f  |..._r-+_Cl5;vgq_|
00000010  70 64 6d 65 37 23 37 65  43 30 3d 0a              |pdme7#7eC0=.|
0000001c
2ex 
```
Every three-byte input makes four-byte output, so it's easy to brute three-byte by three-byte.
I write a simple script to brute every three-byte input:
```python
2ex cat brute.py 
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from subprocess import Popen, PIPE
import string

def run(tmp):
    f = Popen("./mx", shell = True, stdin = PIPE, stdout = PIPE)
    #  tmp = nowflag + a + b + c
    f.stdin.write(tmp + '\n')
    stdout, _ = f.communicate()
    return stdout[: 3]

flag = "flag{change53233}"
dic = string.ascii_lowercase + string.digits
#  key = '\x5f\x70\x64\x6d'
#  key = '\x65\x37\x23\x37'
key = '\x65\x43\x30'

for a in dic:
    for b in '}':
        #  for c in "}":
       tmp = a + b
       print tmp
       stdout = run(tmp)
       if stdout == key:
           print "success"
           print tmp
           exit()
```

