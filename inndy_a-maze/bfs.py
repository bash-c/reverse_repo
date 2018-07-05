import struct

f=open('./map','rb')
d=f.read()
f.close()

#  print d
p=[]
for i in d:
	p.append(0)
#  print p

c=[(0,'')]


while len(c)!=0:
        f=c[0]
        c.pop(0)
        if(len(f[1])>12):
                print(f[1])
        for i in range(32,127):
                index=(f[0]<<9)+4*i
                if(index>len(d)):
                        continue
                t=struct.unpack('<L',d[index:index+4])[0]
                if(t==-1):
                        #  print(f[1]+chr(i))
                        continue
                else:
                        if(t<len(d) and p[t]<=10):
                                c.append((t,f[1]+chr(i)))
                                p[t]+=1

print f[1]
