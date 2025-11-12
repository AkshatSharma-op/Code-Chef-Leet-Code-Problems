a=[3,10]
b=[5,8]
c=sorted(a+b)
l=len(c)
q=l//2
if l%2==0:
    m=(c[q-1]+c[q])/2
else:
    m=c[q] 
print('median',m)   