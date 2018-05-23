
### leftleftrightright(150)
> 这个题学到了不少东西，值得认真写一下

下载好文件后发现是upx的壳，upx -d直接脱掉后运行，发现是经典的check输入的题目（作为一个linuxer，首先用wine模拟运行了一下，这也为我后来的解题减少了不少麻烦，后边会说到）

```bash
ISCC2018_re150 [master●●] file leftleftrightright.exe 
leftleftrightright.exe: PE32 executable (console) Intel 80386, for MS Windows, UPX compressed
ISCC2018_re150 [master●●] upx -d ./leftleftrightright.exe 
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2013
UPX 3.91        Markus Oberhumer, Laszlo Molnar & John Reiser   Sep 30th 2013

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
     18432 <-     10752   58.33%    win32/pe     leftleftrightright.exe

Unpacked 1 file.
ISCC2018_re150 [master●●] file leftleftrightright.exe 
leftleftrightright.exe: PE32 executable (console) Intel 80386, for MS Windows
ISCC2018_re150 [master●●] chmod +x leftleftrightright.exe 
ISCC2018_re150 [master●●] ./leftleftrightright.exe 
0009:fixme:msvcp:_Locinfo__Locinfo_ctor_cat_cstr (0x32fcbc 1 C) semi-stub
aaaaaaa
0009:fixme:msvcp:_Locinfo__Locinfo_ctor_cat_cstr (0x32fd1c 1 C) semi-stub
try again!
请按任意键继续...%                                          
```

拖到IDA里分析之前，先搜索了一波字符串，发现存在*IsDebuggerPresent*和疑似加密后的flag：*s_imsaplw_e_siishtnt{g_ialt}F*，如果需要调试，要先nop掉IsDebuggerPresent，先静态分析，拖到IDA里F5大法，main函数的伪代码和汇编都很乱，但大致可以看出把我们的输入经过一通操作后扔给sub_401090()函数check，通过即为正确的flag，同时能看出flag的长度为29(0x1D)

```C
  if ( sub_401090(v16) || v15 < 0x1D || (v17 = "flag is right!", v15 > 0x1D) )
    v17 = "try again!";
  v18 = sub_401BF0(std::cout, v17, sub_401E30);
  std::basic_ostream<char,std::char_traits<char>>::operator<<(v18, v19);
  system("pause");
```

这时首先想的是通过调试快速确定怎么对输入进行变化的，于是到windows下试图用Ollydbg调试（调试之前要先找到对IsDebuggerPresent的调用并nop掉，可以在IDA的import页面通过x交叉引用找到），这时遇到了第一个问题：文件在windows下直接crash
![](http://ww1.sinaimg.cn/large/006AWYXBly1frlj8wpy77j30j90d9gll.jpg)
扔进OD单步调试，很快就能定位到crash出现的位置
![](http://ww1.sinaimg.cn/large/006AWYXBly1frljf0y35uj30ss08ojrq.jpg)
crash出现的原因不难分析，此时[ds + 0x40600]是一个不可读的地址，这时候想起来windows vitia（writeup用的是windows 2008 server）及其以上版本引入了aslr技术，导致程序载入的基址是随机的，如果取值的地址是写死的（比如这道题），就很可能跳到不可读的地址，程序crash，细节可以看[这里](https://www.52pojie.cn/forum.php?mod=viewthread&tid=393505)
> 一些trick：
> - OD把代码当成数据分析时，可以选中，点退格让OD重新分析
> - ctrl + A可以重新分析当前模块的代码，也能把误识别的数据转为代码
 

同时找到了一个很方便的[工具](https://www.52pojie.cn/thread-377450-1-1.html)可以固定程序的载入地址，固定程序的载入地址随机化后，打开程序，终于可以正常工作了，于是上OD调试，跟了几步指令后忽然意识到，check函数没有进行查表，亦或这些操作，只有很简单的位移，这说明我们的输入并不会发生改变，只会发生移位，如果我们能得到一串字符移位后的结果，就可以找到移位的规律，进而恢复出flag
```C
//check函数不会改变输入
int __cdecl sub_401090(unsigned int a1)
{
  int v1; // ecx
  const char *v3; // esi
  unsigned int v4; // edx
  bool v5; // cf
  unsigned __int8 v6; // al
  unsigned __int8 v7; // al
  unsigned __int8 v8; // al

  if ( !a1 )
    return 0;
  v3 = "s_imsaplw_e_siishtnt{g_ialt}F";
  v4 = a1 - 4;
  if ( a1 < 4 )
  {
LABEL_6:
    if ( v4 == -4 )
      return 0;
  }
  else
  {
    while ( *(_DWORD *)v1 == *(_DWORD *)v3 )
    {
      v1 += 4;
      v3 += 4;
      v5 = v4 < 4;
      v4 -= 4;
      if ( v5 )
        goto LABEL_6;
    }
  }
  v5 = *(_BYTE *)v1 < (const unsigned __int8)*v3;
  if ( *(_BYTE *)v1 != *v3 )
    return -v5 | 1;
  if ( v4 != -3 )
  {
    v6 = *(_BYTE *)(v1 + 1);
    v5 = v6 < v3[1];
    if ( v6 != v3[1] )
      return -v5 | 1;
    if ( v4 != -2 )
    {
      v7 = *(_BYTE *)(v1 + 2);
      v5 = v7 < v3[2];
      if ( v7 != v3[2] )
        return -v5 | 1;
      if ( v4 != -1 )
      {
        v8 = *(_BYTE *)(v1 + 3);
        v5 = v8 < v3[3];
        if ( v8 != v3[3] )
          return -v5 | 1;
      }
    }
  }
  return 0;
}
```
于是我们直接在check函数之后下断点
![](http://ww1.sinaimg.cn/large/006AWYXBly1frlk5z6rqaj30so04ht9j.jpg)
运行，输入29位不同的数据后观察
![](http://ww1.sinaimg.cn/large/006AWYXBly1frlk9m8f5lj30hc0593yg.jpg)
找到了移位前后的字符串，这样就可以恢复flag了，脚本如下：
```python
ISCC2018_re150 [master●●] cat solve.py 
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

encrypt = "s_imsaplw_e_siishtnt{g_ialt}F"

before = "abcdefghijklmnopqrstuvwxyzABC"
after = "onpqmlrskjtuihvwgfxyedzAcbBCa"

flag = [encrypt[after.find(c)] for c in before]
print "".join(flag)
ISCC2018_re150 [master●●] python solve.py 
Flag{this_was_simple_isnt_it}
ISCC2018_re150 [master●●]
```
#### 以上是写writeup时偶然发现的新解法，新解法出现的原因应该是windows 2008 server的load机制与windows 10不同，windows 2008 server的更低级，原解法如下：
固定exe的装载基址后，发现运行到cin时，程序又crash了，这时才想到windows10下dll的装载基址也是随机的，通过比较aslr_disabler.exe处理前后的exe，发现只对pe头的一个字段改了一位（可以通过010 editor的compare功能看出），于是想到了两种思路：
1. 找到exe调用的dll，通过修改pe头固定其基址
2. 在od调试的过程中手动指定其基址

很明显第一种方法得不偿失，麻烦不说，很有可能造成系统环境的崩溃。于是尝试在OD调试的过程中指定dll的基址，试了一下发现要改的地方太多，放弃了。这个时候想到用wine模拟时程序可以正常运行，于是搜索了一下调试wine加载的程序的方法，google的所有结果都指向一个工具[winedbg](https://manpages.debian.org/stretch/wine-development/winedbg-development.1.en.html)，按照man手册的说明，还可以以gdb模式启动，尝试了一下，发现在自己电脑上各种报错，把patch后的exe发给一个用arch的大佬学弟试了一下，一次就成了（吐血），比较后发现是wine的版本问题，于是果断卸载了apt安装的2.0的wine，手动编译了一个3.8的wine，然后**winedbg --gdb ./leftleftrightright.exe**，终于跑起来了，之后的方法就和使用ollydbg时一样了，直接下断点查看处理前后的字符串即可
![](http://ww1.sinaimg.cn/large/006AWYXBly1frll07qhozj30nu0aktac.jpg)

patch后的exe和解题脚本可以在我的[github](https://github.com/M4xW4n9/reverse_repo/tree/master/ISCC2018_re150)上找到
