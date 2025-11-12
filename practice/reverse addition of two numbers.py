a=[2,4,3]
b=[5,6,4]
a1=int(''.join(map(str,a[::-1])))
b1=int(''.join(map(str,b[::-1])))
s=a1+b1
s1=list(map(int,str(s)[::-1]))
# s1=list(map(int,''.join(str(s)[::-1]).split()))
print(s1)
