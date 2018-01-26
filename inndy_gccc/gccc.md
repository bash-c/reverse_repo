#### 0x04 gccc

该题的逻辑很简单,只有一个输入,下载文件后发现gccc.exe为.Net(C#)架构,因此用C#的反编译工具(这里用了)反编译得到题目代码如下:

```c#
// GrayCCC
public static void Main()
{
	Console.Write("Input the key: ");
	uint num;
	if (!uint.TryParse(Console.ReadLine().Trim(), out num))
	{
		Console.WriteLine("Invalid key");
		return;
	}
	string text = "";
	string text2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ{} ";
	int num2 = 0;
	byte[] array = new byte[]
	{
		164, 25, 4, 130, 126, 158, 91, 199, 173, 252, 239, 143, 150, 251, 126, 
		39, 104, 104, 146, 208, 249, 9, 219, 208, 101, 182, 62, 92, 6, 27, 5, 46
	};
	byte b = 0;
	while (num != 0u)
	{
		char c = (char)(array[num2] ^ (byte)num ^ b);
		if (!text2.Contains(new string(c, 1)))
		{
			Console.WriteLine("Invalid key");
			return;
		}
		text += c;
		b ^= array[num2++];
		num >>= 1;
	}
	if (text.Substring(0, 5) != "FLAG{" || text.Substring(31, 1) != "}")
	{
		Console.WriteLine("Invalid key");
		return;
	}
	Console.WriteLine("Your flag is: " + text);
}
```

可以看到,逻辑很简单,对输入进行了32轮验证,通过每一层验证即可得到flag.

但逻辑简单并不意味着容易解决,仔细分析代码可以看出解题的关键在求出num的值,num经过32次右移一位后等于0,因此取值范围为**[2 ^ 31, 2 ^ 32)**, 在该范围内找到满足32轮验证的值即可,但在找到该值时遇到了问题,如果单纯爆破的话,2 ^ 32 - 2 ^ 31次爆破远远超出了能接受的范围,因此考虑用z3来解决这个多约束问题.

该题的约束条件有如下几个:

- 0~5位为"FLAG{"
- 最后一位(31)为"}"
- 6~30位需在"ABCDEFGHIJKLMNOPQRSTUVWXYZ{} "内

因此可以写出z3的代码如下:

```python
def getNum():
	b = 0
	num2 = 0
	# 2 ** 30 <= num < 2 ** 31
	s = Solver()
	num = BitVec('num', 64)
	s.add(num >= 2 ** 31)
	s.add(num < 2 ** 32)
	# s.add(num > 1510650850)

	for i in xrange(32):
		if i < 5:
			s.add(((array[num2] ^ (num & 0x7f) ^ b) & 0x7f) == ord('FLAG{'[i]))
		elif 5 <= i < 31:
			s.add(
					Or(	
						And(
							((array[num2] ^ (num & 0x7f) ^ b) & 0x7f) >= 65, 
							((array[num2] ^ (num & 0x7f) ^ b) & 0x7f) <= 90, 
						),
						
						# ((array[num2] ^ (num & 0x7f) ^ b) & 0x7f) == ord('{'),
						# ((array[num2] ^ (num & 0x7f) ^ b) & 0x7f) == ord('}'),
						((array[num2] ^ (num & 0x7f) ^ b) & 0x7f) == ord(' ')

					)
				)
                elif i == 31:
                        s.add(((array[num2] ^ (num & 0x7f) ^ b) & 0x7f) == ord('}'))
		b ^= array[num2]
		b &= 0x7f
		num2 += 1
		num >>= 1

	if s.check() == sat:
		print s.model()
                #bug
		#  print s.model()[num].as_long()
	# while s.check() == sat:
		# print s.model()[num]
		# s.add(Or(num != s.model()[num].as_long()))
```

运行,num的值就秒出了

![](https://ws1.sinaimg.cn/large/006AWYXBly1fmyovxowozj30hw03975k.jpg)

> 注释掉的部分是一个还没解决的bug,本来是想通过添加约束跑出所有的可行解,但可能是因为用了BitVec导致在数据类型的转换上有些问题,现在只跑出了一组解.等到考完试再来修这个bug

有了num的值,接下类有很简单了,可用python求解

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = "M4x"

import pdb
from z3 import *
array = [164,25, 4, 130, 126, 158, 91, 199, 173, 252, 239, 143, 150, 
251, 126, 39, 104, 104, 146, 208, 249, 9, 219, 208, 101, 
182, 62, 92, 6, 27, 5, 46]
# print len(array)

def getNum():
	b = 0
	num2 = 0
	# 2 ** 30 <= num < 2 ** 31
	s = Solver()
	num = BitVec('num', 64)
	s.add(num >= 2 ** 31)
	s.add(num < 2 ** 32)
	# s.add(num > 1510650850)

	for i in xrange(32):
		if i < 5:
			s.add(((array[num2] ^ (num & 0x7f) ^ b) & 0x7f) == ord('FLAG{'[i]))
		elif 5 <= i < 31:
			s.add(
					Or(	
						And(
							((array[num2] ^ (num & 0x7f) ^ b) & 0x7f) >= 65, 
							((array[num2] ^ (num & 0x7f) ^ b) & 0x7f) <= 90, 
						),
						
						# ((array[num2] ^ (num & 0x7f) ^ b) & 0x7f) == ord('{'),
						# ((array[num2] ^ (num & 0x7f) ^ b) & 0x7f) == ord('}'),
						((array[num2] ^ (num & 0x7f) ^ b) & 0x7f) == ord(' ')

					)
				)
                elif i == 31:
                        s.add(((array[num2] ^ (num & 0x7f) ^ b) & 0x7f) == ord('}'))
		b ^= array[num2]
		b &= 0x7f
		num2 += 1
		num >>= 1

	if s.check() == sat:
		print s.model()
                #bug
		#  print s.model()[num].as_long()
	# while s.check() == sat:
		# print s.model()[num]
		# s.add(Or(num != s.model()[num].as_long()))

def getFlag():
	text2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ{} "
	num = 3658134498
	num2 = 0
	b = 0 
	flag = ""

	while num:
		c = chr((array[num2] ^ (num & 0x7f) ^ b) & 0x7f)
		if c not in text2:
			print ord(c)
		flag += c
		b ^= array[num2]
		num2 += 1
		num >>= 1
		print flag

#  getNum()
getFlag()
```

也可简单的修改反编译得到的c#代码,运行C#得到flag(推荐该方法)

```c#
// GrayCCC
using System;
namespace GrayCCC
{
	class GCCC
	{
		public static void Main()
		{
			// Console.Write("Input the key: ");
			// uint num;
			// if (!uint.TryParse(Console.ReadLine().Trim(), out num))
			// {
			// 	Console.WriteLine("Invalid key");
			// 	return;
			// }
			string text = "";
			string text2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ{} ";
			int num2 = 0;
			uint num = 3658134498;
			byte[] array = new byte[]
			{
				164,25, 4, 130, 126, 158, 91, 199, 173, 252, 239, 143, 150, 
				251, 126, 39, 104, 104, 146, 208, 249, 9, 219, 208, 101, 
				182, 62, 92, 6, 27, 5, 46
			};
			
			byte b = 0;
			while (num != 0u)
			{
				char c = (char)(array[num2] ^ (byte)num ^ b);
				if (!text2.Contains(new string(c, 1)))
				{
					Console.WriteLine("Invalid key");
					return;
				}
				text += c;
				b ^= array[num2++];
				num >>= 1;
				Console.WriteLine(text);
			}
			if (text.Substring(0, 5) != "FLAG{" || text.Substring(31, 1) != "}")
			{
				Console.WriteLine("Invalid key");
				return;
			}
			Console.WriteLine("Your flag is: " + text);
		}
	}
}
```

![](https://ws1.sinaimg.cn/large/006AWYXBly1fmypbvcrrwj311y0lc40y.jpg)



> 可以看出,通过z3求解此类多约束问题能极大地提高效率.
>
> 另外听Kira师傅说这道题也可以诸位爆破,也等到考完试再来填坑吧.

